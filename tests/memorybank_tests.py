from nose.tools import *
from memorybank.core import *
import unittest


class MemoryBankTest(unittest.TestCase):
    def setUp(self):
        self.mbank = MemoryBank()

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
        self.mbank.connect(memory_a, memory_b, type='child')

        connections = self.mbank.get_connections(memory_a)
        assert_equal(connections[0], (memory_b, 'child'))

    def test_connect_memories_twice(self):
        memory_a = self.mbank.create_memory('First memory')
        memory_b = self.mbank.create_memory('Second memory')

        self.mbank.connect(memory_a, memory_b, type='child')
        self.mbank.connect(memory_a, memory_b, type='related')

        connections = self.mbank.get_connections(memory_a)
        assert_equal(len(connections), 2)
        assert((memory_b, 'child') in connections)
        assert((memory_b, 'related') in connections)
