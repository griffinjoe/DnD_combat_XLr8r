from .char import *
from .npc import *

class Room(object):
	def __init__(self, *occupants):
		# To call with a list of occupants named "party", use something like:
		# r = Room(*(party + 5*[NPC('NPC ' + str(i)) for i in range(2)]))
		self.occupants = occupants

	def turn(self):
		inits = {elt:[] for elt in np.arange(1, 19)}
		occupants = list(self.occupants)
		np.random.shuffle(occupants)
		# Give everyone an initiative value
		for occupant in occupants:
			init = np.random.randint(1, 11) + min(occupant.get_init_mod(), 8)
			inits[init].append(occupant)
		# Iterate through initiative values, not occupants
		# Use "inits" dictionary to map who goes when
		for init in np.arange(18, 0, -1):
			# 18 goes first, 1 goes last
			if (len(inits[init]) != 0):
				print('Initiative State: ' + str(init))
				for actor in inits[init]:
					name = actor.get_name() + "'s turn:"
					col_string = actor.pretty_print(actor.hit_reqs())
					print(name + '\n' + col_string)
					# Wait until the operator hits enter to continue
					input('')
