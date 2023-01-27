import pybullet as p
import pybullet_data
import time
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
#list for use in for loop
list = range(1000)
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("box.sdf")
for n in list:
    p.stepSimulation()
    time.sleep(1/60)
    print(n)
p.disconnect()