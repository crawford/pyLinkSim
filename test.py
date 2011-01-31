from simulator import Simulator
from window import Window
from anchor import Anchor
from free_joint import FreeJoint

sim = Simulator()
win = Window(sim)

cA = Anchor((10,50))
cB = FreeJoint((40,50))
cC = Anchor((70,50))
cD = FreeJoint((25,30))
cE = FreeJoint((55,30))

sim.create_segment(cA, cB)
sim.create_segment(cA, cD)
sim.create_segment(cB, cD)
sim.create_segment(cB, cC)
sim.create_segment(cB, cE)
sim.create_segment(cC, cE)
sim.create_segment(cD, cE)

raw_input("Created. Press key")

sim.step()

raw_input("Stepped. Presss key")

