# Copyright (C) 2017 Mikael Hallendal <hallski@hallski.org>

import urwid

parents = ['Parent 1', 'Parent 2', 'Parent 3']
children = ['Child 1', 'Child 2', 'Child 3', 'Child 4', 'Child 5']
siblings = ['Sibling 1', 'Sibling 2', 'Sibling 3', 'Sibling 4', 'Sibling 5']
related = ['Related 1', 'Related 2', 'Related 3']

palette = [
    ('background', 'light green', 'black')]


active_memory = urwid.Text('Focused memory', align='center')


def wrap_text(string):
    return urwid.Text(string)


def clicked(button, string):
    active_memory.set_text(string)


def wrap_button(string):
    button = urwid.Button(string)
    urwid.connect_signal(button, 'click', clicked, string)
    return button


def wrap_item_list(item_list, wrap_function):
    return [wrap_function(item) for item in item_list]


def exit_on_q(key):
    if key.lower() in ('q'):
        raise urwid.ExitMainLoop()


def main():
    fill = urwid.Filler(active_memory, 'middle')
    walker = urwid.SimpleFocusListWalker(wrap_item_list(related, wrap_button))
    rel_list = urwid.ListBox(walker)
    pile = urwid.Pile([rel_list, fill])
    background = urwid.AttrMap(pile, 'background')
    loop = urwid.MainLoop(background, palette, unhandled_input=exit_on_q)
    loop.run()

    print('Bye for now!')


if __name__ == '__main__':
    main()
