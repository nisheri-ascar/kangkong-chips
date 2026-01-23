
from openalea.plantgl.all import *


# Viewer.display(Sphere())

scene = Scene()
c = Cylinder(1,10)
color = Material(Color3(255,0,0),Color3(0,0,0),Color3(0,0,0),1,0)
Shape = Shape(c, color)
scene.add(Shape)
Viewer.display(scene)

# screen
Viewer.frameGL.setBgColor(255,255,200)
Viewer.grids.setXYPlane(True)
Viewer.grids.setYZPlane(False)
Viewer.grids.setXZPlane(False)
Viewer.frameGL.saveImage("/home/nisherii/projects/kangkong-chips/image_output/result.png")


