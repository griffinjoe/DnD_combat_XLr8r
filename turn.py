from .char import *
from .npc import *

class Room(object):
	def __init__(self, *occupants):
		# To call with a list of occupants named "party", use something like:
		# r = Room(*(party + [NPC()]))
		self.occupants = list(occupants)

	def turn(self):
		inits = {elt:[] for elt in np.arange(1, 19)}
		# Give everyone an initiative value
		for occ in self.occupants:
			init = np.random.randint(1, 11) + min(occ.get_init_mod(), 8)
			inits[init].append(occ)
		# Iterate through initiative values, not occupants
		# Use "inits" dictionary to map who goes when
		for init in np.arange(18, 0, -1):
			# 18 goes first, 1 goes last
			if (len(inits[init]) != 0):
				print('Initiative State: ' + str(init))
				np.random.shuffle(inits[init])
				for actor in inits[init]:
					print(actor.take_turn())
					# Wait until the operator hits enter to continue
					input('')

def build_room(party, num_NPCs):
	npc_list = num_NPCs * [NPC('NPC ' + str(i)) for i in range(num_NPCs)]
	return Room(*(party + npc_list))
