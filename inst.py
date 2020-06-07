from .turn import *

dunkin = Character(
	'Dunkin',
	4,
	Abilities(strgth = 18, intel = 7, wis = 6, dex = 11, const = 15, cha = 8),
	('Neutral', 'Neutral'),
	'Dwarf',
	Barbarian()
)

iorveth = Character(
	'Iorveth',
	5,
	Abilities(strgth = 15, intel = 14, wis = 14, dex = 11, const = 14, cha = 7),
	('Lawful', 'Good'),
	'Half-Elf',
	Ranger()
)

griffin = Character(
	'Griffin',
	5,
	Abilities(strgth = 18, intel = 9, wis = 13, dex = 13, const = 11, cha = 17),
	('Lawful', 'Good'),
	'Human',
	Paladin()
)

redfox = Character(
	'RedFox',
	5,
	Abilities(strgth = 12, intel = 14, wis = 6, dex = 17, const = 8, cha = 10),
	('Lawful', 'Evil'),
	'Human',
	Assassin()
)

#momoa = Character(
#	'Momoa',
#	6,
#	Abilities(strgth = 9, intel = 13, wis = 18, dex = 11, const = 11, cha = 15),
#	('Neutral', 'Neutral'),
#	'Human',
#	Druid()
#)

party = [iorveth, dunkin, redfox, griffin]
