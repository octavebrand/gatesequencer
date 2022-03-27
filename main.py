#from Tkinter import *
import keyboard
import time
from class_tracks import step
from stepper import count
from stepper import playStep

stepA1 = step(1,0,127,15,0,0)
stepA2 = step(1,0,127,15,0,0)
stepA3 = step(1,0,127,15,0,0)
stepA4 = step(1,0,127,15,0,1)
stepB1 = step(2,0,127,15,0,0)
stepB2 = step(2,0,127,15,0,0)
stepB3 = step(2,0,127,15,0,0)
stepB4 = step(2,0,127,15,0,1)

stepMatrix = [[stepA1, stepA2, stepA3, stepA4],
			  [stepB1, stepB2, stepB3, stepB4]]


#des trucs pourris
print(stepA1.prob)
print(stepMatrix[0][3].rst)
print(stepMatrix[1][1].gateOn)
stepMatrix[1][1].gateOn = 1
print(stepMatrix[1][1].gateOn)
stepB2.gateOn = 0
print(stepMatrix[1][1].gateOn)

#un truc qui marche pas très bien
count()



