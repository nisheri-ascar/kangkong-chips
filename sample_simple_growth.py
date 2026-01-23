# basic geometric grow, just for self testing purposes

from openalea.plantgl.all import *
import time

length = 1.0
stem = Cylinder(radius=0.1, height=length)
shape = Shape(stem, Material(Color3(0, 200, 0))) # Green
windowFinishedLoading = False
scene = Scene([shape])
Viewer.display(scene)

while(True):
    length += 0.5
    if(windowFinishedLoading == False):
        #time.sleep(20)
        windowFinishedLoading = True

