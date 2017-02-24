# Copyright (C) 2017 Mikael Hallendal <hallski@hallski.org>

import urwid


def main():
    txt = urwid.Text('Hello world')
    fill = urwid.Filler(txt, 'top')
    loop = urwid.MainLoop(fill)
    loop.run()

    print('hello world')


if __name__ == '__main__':
    main()
