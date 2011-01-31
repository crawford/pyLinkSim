from simulator import Simulator
import pygame

WINDOW_SIZE = (80,80)
BACK_COLOR = (200,200,200)

class Window(object):
	simulator = None
	canvas = None

	def __init__(self, simulator):
		self.simulator = simulator
		simulator.register_step_callback(self.draw_model)

		pygame.init()
		self.canvas = pygame.display.set_mode(WINDOW_SIZE)
		self.canvas.fill(BACK_COLOR)


	def draw_model(self):
		for segment in self.simulator.segments:
			pygame.draw.aaline(self.canvas, segment.get_color(),
			                   segment.connA.coords, segment.connB.coords)

		for connection in self.simulator.connections:
			pygame.draw.circle(self.canvas, connection.color, connection.coords,
			                   connection.radius)

		pygame.display.flip()
