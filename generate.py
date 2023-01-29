import pyrosim.pyrosim as pyrosim
#Define variables to use in the SendCube function.
length = 1
width = 1
height = 1
x = 0
y = 0 
z = 0.50
pyrosim.Start_SDF("box.sdf")
#Define a variable for adding an incremental height to the z coordinate of the Send_Cube function in order to create a tower of cubes.
pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size = [length, width, height])
pyrosim.End()