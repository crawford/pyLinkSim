from math import atan2, sin, cos, pi

class Connection(object):
	coords = None
	links = None
	color = None
	radius = None

	def __init__(self, coords):
		self.coords = coords
		self.links = []
		self.color = (100,100,100)
		self.radius = 2

	def add_link(self, link):
		self.links.append(link)

	def get_link_angle(self, link):
		if (self == link.connA):
			otherCoords = link.connB.coords
		else:
			otherCoords = link.connA.coords

		dx = otherCoords[0] - self.coords[0]
		dy = self.coords[1] - otherCoords[1]

		return atan2(dy, dx)

	def get_forces(self):
		totalXForce = 0
		totalYForce = 0

		#Sum the forces from each of the connecting links
		for link in self.links:
			force = link.get_force()
			if (force == None):
				continue


			angle = self.get_link_angle(link)
			print "Angle:", angle

			totalXForce += force * cos(angle)
			print "ForceX:", force * cos(angle)

			totalYForce -= force * sin(angle)
			print "ForceY:", force * sin(angle)

		totalYForce += 0.5

		print totalXForce, totalYForce

		return (totalXForce, totalYForce)
