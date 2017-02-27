# Copyright (C) 2017 Mikael Hallendal <hallski@hallski.org>

import urwid

parents = ['Blizzard Entertainment', 'Roleplaying Games', 'MMORPG', 'Fantasy']
children = ['Azeroth', 'Illidan', 'Wrath of the Litch King', 'Draenor']
siblings = ['Diablo', 'Starcraft', 'Warcraft', 'Guild Wars', 'Rift']
related = ['Warcraft', 'MMO Champion', 'Dark Legacy Comics']

palette = [
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


@wrap_with_palette('debug4')
def get_active_memory():
    return urwid.Filler(active_memory, 'top')


# @wrap_with_palette('debug4')
def get_parents_widget():
    return get_list_widget(parents)


# @wrap_with_palette('debug2')
def get_chilren_widget():
    return get_list_widget(children)


def get_list_widget(items):
    walker = urwid.SimpleFocusListWalker(wrap_list_items(items, wrap_button))
    widget = urwid.ListBox(walker)
    return widget


# @wrap_with_palette('debug3')
def get_related_widget():
    return get_list_widget(related)


# @wrap_with_palette('debug5')
def get_siblings_widget():
    return get_list_widget(siblings)


def main():
    under_cols = urwid.Columns([('weight', 1, get_related_widget()),
                                ('weight', 2, get_chilren_widget()),
                                ('weight', 1, get_siblings_widget())],
                               dividechars=5)
    main_pile = urwid.Pile([get_parents_widget(),
                            urwid.LineBox(get_active_memory()),
                            urwid.Padding(under_cols,
                                          left=2, right=2)])

    background = urwid.AttrMap(main_pile, 'background')
    loop = urwid.MainLoop(background, palette, unhandled_input=exit_on_q)
    loop.run()

    print('Bye for now!')


if __name__ == '__main__':
    main()
