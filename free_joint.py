from connection import Connection

class FreeJoint(Connection):

	def __init__(self, coords):
		Connection.__init__(self, coords)
		self.color = (100,100,255)

	def eval_step(self):
		fx,fy = self.get_forces()
		self.coords = (self.coords[0] + fx, self.coords[1] + fy)
