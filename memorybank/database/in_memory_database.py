# Copyright (C) 2017 Mikael Hallendal <hallski@hallski.org>

import copy
import uuid


class NonPersistentMemoryStore(object):
    def __init__(self):
        self.memories = []

    def insert(self, memory):
        memory.db_id = uuid.uuid4()
        self.memories.append(memory)

    def save(self, memory):
        if not memory.db_id:
            raise Exception('Memory not stored in database')

        # Don't need to do anything in the non-persistent database

    def remove(self, memory):
        if not memory.db_id:
            raise Exception('Memory not stored in database')

        self.memories.remove(memory)

    def find_by_title(self, title):
        for memory in self.memories:
            if memory.title == title:
                return memory

        return None


class NonPersistentLinkStore(object):
    def __init__(self):
        self._links = []

    def insert(self, link):
        link.db_id = uuid.uuid4()
        self._links.append(link)

    def remove(self, link):
        self._links.remove(link)

    def remove_links(self, links):
        for link in links:
            self.remove(link)

    def save(self, link):
        # Do nothing
        pass

    def find(self, memory):
        return [link for link in self._links
                if link.memory_a == memory or link.memory_b == memory]
