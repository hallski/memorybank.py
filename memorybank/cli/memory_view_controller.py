# Copyright (C) 2017 Mikael Hallendal <hallski@hallski.org>

from memorybank.cli.command_input import CommandInput

class MemoryViewController(object):
    def __init__(self, view, memorybank):
        self._memorybank = memorybank
        self._view = view
        view.delegate = self

        self.active_memory = memorybank.start_memory
        self._command_input = CommandInput()
        self._command_input.delegate = self

    @property
    def active_memory(self):
        return self._active_memory

    @property
    def view(self):
        return self._view

    @active_memory.setter
    def active_memory(self, active_memory):
        self._active_memory = active_memory
        self._update_view()

    def enable_input(self, initial_text):
        self._view.display_input(initial_text)

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

    # Actions
    def memory_selected(self, identifier):
        '''Action called from the view when a memory link is activated'''
        memory = self._memorybank.find_memory_by_id(identifier)
        if memory:
            self.active_memory = memory
