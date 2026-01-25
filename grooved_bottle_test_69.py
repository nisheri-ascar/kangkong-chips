print("Cylinders + Curved Polyline slopes with tweakable circle slices!")
from openalea.plantgl.all import *
import math

scene = Scene()

def bottle():
    global scene 

    # -------------------------
    # Tweakable parameters
    # -------------------------
    height = 2
    num_slices = 10
    radius = 3
    groove_depth = 0.2
    circle_slices = 64        # number of segments for circular appearance
    transition_ratio = 0.3    # how tall the downslope is
    num_pts_slope = 10        # smoothness of the curve

    # -------------------------
    # Visual Attributes
    # -------------------------
    ambient = Color3(0,0,255)
    diffuse = 1.0
    specular = Color3(0,0,0)
    emmision = Color3(0,0,0)
    shininess = 0.2
    transparency = 0.1

    material = Material(ambient, diffuse, specular, emmision, shininess, transparency)

    # -------------------------
    # Slice + slope parameters
    # -------------------------
    slice_h = height / num_slices
    transition_h = slice_h * transition_ratio
    body_h = slice_h - transition_h

    # -------------------------
    # Build cylinder slices with curved downslope
    # -------------------------
    for i in range(num_slices):
        r0 = radius - (groove_depth if i % 2 else 0)
        r1 = radius - (groove_depth if (i + 1) % 2 else 0)
        z = i * slice_h
        is_last = (i == num_slices - 1)

        print(f"iteration: {i}, r0={r0}, r1={r1}, z={z}")

        # --- main cylinder ---
        cyl_h = slice_h
        slice_cyl = Translated(
            0, 0, z,
            Cylinder(r0, cyl_h, 0, circle_slices)  # use circle_slices here
        )
        scene += Shape(slice_cyl, material)

        # --- curved polyline slope for groove ---
        if not is_last and r0 != r1:
            pts = []
            for j in range(num_pts_slope + 1):
                t = j / num_pts_slope
                # cosine easing for smooth slope
                eased_t = (1 - math.cos(math.pi * t)) / 2
                radius_at_t = r0 + eased_t * (r1 - r0)
                height_at_t = z + body_h + eased_t * transition_h
                pts.append(Vector2(radius_at_t, height_at_t))
            slope_polyline = Polyline2D(pts)
            slope_revolved = Revolution(slope_polyline, slices=circle_slices)  # use circle_slices
            scene += Shape(slope_revolved, material)

    # -------------------------
    # Bottom cap
    # -------------------------
    scene += Shape(Cylinder(radius, 0.001, 1, circle_slices), material)

bottle()
Viewer.display(scene)

