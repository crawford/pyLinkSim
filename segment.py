from connection import Connection

class Segment(object):
	connA = None
	connB = None

	def __init__(self, connA, connB):
		self.connA = connA
		self.connB = connB

		connA.add_link(self)
		connB.add_link(self)

	def get_color(self):
		return (255,255,255)
