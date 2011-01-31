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
