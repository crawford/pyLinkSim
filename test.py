from simulator import Simulator
from window import Window
from anchor import Anchor
from free_joint import FreeJoint

sim = Simulator()
win = Window(sim)

cA = Anchor((70,110))
cB = FreeJoint((100,110))
cC = Anchor((130,110))
cD = FreeJoint((85,90))
cE = FreeJoint((115,90))

sim.create_segment(cA, cB)
sim.create_segment(cA, cD)
sim.create_segment(cB, cD)
sim.create_segment(cB, cC)
sim.create_segment(cB, cE)
sim.create_segment(cC, cE)
sim.create_segment(cD, cE)

raw_input("Created. Press key")

while True:
	sim.step()

	if raw_input("Stepped. Presss key") == 'q':
		break

