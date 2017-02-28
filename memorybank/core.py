# Copyright (C) 2017 Mikael Hallendal <hallski@hallski.org>


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
