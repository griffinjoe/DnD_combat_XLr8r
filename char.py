import numpy as np

class Character(object):
	# The object for referencing all useful information about a character
	def __init__(self, name, lvl, abilities, align, race, play_class):
		self.name = name
		self.race = race
		self.lvl = lvl
		self.play_class = play_class
		self.abilities = abilities
		self.align = align

	def hit_reqs(self):# Calculate the to-hit roll values
		# Automatically add to-hit effects for this character
		# Exclude adjustments based on chosen weapon
		# For this function to work, player level must be at least 1
		table = self.play_class.get_table()
		reqs = table[min(self.lvl - 1, 20)]
		return reqs

	def get_init_mod(self):
		dex = self.abilities.get_dex()
		if (dex > 15):
			return dex - 15
		return 0

	def pretty_print(self, hits):
		# First build the opening line
		title_str = '"To-hit":'
		# Next build the list of armor classes
		# It's just an evenly spaced string of integers [-10, 10]
		acs = np.arange(-10, 11)
		ac_entries = [((' ' * (3 - len(str(ac)))) + str(ac)) for ac in acs]
		ac_line = ' '.join(ac_entries)
		# Add a horizontal line for easy readability
		sep_line = '-' * len(ac_line)
		# Build the roll requirements line
		rolls = [((' ' * (3 - len(str(to)))) + str(to)) for to in hits]
		roll_line = ' '.join(rolls)
		return '\n'.join((title_str, ac_line, sep_line, roll_line))

	def mod_strings(self):
		# First list the "to-hit" mods
		hit_mods = []
		strgth = self.abilities.get_str()
		if (strgth > 16):
			hit_mods.append('To-hit Mods: +' + str(strgth - 16))
		hit_string = '  '.join(hit_mods)
		# Second, list the damage mods
		dmg_mods = []
		if (strgth > 15):
			dmg_mods.append('Damage: +' + str(strgth - 15))
		dmg_string = '  '.join(dmg_mods)
		return (hit_string, dmg_string)

	def get_name(self):
		return self.name

class Abilities(object):
	# This is just a list of the ability values.
	# Most of them won't even be used for the basic version
	def __init__(self, strgth, intel, wis, dex, const, cha):
		self.strgth = strgth
		self.intel = intel
		self.wis = wis
		self.dex = dex
		self.const = const
		self.cha = cha

	def __str__(self):
		return str(self.__dict__)

	def get_str(self):
		return self.strgth

	def get_int(self):
		return self.intel

	def get_wis(self):
		return self.wis

	def get_dex(self):
		return self.dex

	def get_con(self):
		return self.const

	def get_cha(self):
		return self.cha

	def set_str(self, strgth):
		self.strgth = strgth

	def set_int(self, intel):
		self.intel = intel

	def set_wis(self, wis):
		self.wis = wis

	def set_dex(self, dex):
		self.dex = dex

	def set_con(self, const):
		self.const = const

	def set_cha(self, cha):
		self.cha = cha

class PlayerClass(object):
	# Generic character class, to be used as a base for other classes
	def __init__(self):
		self.classname = 'Generic'
		# Hit tables available on DM Guide p74
		self.hit_table = np.zeros((21, 21))

	def __str__(self):
		return self.classname + ':\n' + str(self.hit_table.T)

	def get_table(self):
		return self.hit_table

fighter_table = np.array(
	2*[[25,24,23,22,21,20,20,20,20,20,20,19,18,17,16,15,14,13,12,11,10]] +
	2*[[23,22,21,20,20,20,20,20,20,19,18,17,16,15,14,13,12,11,10, 9, 8]] +
	2*[[21,20,20,20,20,20,20,19,18,17,16,15,14,13,12,11,10, 9, 8, 7, 6]] +
	2*[[20,20,20,20,20,19,18,17,16,15,14,13,12,11,10, 9, 8, 7, 6, 5, 4]] +
	2*[[20,20,20,19,18,17,16,15,14,13,12,11,10, 9, 8, 7, 6, 5, 4, 3, 2]] +
	2*[[20,19,18,17,16,15,14,13,12,11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]] +
	2*[[18,17,16,15,14,13,12,11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0,-1,-2]] +
	2*[[16,15,14,13,12,11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0,-1,-2,-3,-4]] +
	5*[[14,13,12,11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0,-1,-2,-3,-4,-5,-6]]
)

druid_table = np.array(
	3*[[25,24,23,22,21,20,20,20,20,20,20,19,18,17,16,15,14,13,12,11,10]] +
	3*[[23,22,21,20,20,20,20,20,20,19,18,17,16,15,14,13,12,11,10, 9, 8]] +
	3*[[21,20,20,20,20,20,20,19,18,17,16,15,14,13,12,11,10, 9, 8, 7, 6]] +
	3*[[20,20,20,20,20,19,18,17,16,15,14,13,12,11,10, 9, 8, 7, 6, 5, 4]] +
	3*[[20,20,20,19,18,17,16,15,14,13,12,11,10, 9, 8, 7, 6, 5, 4, 3, 2]] +
	3*[[20,19,18,17,16,15,14,13,12,11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]] +
	3*[[19,18,17,16,15,14,13,12,11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0,-1]]
)

thief_table = np.array(
	4*[[26,25,24,23,22,21,20,20,20,20,20,20,19,18,17,16,15,14,13,12,11]] +
	4*[[24,23,22,21,20,20,20,20,20,20,19,18,17,16,15,14,13,12,11,10, 9]] +
	4*[[21,20,20,20,20,20,20,19,18,17,16,15,14,13,12,11,10, 9, 8, 7, 6]] +
	4*[[20,20,20,20,20,19,18,17,16,15,14,13,12,11,10, 9, 8, 7, 6, 5, 4]] +
	4*[[20,20,20,19,18,17,16,15,14,13,12,11,10, 9, 8, 7, 6, 5, 4, 3, 2]] +
	1*[[20,19,18,17,16,15,14,13,12,11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]]
)

magician_table = np.array(
	5*[[26,25,24,23,22,21,20,20,20,20,20,20,19,18,17,16,15,14,13,12,11]] +
	5*[[24,23,22,21,20,20,20,20,20,20,19,18,17,16,15,14,13,12,11,10, 9]] +
	5*[[21,20,20,20,20,20,20,19,18,17,16,15,14,13,12,11,10, 9, 8, 7, 6]] +
	5*[[20,20,20,20,19,18,17,16,15,14,13,12,11,10, 9, 8, 7, 6, 5, 4, 3]] +
	1*[[20,20,19,18,17,16,15,14,13,12,11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1]]
)

# Define all the individual character classes
class Magician(PlayerClass):
	def __init__(self, classname = 'Magician'):
		self.classname = classname
		self.hit_table = magician_table

class Illusionist(Magician):
	def __init__(self):
		Magician.__init__(self, 'Illusionist')

class Thief(PlayerClass):
	def __init__(self, classname = 'Thief'):
		self.classname = classname
		self.hit_table = thief_table

class Assassin(Thief):
	def __init__(self):
		Thief.__init__(self, 'Assassin')

class Druid(PlayerClass):
	def __init__(self, classname = 'Druid'):
		self.classname = classname
		self.hit_table = druid_table

class Cleric(Druid):
	def __init__(self):
		Druid.__init__(self, 'Cleric')

class Monk(Druid):
	def __init__(self):
		Druid.__init__(self, 'Monk')

class Fighter(PlayerClass):
	def __init__(self, classname = 'Fighter'):
		self.classname = classname
		self.hit_table = fighter_table

class Ranger(Fighter):
	def __init__(self):
		Fighter.__init__(self, 'Ranger')

class Paladin(Fighter):
	def __init__(self):
		Fighter.__init__(self, 'Paladin')

class Barbarian(Fighter):
	def __init__(self):
		Fighter.__init__(self, 'Barbarian')
