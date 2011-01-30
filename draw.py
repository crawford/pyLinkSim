import pygame

LINK_COLOR =   (255,255,255)
JOINT_COLOR =  (255,100,100)
ANCHOR_COLOR = (100,100,100)
JOINT_RADIUS = 2
BACK_COLOR =   (200,200,200)
WINDOW_SIZE =  (80,80)

def init():
	pygame.init()

def draw(window, joints, links):
	for ((pos1,an1),(pos2,an2)) in links:
		pygame.draw.aaline(window, LINK_COLOR, pos1, pos2)

	for (pos,anchor) in joints:
		if anchor:
			pygame.draw.circle(window, JOINT_COLOR, pos, JOINT_RADIUS)
		else:
			pygame.draw.circle(window, ANCHOR_COLOR, pos, JOINT_RADIUS)

	pygame.display.flip()

init()

window = pygame.display.set_mode(WINDOW_SIZE)
window.fill(BACK_COLOR)


a = ((10,50),True)
b = ((40,50),False)
c = ((70,50),True)
d = ((25,30),False)
e = ((55,30),False)

joints = [a, b, c, d, e]
links = [(a,d), (b,d), (a,b), (b,e), (c,e), (b,c), (d,e)]

draw(window, joints, links)

while True:
	event = pygame.event.wait()
	if event.type == pygame.QUIT:
		exit(0)
	else:
		print event
