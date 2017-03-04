# Copyright (C) 2017 Mikael Hallendal <hallski@hallski.org>

from memorybank.memory import Memory
from memorybank.link import Link


class MemoryBank(object):
    def __init__(self, memory_store, link_store):
        self._memory_store = memory_store
        self._link_store = link_store

    def create_memory(self, title, note=''):
        memory = Memory(title, note=note)
        self._memory_store.insert(memory)
        return memory

    def save_memory(self, memory):
        self._memory_store.save(memory)

    def remove_memory(self, memory):
        links = self._link_store.find(memory)
        self._link_store.remove_links(links)
        self._memory_store.remove(memory)

    def link(self, memory_a, memory_b, link_type='child'):
        '''Links memory_a to memory_b with specified link_type'''
        previous_links = self.get_links(memory_a)
        if ((memory_b, link_type) in previous_links):
            return

        link = Link(memory_a, memory_b, link_type)
        self._link_store.insert(link)

    def get_links(self, memory):
        links = self._link_store.find(memory)

        return [l.get_relative_link_for_memory(memory) for l in links]

    def find_memory(self, title):
        return self._memory_store.find_by_title(title)
