# Copyright (C) 2017 Mikael Hallendal <hallski@hallski.org>

import urwid
from memorybank.core import MemoryBank
from memorybank.memory import Memory
from memorybank.fake_data import *

import asyncio


palette = [
    ('title', 'light blue', 'black'),
    ('header', 'white', 'dark blue'),
    ('active_memory', 'yellow', 'black'),
    ('active_note', 'white', 'black'),
    ('selected_menu_item', 'white', 'dark green'),
    ('main_box', 'light blue', 'black'),
    ('background', 'dark green', 'black')]


active_memory = urwid.Text(('active_memory', 'World of Warcraft'),
                           align='left')

parents = ['Blizzard Entertainment', 'Roleplaying Games', 'MMORPG', 'Fantasy']
children = ['Azeroth', 'Illidan', 'Wrath of the Litch King', 'Draenor']
siblings = ['Diablo', 'Starcraft', 'Warcraft', 'Guild Wars', 'Rift']
related = ['Warcraft', 'MMO Champion', 'Dark Legacy Comics']


memory_bank = create_fake_memory_bank()
a_memory = memory_bank.find_memory('World of Warcraft')


# Temporary testing out to see how it looks with a number at the front.
# The idea is to allow for simply pressing the number and <enter> to
# select the specific memory
nr = 0


class MBButton(urwid.Button):
    def __init__(self, caption, callback):
        global nr
        nr += 1
        super(MBButton, self).__init__("")
        urwid.connect_signal(self, 'click', callback, caption)
        s = '{0}. {1}'.format(nr, caption)
        self._w = urwid.AttrMap(urwid.SelectableIcon(s, 0),
                                None, focus_map='selected_menu_item')


def clicked(button, string):
    active_memory.set_text(('active_memory', string))


def wrap_button(string):
    return MBButton(string, clicked)


def wrap_list_items(item_list, wrap_function):
    return [wrap_function(item) for item in item_list]


def exit_on_q(event):
    if event in ('q', 'Q'):
        raise urwid.ExitMainLoop()


def get_active_memory():
    note = urwid.Text(('active_note', a_memory.note))
    pile = urwid.Pile([('pack', active_memory),
                       ('pack', urwid.Divider()),
                       ('pack', note)])
    pile = urwid.Padding(pile, left=2, right=1)
    lb = urwid.AttrMap(pile, 'main_box')
    return lb


def get_parents_widget():
    return create_relation_frame('Parent Memories', parents)


def get_children_widget():
    return create_relation_frame('Child Memories', children)


def get_list_widget(items):
    walker = urwid.SimpleFocusListWalker(wrap_list_items(items, wrap_button))
    widget = urwid.ListBox(walker)
    return widget


def get_related_widget():
    return create_relation_frame('Related Memories', related)


def create_relation_frame(title, items):
    title = urwid.Text(('title', title))
    pile = urwid.Pile([('pack', urwid.Divider()), get_list_widget(items)])
    return urwid.Frame(pile, header=title)


def get_siblings_widget():
    return create_relation_frame('Sibling Memories', items=siblings)


def get_header_widget():
    text = urwid.Text('Memory Bank - 0.1', align='center')
    return urwid.AttrMap(text, 'header')


def main():
    pile_left = urwid.Pile([get_parents_widget(),
                            ('pack', urwid.Divider(top=1)),
                            get_children_widget()])
    pile_left = urwid.Padding(pile_left, left=1, right=1)
    pile_right = urwid.Pile([get_siblings_widget(),
                             ('pack', urwid.Divider(top=1)),
                             get_related_widget()])
    pile_right = urwid.Padding(pile_right, left=1, right=1)

    cols = urwid.Columns([('weight', 2, get_active_memory()),
                          ('weight', 1, pile_left),
                          ('weight', 1, pile_right)],
                         dividechars=2)

    main_pile = urwid.Pile([('pack', get_header_widget()),
                            ('pack', urwid.Divider(bottom=2)),
                            cols,
                            ('pack', urwid.Divider(top=2))])

    background = urwid.AttrMap(main_pile, 'background')

    #    event_loop = asyncio.get_event_loop()
    event_loop = urwid.AsyncioEventLoop(loop=asyncio.get_event_loop())
    loop = urwid.MainLoop(background, palette,
                          event_loop=event_loop,
                          unhandled_input=exit_on_q)
    loop.run()

    print('Bye for now!')


if __name__ == '__main__':
    main()
