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


def wrap_list_items(item_list, wrap_function):
    return [wrap_function(item) for item in item_list]


def exit_on_q(event):
    if event in ('q', 'Q'):
        raise urwid.ExitMainLoop()


def get_parents_widget():
    parents_widget = urwid.Text('Parents goes here', align='center')
    return urwid.Filler(parents_widget)


def get_chilren_widget():
    children_widget = urwid.Text('Children goes here', align='center')
    return urwid.Filler(children_widget, 'middle')


def get_related_widget():
    related_walker = urwid.SimpleFocusListWalker(wrap_list_items(related, wrap_button))
    rel_list = urwid.ListBox(related_walker)
    return rel_list


def main():
    fill = urwid.Filler(active_memory, 'middle')
    related_list = urwid.Filler(get_related_widget(), 'middle')
    col = urwid.Columns([get_related_widget(), fill])

    main_pile = urwid.Pile([get_parents_widget(), col, get_chilren_widget()])
    background = urwid.AttrMap(main_pile, 'background')
    loop = urwid.MainLoop(background, palette, unhandled_input=exit_on_q)
    loop.run()

    print('Bye for now!')


if __name__ == '__main__':
    main()
