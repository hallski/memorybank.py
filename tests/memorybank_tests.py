from nose.tools import *
from memorybank.memory import Memory


def test_memory():
    memory = Memory('A memory')
    assert_equal(memory.title, 'A memory')

