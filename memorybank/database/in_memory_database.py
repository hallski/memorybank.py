# Copyright (C) 2017 Mikael Hallendal <hallski@hallski.org>

class InMemoryDatabase(object):
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
