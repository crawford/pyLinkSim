from simulator import Simulator
import pygame

class Window(object):
	WINDOW_SIZE = (200,200)
	BACK_COLOR = (200,200,200)

	simulator = None
	canvas = None

	def __init__(self, simulator):
		self.simulator = simulator
		simulator.register_step_callback(self.draw_model)

		pygame.init()
		self.canvas = pygame.display.set_mode(self.WINDOW_SIZE)


	def draw_model(self):
		self.canvas.fill(self.BACK_COLOR)

		for segment in self.simulator.segments:
			pygame.draw.aaline(self.canvas, segment.get_color(),
			                   segment.connA.coords, segment.connB.coords)

		for connection in self.simulator.connections:
			pygame.draw.circle(self.canvas, connection.color, connection.coords,
			                   connection.radius)

		pygame.display.flip()
