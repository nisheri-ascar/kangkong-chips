print("fuck my life")
from openalea.plantgl.all import *

scene = Scene()

def bottle_pot():
    global scene

    # -------------------------
    # Physical Attributes
    # -------------------------
    height = 2
    num_slices = 4
    radius = 3
    groove_depth = 0.1

    # -------------------------
    # Curve / groove control
    # -------------------------
    slice_h = height / num_slices
    transition_ratio = 0.3   # how “sloped” the grooves should be
    transition_h = slice_h * transition_ratio
    body_h = slice_h - transition_h

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
    # Geometry construction
    # -------------------------
    for i in range(num_slices):
        r0 = radius - (groove_depth if i % 2 else 0)
        z = i * slice_h
        is_last = (i == num_slices - 1)

        # Only compute r1 if next slice exists
        if not is_last:
            r1 = radius - (groove_depth if (i + 1) % 2 else 0)

        # --- main cylinder ---
        cyl_h = body_h if not is_last else slice_h  # last slice = flat top
        slice_cyl = Translated(0, 0, z, Cylinder(r0, cyl_h, 0))
        scene += Shape(slice_cyl, material)

        # --- frustum slope for grooves ---
        if not is_last:
            slope = Translated(0, 0, z + body_h, Frustum(r0, r1, transition_h, 0))
            scene += Shape(slope, material)

    # -------------------------
    # Bottom cap for flower pot
    # -------------------------
    scene += Shape(Cylinder(radius, 0.001, 1), material)

bottle_pot()
Viewer.display(scene)

