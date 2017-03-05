# Copyright (C) 2017 Mikael Hallendal <hallski@hallski.org>

import urwid
import asyncio

from memorybank.fake_data import *
from memorybank.cli.main_view import MainView
from memorybank.cli.main_view_controller import MainViewController
from memorybank.cli.main_view_presenter import MainViewPresenter


palette = [
    ('title', 'light blue', 'black'),
    ('header', 'dark gray', 'black'),
    ('active_memory', 'yellow', 'black'),
    ('active_note', 'white', 'black'),
    ('selected_menu_item', 'white', 'dark green'),
    ('title_box', 'dark gray', 'black'),
    ('footer', 'white', 'dark blue'),
    ('background', 'dark green', 'black')]


def exit_on_q(event):
    if event in ('q', 'Q'):
        raise urwid.ExitMainLoop()


def main():
    memorybank = create_fake_memory_bank()
    view_controller = MainViewController(memorybank)
    view = MainView(view_controller)
    view_presenter = MainViewPresenter(view, memorybank)
    view_controller.presenter = view_presenter

    event_loop = urwid.AsyncioEventLoop(loop=asyncio.get_event_loop())
    main_loop = urwid.MainLoop(view, palette,
                               event_loop=event_loop,
                               unhandled_input=exit_on_q)
    main_loop.run()


if __name__ == '__main__':
    main()
