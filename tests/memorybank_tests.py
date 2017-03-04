# Copyright (C) 2017 Mikael Hallendal <hallski@hallski.org>

from nose.tools import *
from memorybank.core import *
from memorybank.database.in_memory_database import *
import unittest


class MemoryBankTest(unittest.TestCase):
    def setUp(self):
        self.mbank = MemoryBank(NonPersistentMemoryStore(), NonPersistentLinkStore())

    def test_create_memory(self):
        memory = self.mbank.create_memory('Creating a new memory')
        assert_equal(memory.title, 'Creating a new memory')

    def test_find_memory(self):
        memory = self.mbank.create_memory('Memory to find')
        found_memory = self.mbank.find_memory('Memory to find')
        assert_equal(memory, found_memory)

    def test_link_memories(self):
        memory_a = self.mbank.create_memory('Something to remember')
        memory_b = self.mbank.create_memory('Another thing to remember')
        self.mbank.link(memory_a, memory_b, link_type='child')

        links = self.mbank.get_links(memory_a)
        assert_equal(len(links), 1)
        assert_equal(links[0], (memory_b, 'child'))

    def test_link_twice_same_link_type_should_be_ignored(self):
        memory_a = self.mbank.create_memory('Something to remember')
        memory_b = self.mbank.create_memory('Another thing to remember')
        self.mbank.link(memory_a, memory_b, link_type='child')
        self.mbank.link(memory_a, memory_b, link_type='child')

        links = self.mbank.get_links(memory_a)
        assert_equal(len(links), 1)
        assert_equal(links[0], (memory_b, 'child'))

    def test_link_memories_twice(self):
        memory_a = self.mbank.create_memory('First memory')
        memory_b = self.mbank.create_memory('Second memory')

        self.mbank.link(memory_a, memory_b, link_type='child')
        self.mbank.link(memory_a, memory_b, link_type='related')

        links = self.mbank.get_links(memory_a)
        assert_equal(len(links), 2)
        assert((memory_b, 'child') in links)
        assert((memory_b, 'related') in links)

    def test_child_link_creates_a_parent_link_back(self):
        memory_a = self.mbank.create_memory('Parent')
        memory_b = self.mbank.create_memory('Child')

        self.mbank.link(memory_a, memory_b, 'child')

        links = self.mbank.get_links(memory_b)
        assert_equal(len(links), 1)
        assert_equal(links[0], (memory_a, 'parent'))

    def test_related_link_creates_related_link_back(self):
        memory_a = self.mbank.create_memory('A')
        memory_b = self.mbank.create_memory('B')

        self.mbank.link(memory_a, memory_b, 'related')

        links = self.mbank.get_links(memory_b)
        assert_equal(len(links), 1)
        assert_equal(links[0], (memory_a, 'related'))

    def test_remove_memory(self):
        memory = self.mbank.create_memory('Memory to remove')
        self.mbank.remove_memory(memory)

        assert_is_none(self.mbank.find_memory('Memory to remove'))

    def test_removing_memory_removes_links(self):
        memory_a = self.mbank.create_memory('A Memory')
        memory_b = self.mbank.create_memory('B Memory')
        memory_c = self.mbank.create_memory('C Memory')

        self.mbank.link(memory_a, memory_b, 'child')
        self.mbank.link(memory_a, memory_c, 'related')
        self.mbank.link(memory_b, memory_c, 'related')

        self.mbank.remove_memory(memory_a)

        links_b = self.mbank.get_links(memory_b)
        links_c = self.mbank.get_links(memory_c)

        assert_equal(len(links_b), 1)
        assert_equal(len(links_c), 1)
        assert_equal(links_b[0], (memory_c, 'related'))
        assert_equal(links_c[0], (memory_b, 'related'))

    def test_update_memory(self):
         memory = self.mbank.create_memory('A memory')

         memory.title = 'A new title'

         self.mbank.save_memory(memory)

         assert_equal(self.mbank.find_memory('A new title'), memory)
         assert_is_none(self.mbank.find_memory('A memory'))
