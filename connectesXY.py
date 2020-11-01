#!/usr/bin/env python3
"""
compute sizes of all connected components.
sort and display.
"""

from math import sqrt
from timeit import timeit
from sys import argv

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
    origine = Point([0.0, 0.0])

    SortedX = sorted([point for point in points], key = abscisse)
    print("nombre de point est :", len(SortedX))
    # print(SortedX)
    result = prochesX(SortedX, distance)

    print("nombre de points dans result est :", len(result))

    n = len(result)
    dernier_pointX_1 = result[-1]

    segment_1 = Segment([Point([dernier_pointX_1.x, 0]), Point([dernier_pointX_1.x, 1])])

    result_droite = SortedX[n:]
    result_gauche = SortedX[:n]

    print(len(result_gauche), len(result_droite))

    SortedY = sorted([point for point in result_gauche], key = ordonnee)
    result_bis = prochesY(SortedY, distance)
    n_bis = len(result_bis)
    print(n_bis)
    print(result_bis)
    dernierbis = result_bis[-1]

    # segment_2 = Segment([Point([0, dernierbis.y]), Point([dernier_pointX_1.x, dernierbis.y])])

    result_bas = result_gauche[n_bis:]
    result_haut = result_gauche[:n_bis]

    print(len(result_haut), len(result_bas))
    #
    dernier_pointXbis_1 = result_bis[-1]
    #
    dernier_indice_bis = result_gauche.index(dernier_pointXbis_1)
    #
    result_haut = result_gauche[dernier_indice_bis + 1:]
    result_bas = result_gauche[:dernier_indice_bis + 1]
    #
    segment_2 = Segment([Point([0, dernier_pointXbis_1.y]), Point([dernier_pointX_1.x, dernier_pointXbis_1.y])])
    #
    # print("*********************************")
    # print(result_haut)
    # print("*********************************")
    # print(result_bas)
    # tycat(origine, points, segment_1)
    tycat(origine, points, (segment_1, segment_2))


    """
    affichage des tailles triees de chaque composante
    """
    segments = []
    research_base = [point for point in points]
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


    tycat(origine, total, segments)

def main():
    """
    ne pas modifier: on charge une instance et on affiche les tailles
    """
    for instance in argv[1:]:
        distance, points = load_instance(instance)
        # print(distance)
        print_components_sizes(distance, points)




main()
