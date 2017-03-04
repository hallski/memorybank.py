# Copyright (C) 2017 Mikael Hallendal <hallski@hallski.org>

from memorybank.cli.main_view import MainView
from memorybank.cli.main_view_presenter import MainViewPresenter


class MainViewController(object):
    def __init__(self, memorybank):
        # Handler for all events from the MainView
        # Sets the MainViewModel on the MainView when required
        # Sends commands to the core
        self._view_presenter = None

    @property
    def view_presenter(self):
        return self._view_presenter

    @view_presenter.setter
    def view_presenter(self, view_presenter):
        self._view_presenter = view_presenter

    def memory_selected(self, identifier):
        '''Action called from the view when a memory link is activated'''
        print('Open memory {0}'.format(identifier))
