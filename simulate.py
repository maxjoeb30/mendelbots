import pybullet as p
import time
physicsClient = p.connect(p.GUI)
#list for use in for loop
list = range(1000)
for n in list:
    p.stepSimulation()
    time.sleep(1/60)
    print(n)
p.disconnect()