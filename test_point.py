#!/usr/bin/env python3.6

from geo.point import Point

def main():
    p = Point([1, 4])
    # d = p.copy()
    # print(p)
    # print(d)
    # print(p.distance_to(Point([3,4])))
    print(p.__add__(Point([2, 4])))

main()
