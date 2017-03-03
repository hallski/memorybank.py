# Copyright (C) 2017 Mikael Hallendal <hallski@hallski.org>

class Link(object):
    def __init__(self, memory_a, memory_b, link_type):
        self._memory_a = memory_a
        self._memory_b = memory_b
        self._link_type = link_type

    @property
    def memory_a(self):
        return self._memory_a

    @property
    def memory_b(self):
        return self._memory_b

    @property
    def link_type(self):
        return self._link_type
