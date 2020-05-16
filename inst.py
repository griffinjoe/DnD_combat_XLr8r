from .turn import *

dunkin = Character(
	'Dunkin',
	4,
	Abilities(strgth = 17, intel = 8, wis = 12, dex = 15, const = 17, cha = 9),
	('Chaotic', 'Good'),
	'Dwarf',
	Barbarian()
)

iorveth = Character(
	'Iorveth',
	5,
	Abilities(strgth = 15, intel = 14, wis = 14, dex = 11, const = 14, cha = 7),
	('Lawful', 'Good'),
	'Elf',
	Ranger()
)

party = [iorveth, dunkin]

r = Room(*(party + [NPC('Orc ' + str(i)) for i in range(3)]))
