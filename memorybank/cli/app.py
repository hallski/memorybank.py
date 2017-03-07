# Copyright (C) 2017 Mikael Hallendal <hallski@hallski.org>

import urwid
import asyncio
import string

from memorybank.fake_data import *
from memorybank.cli.memory_view import MemoryView
from memorybank.cli.memory_view_controller import MemoryViewController


palette = [
    ('title', 'light blue', 'black'),
    ('header', 'dark gray', 'black'),
    ('active_memory', 'yellow', 'black'),
    ('active_note', 'white', 'black'),
    ('selected_menu_item', 'white', 'dark green'),
    ('title_box', 'dark gray', 'black'),
    ('footer', 'white', 'dark blue'),
    ('command_input', 'yellow', 'dark magenta'),
    ('background', 'dark green', 'black')]


class App(object):
    def __init__(self):
        memorybank = create_fake_memory_bank()
        self._view_controller = MemoryViewController(MemoryView(), memorybank)

    def exit_on_q(self, key):
        if key.lower() in string.ascii_lowercase:
            self._view_controller.enable_input(key)
        #if event in ('q', 'Q'):
        #    raise urwid.ExitMainLoop()

    def run(self):
        event_loop = urwid.AsyncioEventLoop(loop=asyncio.get_event_loop())
        main_loop = urwid.MainLoop(self._view_controller.view, palette,
                                   event_loop=event_loop,
                                   unhandled_input=self.exit_on_q)
        main_loop.run()


def main():
    app = App()
    app.run()

if __name__ == '__main__':
    main()
