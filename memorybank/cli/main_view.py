# Copyright (C) 2017 Mikael Hallendal <hallski@hallski.org>

import urwid

from collections import namedtuple
from functools import partial

#def get_list_widget(items):
#    walker = urwid.SimpleFocusListWalker(items) #wrap_list_items(items, wrap_button))
#    widget = urwid.ListBox(walker)
#    return widget

MemoryLink = namedtuple('MemoryLink', ['name', 'identifier'])

def create_relation_frame(title, items):
    title = urwid.Text(('title', title))
    pile = urwid.Pile([('pack', urwid.Divider()), urwid.ListBox(items)])
    return urwid.Frame(pile, header=title)


class MemoryLinkButton(urwid.Button):
    def __init__(self, caption, callback, callback_context):
        super(MemoryLinkButton, self).__init__("")
        urwid.connect_signal(self, 'click', callback, callback_context)
        self._w = urwid.AttrMap(urwid.SelectableIcon(caption, 0),
                                None, focus_map='selected_menu_item')

def wrap_item_in_button(callback, item):
    return MemoryLinkButton(item.name, callback, item.identifier)

class MainView(urwid.WidgetWrap):
    def __init__(self, controller):
        self._controller = controller
        urwid.WidgetWrap.__init__(self, self._create_widget_tree())

    @property
    def title(self):
        return self._active_memory_name.text

    @title.setter
    def title(self, title):
        self._active_memory_name.set_text(('active_memory', title))

    @property
    def note(self):
        return self._active_memory_note.text

    @note.setter
    def note(self, note):
        self._active_memory_note.set_text(('active_note', note))

    def display_parents(self, parents):
        self._update_link_list(self._parents, parents)

    def display_children(self, children):
        self._update_link_list(self._children, children)

    def display_siblings(self, siblings):
        self._update_link_list(self._siblings, siblings)

    def display_related(self, related):
        self._update_link_list(self._related, related)

    # Private
    def _clicked(self, button, identifier):
        self._controller.memory_selected(identifier)

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

    def _create_active_memory_frame(self):
        pile = urwid.Pile([('pack', self._active_memory_name),
                           ('pack', urwid.Divider()),
                           ('pack', self._active_memory_note)])
        padding = urwid.Padding(pile, left=2, right=1)
        return urwid.AttrMap(padding, 'main_box')

    def _create_header_widget(self):
        text = urwid.Text('Memory Bank - 0.1', align='center')
        return urwid.AttrMap(text, 'header')

    def _create_widget_tree(self):
        self._parents = urwid.SimpleFocusListWalker([])
        self._children = urwid.SimpleFocusListWalker([])
        self._siblings = urwid.SimpleFocusListWalker([])
        self._related = urwid.SimpleFocusListWalker([])

        self._active_memory_name = urwid.Text(('active_memory', ''), align='left')
        self._active_memory_note = urwid.Text(('active_note', ''))

        left_link_col = urwid.Pile([self._create_parents(),
                                    ('pack', urwid.Divider()),
                                    self._create_children()])
        right_link_col = urwid.Pile([self._create_siblings(),
                                     ('pack', urwid.Divider()),
                                     self._create_related()])

        cols = urwid.Columns([('weight', 2, self._create_active_memory_frame()),
                              ('weight', 1, left_link_col),
                              ('weight', 1, right_link_col)])

        main_pile = urwid.Pile([('pack', self._create_header_widget()),
                                ('pack', urwid.Divider(bottom=2)),
                                cols,
                                ('pack', urwid.Divider(top=2))])

        return urwid.AttrMap(main_pile, 'background')
