# Copyright (C) 2017 Mikael Hallendal <hallski@hallski.org>

from memorybank.core import MemoryBank
from memorybank.cli.main_view import *
import urwid

import asyncio

class MainViewPresenter(object):
    def __init__(self, view, memorybank, active_id):
        self._view = view
        loop = asyncio.get_event_loop()
        self._view.set_active_title('A title to remember')
        self._view.set_active_note("Is't this just awesome?")
        loop.call_later(1, self.replace_parents)
        loop.call_later(2, self.replace_children)
        loop.call_later(3, self.replace_siblings)
        loop.call_later(4, self.replace_related)

    def replace_parents(self):
        self._view.display_parents([MemoryLink('New item 1', 1),
                                    MemoryLink('New item 2', 2),
                                    MemoryLink('New item 3', 3)])

    def replace_children(self):
        self._view.display_children([MemoryLink('New item 1', 1),
                                     MemoryLink('New item 2', 2),
                                     MemoryLink('New item 3', 3)])

    def replace_siblings(self):
        self._view.display_siblings([MemoryLink('New item 1', 1),
                                     MemoryLink('New item 2', 2),
                                     MemoryLink('New item 3', 3)])


    def replace_related(self):
        self._view.display_related([MemoryLink('New item 1', 1),
                                    MemoryLink('New item 2', 2),
                                    MemoryLink('New item 3', 3)])
