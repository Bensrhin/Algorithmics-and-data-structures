#!/usr/bin/env python3.6

from geo.segment import Segment
from geo.point import Point

def main():
    point1 = Point([1,1])
    point2 = Point([1,5])
    s = Segment([point1, point2])
    # print(s)
    # print(s.endpoints)
    # c = s.copy()
    # print(c)
    # print(c.endpoints)
    # q = s.bounding_quadrant()
    # print(q)
    # print(q.min_coordinates, q.max_coordinates)
    # print(s.svg_content())
    # point = Point([1,2])
    # print(s.endpoints[0])
    # print(s.endpoints[1])
    # print(s.endpoint_not(point1))
    # print(s.endpoint_not(point2))
    # print(s.contains(Point([2, 4.5])))
    a = s.__repr__()
    print(a)


main()
