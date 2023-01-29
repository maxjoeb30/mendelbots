import pyrosim.pyrosim as pyrosim
#Define variables to use in the SendCube function.
length = 1
width = 1
height = 1
x = 0
y = 0 
z = 0.50
#Define variables for the second SendCube function.
length2 = 1
width2 = 1
height2 = 1
x2 = 0
y2 = 1 
z2 = 1.50
#Define a variable for adding an incremental height to the z coordinate of the Send_Cube function in order to create a tower of cubes.
addheight = 1
for n in range(10):
    pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size = [length, width, height])
    addheight = addheight + 1



pyrosim.Start_SDF("box.sdf")
pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size = [length, width, height])
pyrosim.Send_Cube(name="Box2", pos=[x2,y2,z2] , size = [length2, width2, height2])

pyrosim.End()