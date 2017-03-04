# Copyright (C) 2017 Mikael Hallendal <hallski@hallski.org>

from memorybank.memory import Memory
from memorybank.link import Link


class MemoryBank(object):
    def __init__(self, memory_repository, link_repository):
        self._memory_repository = memory_repository
        self._link_repository = link_repository

    def create_memory(self, title, note=''):
        memory = Memory(title, note=note)
        self._memory_repository.insert(memory)
        return memory

    def save_memory(self, memory):
        self._memory_repository.save(memory)

    def link(self, memory_a, memory_b, link_type='child'):
        '''Links memory_a to memory_b with specified link_type'''
        previous_links = self.get_links(memory_a)
        if ((memory_b, link_type) in previous_links):
            return

        link = Link(memory_a, memory_b, link_type)
        self._link_repository.save(link)

    def get_links(self, memory):
        links = self._link_repository.find(memory)

        return [l.get_relative_link_for_memory(memory) for l in links]

    def find_memory(self, title):
        return self._memory_repository.find_by_title(title)
