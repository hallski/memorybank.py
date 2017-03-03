# Copyright (C) 2017 Mikael Hallendal <hallski@hallski.org>

from memorybank.memory import Memory
from memorybank.link import Link


class MemoryBank(object):
    def __init__(self, database):
        self._database = database

    def create_memory(self, title, note=''):
        memory = Memory(title, note=note)
        self._database.save_memory(memory)
        return memory

    def link(self, memory_a, memory_b, link_type='child'):
        link = Link(memory_a, memory_b, link_type)
        self._database.save_link(link)

    def get_links(self, memory):
        links = self._database.find_links(memory)

        return [(c.memory_b, c.link_type)
                for c in links
                if c.memory_a == memory]

    def find_memory(self, title):
        return self._database.find_memory_by_title(title)
