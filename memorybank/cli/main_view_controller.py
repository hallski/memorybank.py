# Copyright (C) 2017 Mikael Hallendal <hallski@hallski.org>

from memorybank.cli.main_view import MainView
from memorybank.cli.main_view_presenter import MainViewPresenter


class MainViewController(object):
    def __init__(self, memorybank):
        # Handler for all events from the MainView
        # Sets the MainViewModel on the MainView when required
        # Sends commands to the core
        self._memorybank = memorybank
        self._presenter = None

    @property
    def presenter(self):
        return self._presenter

    @presenter.setter
    def presenter(self, presenter):
        self._presenter = presenter

    def memory_selected(self, identifier):
        '''Action called from the view when a memory link is activated'''
        memory = self._memorybank.find_memory_by_id(identifier)
        if memory:
            self.presenter.active_memory = memory
