# Copyright (C) 2017 Mikael Hallendal <hallski@hallski.org>

from memorybank.core import MemoryBank
from memorybank.cli.main_view import *
import urwid


class MainViewPresenter(object):
    def __init__(self, view, memorybank):
        self._view = view
        self._memorybank = memorybank
        self.active_memory = memorybank.start_memory

    @property
    def active_memory(self):
        return self._active_memory

    @active_memory.setter
    def active_memory(self, active_memory):
        self._active_memory = active_memory
        self._update_view()

    def _update_view(self):
        self._view.title = self.active_memory.title
        self._view.note = self.active_memory.note

        self._update_links()

    def _update_links(self):
        links = self._memorybank.get_links(self.active_memory)

        parents, children, siblings, related = ([], [], [], [])
        type_to_list = {'parent': parents,
                        'child': children,
                        'related': related}

        for link in links:
            if not link:
                continue
            memory, link_type = link
            memory_link = MemoryLink(memory.title, memory.db_id)
            l = type_to_list[link_type]
            l.append(memory_link)

        self._view.display_links({'parents': parents,
                                  'children': children,
                                  'related': related,
                                  'siblings': siblings})
