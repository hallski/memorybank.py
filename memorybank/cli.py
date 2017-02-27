# Copyright (C) 2017 Mikael Hallendal <hallski@hallski.org>

import urwid

parents = ['Blizzard Entertainment', 'Roleplaying Games', 'MMORPG', 'Fantasy']
children = ['Azeroth', 'Illidan', 'Wrath of the Litch King', 'Draenor']
siblings = ['Diablo', 'Starcraft', 'Warcraft', 'Guild Wars', 'Rift']
related = ['Warcraft', 'MMO Champion', 'Dark Legacy Comics']

palette = [
    ('title', 'light blue', 'black'),
    ('header', 'white', 'dark blue'),
    ('active_memory', 'yellow', 'black'),
    ('debug1', 'yellow', 'dark red'),
    ('debug2', 'yellow', 'dark magenta'),
    ('debug3', 'yellow', 'dark green'),
    ('debug4', 'dark gray', 'yellow'),
    ('debug5', 'white', 'dark cyan'),
    ('background', 'light green', 'black')]


active_memory = urwid.Text('World of Warcraft', align='center')


class MBButton(urwid.Button):
    def __init__(self, caption, callback):
        super(MBButton, self).__init__("")
        urwid.connect_signal(self, 'click', callback, caption)
        self._w = urwid.AttrMap(urwid.SelectableIcon('> %s' % caption, 4),
                                None, focus_map='debug1')


def wrap_text(string):
    return urwid.Text(string)


def clicked(button, string):
    active_memory.set_text(string)


def wrap_button(string):
    return MBButton(string, clicked)


def wrap_list_items(item_list, wrap_function):
    return [wrap_function(item) for item in item_list]


def exit_on_q(event):
    if event in ('q', 'Q'):
        raise urwid.ExitMainLoop()


def wrap_with_palette(palette_name):
    def curried_decorator(func):
        def wrapper(*args, **kwargs):
            widget = func(*args, **kwargs)
            mapped = urwid.AttrMap(widget, palette_name)
            return mapped
        return wrapper
    return curried_decorator


@wrap_with_palette('active_memory')
def get_active_memory():
    filler = urwid.Filler(active_memory, 'top')
    return urwid.LineBox(filler, title='Active Memory')


# @wrap_with_palette('debug4')
def get_parents_widget():
    return create_relation_frame('Parents', parents + extra_values)


# @wrap_with_palette('debug2')
def get_children_widget():
    return create_relation_frame('Children', children + extra_values)


extra_values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


def get_list_widget(items):
    walker = urwid.SimpleFocusListWalker(wrap_list_items(items, wrap_button))
    widget = urwid.ListBox(walker)
    return widget


# @wrap_with_palette('debug3')
def get_related_widget():
    global extra_values
    return create_relation_frame('Related', related + extra_values)


def create_relation_frame(title, items):
    title = urwid.Text(('title', title))
    pile = urwid.Pile([('pack', urwid.Divider()), get_list_widget(items)])
    return urwid.Frame(pile, header=title)


# @wrap_with_palette('debug5')
def get_siblings_widget():
    return create_relation_frame('Siblings', items=siblings + extra_values)


def get_header_widget():
    text = urwid.Text('Memory Bank - 0.1', align='center')
    return urwid.AttrMap(text, 'header')


def main():
    pile_left = urwid.Pile([get_parents_widget(),
                            ('pack', urwid.Divider(top=1)),
                            get_siblings_widget()])
    pile_right = urwid.Pile([get_children_widget(),
                             ('pack', urwid.Divider(top=1)),
                             get_related_widget()])
    cols = urwid.Columns([('weight', 1, pile_left),
                          ('weight', 2, get_active_memory()),
                          ('weight', 1, pile_right)],
                         dividechars=5)

    main_pile = urwid.Pile([('pack', get_header_widget()),
                            ('pack', urwid.Divider(bottom=2)),
                            cols,
                            ('pack', urwid.Divider(top=2))])

    background = urwid.AttrMap(main_pile, 'background')
    loop = urwid.MainLoop(background, palette, unhandled_input=exit_on_q)
    loop.run()

    print('Bye for now!')


if __name__ == '__main__':
    main()
