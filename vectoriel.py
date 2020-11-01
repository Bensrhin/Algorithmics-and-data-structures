#!/usr/bin/env python3

from math import sqrt
from timeit import timeit
from sys import argv

from geo.point import Point
from geo.tycat import tycat
from geo.segment import Segment

def main():

    a = Point([0.7, 0.79])
    b = Point([0.84, 0.62])
    c = Point([b.x, a.y])
    # tycat(points)
    d = a.cross_product(b, c)
    ab = a.distance_to(b)
    ac = a.distance_to(c)
    print(d)
    print(ab*ac)
    print(d / (ab*ac))
    # P = Point([SortedX[i + 1].x, SortedX[i].y])
    # vect = SortedX[i].cross_product(SortedX[i + 1], P)
    # Pto1 = SortedX[i].distance_to(P)
    # Pto2 = SortedX[i + 1].distance_to(P)
    # to12 = SortedX[i].distance_to(SortedX[i + 1])
    # d_y = d * vect / (Pto1 * Pto2)
    # d_x = sqrt(d**2 - d_y**2)
main()
