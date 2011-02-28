from connection import Connection

class Anchor(Connection):

	def __init__(self, coords):
		Connection.__init__(self, coords)
		self.color = (255,100,100)
	
	def eval_step(self):
		pass
