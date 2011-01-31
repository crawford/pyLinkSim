from anchor import Anchor
from free_joint import FreeJoint
from segment import Segment

class Simulator(object):
	connections = None
	segments = None
	stepCbs = None

	def __init__(self):
		self.connections = []
		self.segments = []
		self.stepCbs = []

	def create_segment(self, connA, connB):
		self.connections.append(connA)
		self.connections.append(connB)

		self.segments.append(Segment(connA, connB))

	def register_step_callback(self, callback):
		self.stepCbs.append(callback)

	def run_step_callbacks(self):
		for cb in self.stepCbs:
			cb()

	def step(self):
		self.run_step_callbacks()
