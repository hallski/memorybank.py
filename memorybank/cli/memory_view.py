# Copyright (C) 2017 Mikael Hallendal <hallski@hallski.org>

import urwid
import weakref

from collections import namedtuple
from memorybank.cli.command_input import CommandInput


MemoryLink = namedtuple('MemoryLink', ['name', 'identifier'])


def create_relation_frame(title, items):
    title = urwid.Text(('title', title))
    listbox = urwid.ListBox(items)
    return urwid.Frame(listbox, header=title)


class MemoryLinkButton(urwid.Button):
    def __init__(self, caption, callback, callback_context):
        super(MemoryLinkButton, self).__init__("")
        urwid.connect_signal(self, 'click', callback, callback_context)
        self._w = urwid.AttrMap(urwid.SelectableIcon(caption, 0),
                                None, focus_map='selected_menu_item')


class MemoryView(urwid.WidgetWrap):
    def __init__(self):
        urwid.WidgetWrap.__init__(self, self._create_widget_tree())

    @property
    def delegate(self):
        return self._delegate

    @delegate.setter
    def delegate(self, delegate):
        self._delegate = weakref.proxy(delegate)

    @property
    def title(self):
        return self._title_widget.text

    @title.setter
    def title(self, title):
        self._title_widget.set_text(('active_memory', title))

    @property
    def note(self):
        return self._note_widget.text

    @note.setter
    def note(self, note):
        self._note_widget.set_text(('active_note', note))

    def display_links(self, links):
        '''Updates the link lists based on the values 'parents', 'children', 'siblings'
           and 'related' in the links dictionary'''
        self._update_link_list(self._parents, links['parents'])
        self._update_link_list(self._children, links['children'])
        self._update_link_list(self._siblings, links['siblings'])
        self._update_link_list(self._related, links['related'])

    def display_input(self, initial_text):
        self._input_widget.set_edit_text(initial_text)
        self._input_widget.edit_pos = len(initial_text)
        self._previous_focus = self._main_pile.focus_position
        a = urwid.AttrMap(self._input_widget, 'command_input')
        self._main_pile.contents.append((a, ('pack', None)))
        self._main_pile.set_focus(len(self._main_pile.contents) - 1)
        self._input_shown = True

    def keypress(self, size, key):
        key = super(MemoryView, self).keypress(size, key)
        if key == 'esc' and self._input_shown:
            self._input_shown = False
            del self._main_pile.contents[-1]
            self._main_pile.set_focus(self._previous_focus)
            return None
        return key

    # Private
    def _clicked(self, button, identifier):
        self.delegate.memory_selected(identifier)

    def _update_link_list(self, link_list, items):
        links = [MemoryLinkButton(item.name, self._clicked, item.identifier)
                 for item in items]

        del link_list[:]
        link_list.extend(links)

    def _create_parents(self):
        return create_relation_frame('Parents', items=self._parents)

    def _create_children(self):
        return create_relation_frame('Children', items=self._children)

    def _create_siblings(self):
        return create_relation_frame('Siblings', items=self._siblings)

    def _create_related(self):
        return create_relation_frame('Related', items=self._related)

    def _create_header_widget(self):
        text = urwid.Text('Memory Bank - 0.1', align='right')
        return urwid.AttrMap(text, 'header')

    def _create_footer_widget(self):
        text = urwid.Text('Menu', align='left')
        return urwid.AttrMap(text, 'footer')

    def _create_widget_tree(self):
        self._parents = urwid.SimpleFocusListWalker([])
        self._children = urwid.SimpleFocusListWalker([])
        self._siblings = urwid.SimpleFocusListWalker([])
        self._related = urwid.SimpleFocusListWalker([])

        self._input_widget = CommandInput()

        self._title_widget = urwid.Text(('active_memory', ''), align='center')
        self._note_widget = urwid.Text(('active_note', ''))

        note_box = urwid.Filler(self._note_widget, valign='top')

        links_col = urwid.Columns([self._create_parents(),
                                   self._create_children(),
                                   self._create_siblings(),
                                   self._create_related()],
                                  dividechars=1)

        nr_of_links_shown = 5
        links_col = urwid.BoxAdapter(links_col, nr_of_links_shown + 1)

        main_pile = urwid.Pile([('pack', self._create_header_widget()),
                                ('pack', urwid.Divider()),
                                ('pack', self._title_widget),
                                ('pack', urwid.Divider()),
                                ('pack', links_col),
                                ('pack', urwid.Divider()),
                                note_box,
                                ('pack', urwid.Divider())])

        self._main_pile = main_pile

        main_pile = urwid.Padding(main_pile, left=2, right=2)

        return urwid.AttrMap(main_pile, 'background')
