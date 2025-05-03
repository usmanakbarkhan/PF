
from math import pi,sqrt

def sphere_volume(r):
    sphere_volumes = (4 / 3) * pi * (r ** 3)
    print("sphere_volume : ",sphere_volumes)
    return
def sphere_surface(r):
    sphere_surfaces = 4 * pi * (r ** 2)
    print("sphere_surfaces : ",sphere_surfaces)
    return

def cylinder_volume(r,h):
    cylinder_volumes = pi * (r ** 2) * h
    print("cylinder_volumes : ", cylinder_volumes)
    return

def cylinder_surface(r,h):
    cylinder_surfaces = (2 * pi * r * h) + (2 * pi * (r ** 2))
    print("cylinder_surfaces : ",cylinder_surfaces)
    return

def cone_volume(r,h):
    cone_volumes = pi * (r ** 2) * (h / 3)
    print("cone_volumes : ", cone_volumes)
    return

def cone_surface(r,h):
    cone_surfaces = pi * r * (r + sqrt((h ** 2) + (r ** 2)))
    print("cone_surfaces : ", cone_surfaces)
    return

r=float(input("enter a value of r : "))
h=float(input("enter a value of h : "))
a = sphere_surface(r)
b = sphere_volume(r)
c = cylinder_volume(r,h)
d = cylinder_surface(r,h)
e = cone_volume(r,h)
f = cone_surface(r,h)
