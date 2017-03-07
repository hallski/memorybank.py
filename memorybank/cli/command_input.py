# Copyright (C) 2017 Mikael Hallendal <hallski@hallski.org>

import urwid
import weakref


class CommandInput(urwid.Edit):
    def __init__(self):
        urwid.register_signal(CommandInput, ['cancel'])
        super(CommandInput, self).__init__('> ')

    @property
    def delegate(self):
        return self._delegate

    @delegate.setter
    def delegate(self, delegate):
        self._delegate = weakref.proxy(delegate)

    def keypress(self, size, key):
        # Eat up and down
        if key in ('up', 'down'):
            return None
        return super(CommandInput, self).keypress(size, key)
