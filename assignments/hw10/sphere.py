"""
Name: Brett Widholm
sphere.py

Problem: This program makes a sphere class

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


from math import pi

class Sphere:
    """
    Constructs a sphere once called in main file
    """

    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def surface_area(self):
        sphere_sa = (4 * pi * (self.radius ** 2))
        return sphere_sa

    def volume(self):
        sphere_vol = ((4/3) * pi * (self.radius ** 3))
        return sphere_vol
