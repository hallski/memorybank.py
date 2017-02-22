import sys

from memorybank.memory import *

def main(args=None):
    """The main routin."""
    if args is None:
        args = sys.argv[1:]

    memory = Memory('A Memory')
    print('MemoryBank: %s' % memory.title)


if __name__ == '__main__':
    main()
