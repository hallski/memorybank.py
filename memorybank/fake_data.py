# Copyright (C) 2017 Mikael Hallendal <hallski@hallski.org>

from memorybank.core import *
from memorybank.database.in_memory_database import *

def create_fake_memory_bank():
    memory_bank = MemoryBank(NonPersistentMemoryStore(), NonPersistentLinkStore())
    m = memory_bank.create_memory('World of Warcraft', note='''\
World of Warcraft (WoW) is a massively multiplayer online  \
role-playing game (MMORPG) released in 2004 by Blizzard Entertainment. It is \
the fourth released game setin the fantasy Warcraft universe, which was first \
introduced by Warcraft: Orcs & Humans in 1994.[3] World of Warcraft takes \
place within the Warcraft world of Azeroth, approximately four years after \
the events at the conclusion of Blizzard's previous Warcraft release, \
Warcraft III: The Frozen Throne.[4] Blizzard Entertainment announced World of \
Warcraft on September 2, 2001.[5] The game was released on November 23, 2004, \
on the 10th anniversary of the Warcraft franchise.
''')

    parents = ['Blizzard Entertainment', 'Roleplaying Games', 'MMORPG', 'Fantasy']
    children = ['Azeroth', 'Illidan', 'Wrath of the Litch King', 'Draenor']
    siblings = ['Diablo', 'Starcraft', 'Warcraft', 'Guild Wars', 'Rift']
    related = ['Warcraft', 'MMO Champion', 'Dark Legacy Comics']

    blizzard = memory_bank.create_memory('Blizzard Entertainment')
    memory_bank.link(blizzard, m, 'parent')
    memory_bank.link(blizzard, memory_bank.create_memory('Diablo'), 'parent')
    memory_bank.link(blizzard, memory_bank.create_memory('StarCraft'), 'parent')
    memory_bank.link(blizzard, memory_bank.create_memory('Warcraft'), 'parent')

    roleplay = memory_bank.create_memory('Roleplaying Games')
    memory_bank.link(roleplay, m, 'parent')
    memory_bank.link(roleplay, memory_bank.create_memory('Guild Wards'), 'parent')

    memory_bank.link(memory_bank.create_memory('Fantasy'), m, 'parent')

    for child in children:
        memory_bank.link(m, memory_bank.create_memory(child), 'parent')

    for r in related:
        memory_bank.link(m, memory_bank.create_memory(r), 'related')

    return memory_bank
