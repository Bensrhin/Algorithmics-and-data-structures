#!/usr/bin/env python

from geo.quadrant import Quadrant
from geo.point import Point

def main():
    q = Quadrant((50,50), (100,100))
    c = q.empty_quadrant(2)
    print(c.max_coordinates, c.min_coordinates)
    # q.add_point(Point([20, 60]))
    # print(q.min_coordinates, q.max_coordinates)
    # q.update(Quadrant((60,60),(180,180)))
    # print(q.min_coordinates, q.max_coordinates)
    # l = q.limits(0)
    # print(l)
    # print(q.get_arrays())
    q.inflate(10)
    print(q.max_coordinates, q.min_coordinates)

main()
