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

    def get_relative_link_for_memory(self, memory):
        '''Creates a tuple with the memory and link type from
           the memories perspective.'''
        if memory == self._memory_a:
            return (self._memory_b, self._link_type)
        elif memory == self._memory_b:
            if self._link_type == 'child':
                return (self._memory_a, 'parent')
            elif self._link_type == 'related':
                return (self._memory_a, 'related')
        else:
            raise Exception('Memory {0} is not part of this link'.format(memory))
