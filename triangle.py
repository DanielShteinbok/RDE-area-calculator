#!/usr/bin/env python
import math

def area_triangle(a, b, c):
    """
    calculate area of triangle with sides a, b, c via Heron's formula
    """
    s = (a + b + c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

def area_polygon(l1, *triangle_components):
    """
    calculate area of polygon by breaking it up into triangles.
    Starting from a point A, go out a distance of l1 to point B.
    From point B, for n steps for (n-2)-sided polygon, give a 2-tuple of
    length from previous point to next point, and the diagonal from there to A.

    for a quadrilateral with points A, B, C, D where XY denotes the length from X to Y for some points X and Y,
    call this function as:
    area_polygon(AB, (BC, CA), (CD, DA))
    """
    counted_area = 0
    last_side = l1

    for pair in triangle_components:
        counted_area += area_triangle(last_side, item[0], item[1])

    return counted_area
