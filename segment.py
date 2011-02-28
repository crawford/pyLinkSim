from connection import Connection
from math import pow, sqrt

class Segment(object):
	MAX_STRETCH = 1.5
	MIN_STRETCH = 0.75
	FORCE_FACTOR = 10

	connA = None
	connB = None
	init_length = None

	def __init__(self, connA, connB):
		print 'creating segment'

		self.connA = connA
		self.connB = connB

		self.init_length = self.get_length()

		connA.add_link(self)
		connB.add_link(self)

	def get_color(self):
		force = self.get_force()

		if force == None:
			return (255,255,0)
		
		#This is a mess
		if force < 0:
			return (100,100,100 + 
			  (int)(155 / (1 - self.MIN_STRETCH) / self.FORCE_FACTOR * -force))
		else:
			return (
			  (int)(155 / (self.MAX_STRETCH - 1) / self.FORCE_FACTOR * force) +
			  100,100,100)

	def get_force(self):
		stretch = self.get_length()/self.init_length;

		if stretch > self.MAX_STRETCH:
			return None

		if stretch < self.MIN_STRETCH:
			return None

		#Convert this from centered around 1 to centered around 0
		stretch = stretch - 1

		return stretch*self.FORCE_FACTOR

	def get_length(self):
		return sqrt(pow(self.connA.coords[0] - self.connB.coords[0], 2) +
		            pow(self.connA.coords[1] - self.connB.coords[1], 2))
