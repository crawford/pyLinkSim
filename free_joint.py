from connection import Connection

class FreeJoint(Connection):

	def __init__(self, coords):
		Connection.__init__(self, coords)
		self.color = (100,100,255)
