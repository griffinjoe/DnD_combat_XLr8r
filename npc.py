import numpy as np

class NPC(object):
	def __init__(self, name = 'NPC'):
		self.name = name

	def hit_reqs(self):
		return np.zeros((21,))

	def get_init_mod(self):
		return 0

	def pretty_print(self, hit_reqs):
		return ''

	def mod_strings(self):
		return ('', '')

	def get_name(self):
		return self.name

	def take_turn(self):
		return self.name + "'s turn!\n"
