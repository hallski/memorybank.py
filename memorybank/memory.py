# Copyright (C) 2017 Mikael Hallendal <hallski@hallski.org>

class Memory(object):
    def __init__(self, title, note=''):
        self._title = title
        self._note = note
        self.db_id = None

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        self._title = new_title

    @property
    def note(self):
        return self._note

    @note.setter
    def note(self, new_note):
        self._note = new_note

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
