from nose.tools import *
from memorybank.core import *
import unittest


class MemoryBankTest(unittest.TestCase):
    def setUp(self):
        self.database = TestDatabase()
        self.mbank = MemoryBank(self.database)

    def test_create_memory(self):
        memory = self.mbank.create_memory('Creating a new memory')
        assert_equal(memory.title, 'Creating a new memory')

    def test_find_memory(self):
        memory = self.mbank.create_memory('Memory to find')
        found_memory = self.mbank.find_memory('Memory to find')
        assert_equal(memory, found_memory)

    def test_connect_memories(self):
        memory_a = self.mbank.create_memory('Something to remember')
        memory_b = self.mbank.create_memory('Another thing to remember')
        self.mbank.link(memory_a, memory_b, link_type='child')

        links = self.mbank.get_links(memory_a)
        assert_equal(links[0], (memory_b, 'child'))

    def test_connect_memories_twice(self):
        memory_a = self.mbank.create_memory('First memory')
        memory_b = self.mbank.create_memory('Second memory')

        self.mbank.link(memory_a, memory_b, link_type='child')
        self.mbank.link(memory_a, memory_b, link_type='related')

        links = self.mbank.get_links(memory_a)
        assert_equal(len(links), 2)
        assert((memory_b, 'child') in links)
        assert((memory_b, 'related') in links)


class TestDatabase(object):
    def __init__(self):
        self.memories = []
        self.links = []

    def save_memory(self, memory):
        self.memories.append(memory)

    def save_link(self, link):
        self.links.append(link)

    def find_links(self, memory):
        return (c for c in self.links
                if c.memory_a == memory or c.memory_b == memory)

    def find_memory_by_title(self, title):
        return next(m for m in self.memories if m.title == title)
