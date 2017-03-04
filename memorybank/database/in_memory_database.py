# Copyright (C) 2017 Mikael Hallendal <hallski@hallski.org>

import copy
import uuid


class NonPersistentMemoryRepository(object):
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
        m = next(m for m in self.memories if m.title == title)
        if m:
            copy.deepcopy(m)
        return m

class NonPersistentLinkRepository(object):
    def __init__(self):
        self._links = []

    def insert(link):
        pass

    def remove(link):
        pass

    def save(self, link):
        self._links.append(link)

    def find(self, memory):
        return (c for c in self._links
                if c.memory_a == memory or c.memory_b == memory)
