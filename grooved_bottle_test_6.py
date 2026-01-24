print("Water bottle flower pot with grooved bottom!")
from openalea.plantgl.all import *

scene = Scene()

def flower_pot():
    global scene

    # -------------------------
    # Physical Attributes
    # -------------------------
    height = 2
    radius = 3
    num_ribs = 4            # number of vertical ribs (grooves)
    groove_depth = 0.1       # depth of vertical grooves
    bottom_depth = 0.2       # depth of the concave bottle bottom

    # -------------------------
    # Visual Attributes
    # -------------------------
    ambient = Color3(0, 0, 255)
    diffuse = 1.0
    specular = Color3(0, 0, 0)
    emmision = Color3(0, 0, 0)
    shininess = 0.2
    transparency = 0.1

    material = Material(
        ambient, diffuse, specular,
        emmision, shininess, transparency
    )

    # -------------------------
    # Build 2D profile for revolution
    # -------------------------
    profile_points = []

    # First, define the bottle bottom (concave with grooves)
    # We'll create a simple groove pattern at the base
    bottom_steps = 5
    for i in range(bottom_steps + 1):
        z = i * (bottom_depth / bottom_steps)
        # Alternate radius inward to simulate the grooves
        r = radius - (groove_depth if i % 2 else 0)
        profile_points.append((z, r))

    # Then add vertical walls
    wall_steps = num_ribs
    wall_height = height - bottom_depth
    for i in range(wall_steps + 1):
        z = bottom_depth + i * (wall_height / wall_steps)
        r = radius - (groove_depth if i % 2 else 0)
        profile_points.append((z, r))

    # Ensure top is flat
    profile_points[-1] = (height, profile_points[-1][1])

    # Convert to Vector2 (radius, z) for Polyline2D
    polyline2d = Polyline2D([Vector2(r, z) for z, r in profile_points])

    # -------------------------
    # Revolve to make 3D pot
    # -------------------------
    revolved = Revolution(polyline2d)

    scene += Shape(revolved, material)

    # -------------------------
    # Bottom cap (optional)
    # -------------------------
    scene += Shape(Cylinder(radius, 0.001, 1), material)

flower_pot()
Viewer.display(scene)

