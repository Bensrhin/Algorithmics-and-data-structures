#!/usr/bin/env python3
"""
compute sizes of all connected components.
sort and display.
"""

from math import sqrt
from timeit import timeit
from sys import argv
from math import sqrt
from geo.point import Point
from geo.tycat import tycat
from geo.segment import Segment

def load_instance(filename):
    """
    loads .pts file.
    returns distance limit and points.
    """
    with open(filename, "r") as instance_file:
        lines = iter(instance_file)
        distance = float(next(lines))
        points = [Point([float(f) for f in l.split(",")]) for l in lines]

    return distance, points

def abscisse(point):
    """ Abscisse d'un point"""
    return(point.x)

def ordonnee(point):
    """ Ordonnee d'un point"""
    return(point.y)

def prochesY(SortedY, d):
    # print(SortedX)
    i = 1
    proche = [SortedY[i - 1]]
    while abs(SortedY[i - 1].y - SortedY[i].y) < d and i + 1 < len(SortedY):
        proche.append(SortedY[i])
        i += 1

    if abs(SortedY[i - 1].y - SortedY[i].y) < d:
        proche.append(SortedY[i])
    return proche

def prochesX(SortedX, d):
    i = 1
    proche = [SortedX[i - 1]]
    while abs(SortedX[i - 1].x - SortedX[i].x) < d and i + 1 < len(SortedX):
        proche.append(SortedX[i])
        i += 1

    if abs(SortedX[i - 1].x - SortedX[i].x) < d:
        proche.append(SortedX[i])

    return proche

def print_components_sizes(distance, points):

    """
    affichage des tailles triees de chaque composante
    """
    segments = []
    research_base = [point for point in points]

    d = distance / sqrt(2)
    n = int(1 / d)

    segments_horizentaux = [Segment([Point([i*d, 0]), Point([i*d, 1])]) for i in range(n+1)]
    segments_verticaux = [Segment([Point([0, i*d]), Point([1, i*d])]) for i in range(n+1)]
    origine = Point([0.0, 0.0])
    total = research_base.copy()
    s = 0
    while len(research_base) > 0:
        current = research_base[0]
        research_base.pop(0)
        for point in research_base:
            if current.distance_to(point) < distance:
                s += 1
                segments.append(Segment([current, point]))


    tycat(origine, total, segments + segments_horizentaux + segments_verticaux)
    # tycat(origine, total)

def main():
    """
    ne pas modifier: on charge une instance et on affiche les tailles
    """
    for instance in argv[1:]:
        distance, points = load_instance(instance)
        # print(distance)
        print_components_sizes(distance, points)




main()
