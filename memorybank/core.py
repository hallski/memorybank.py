# Copyright (C) 2017 Mikael Hallendal <hallski@hallski.org>


class MemoryBank(object):
    def __init__(self):
        self._connections = []

    def create_memory(self, title, note=''):
        return Memory(title, note=note)

    def connect(self, memory_a, memory_b, type='child'):
        self._connections.append(Connection(memory_a, memory_b, type))

    def get_connections(self, memory):
        return [(c.memory_b, c.connection_type) for c in self._connections if c.memory_a == memory]

    def find_memory(self, title):
        return Memory('Memory to find')


class Connection(object):
    def __init__(self, memory_a, memory_b, connection_type):
        self._memory_a = memory_a
        self._memory_b = memory_b
        self._connection_type = connection_type

    @property
    def memory_a(self):
        return self._memory_a

    @property
    def memory_b(self):
        return self._memory_b

    @property
    def connection_type(self):
        return self._connection_type


class Memory(object):
    def __init__(self, title, note=''):
        self._title = title
        self._note = note

    @property
    def title(self):
        return self._title

    @property
    def note(self):
        return self._note

    def add_connection(self, other, connection_type):
        pass

    def remove_connection(self, other, connection_type=''):
        pass

    def get_connections(self, connection_type=''):
        pass

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.title == other.title and \
                   self.note == other.note
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented
