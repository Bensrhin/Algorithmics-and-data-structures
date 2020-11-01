#!/usr/bin/env python3

from sys import argv

from geo.point import Point
from geo.tycat import tycat
from geo.segment import Segment
from geo.quadrant import Quadrant

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
def print_components_sizes(distance, points):
    """
    affichage des tailles triees de chaque composante
    """
    segments = []
    research_base = [point for point in points]
    origine = Point([0.0, 0.0])
    total = research_base.copy()
    s = 0
    enveloppe = []
    while len(research_base) > 0:
        current = research_base[0]
        research_base.pop(0)
        for point in research_base:
            if current.distance_to(point) < distance:
                s += 1
                segments.append(Segment([current, point]))
        enveloppe.append(s)
        print(enveloppe)
    tycat(origine, total, segments)

# def intersectionNonVide(A,B):
#     """
#     calculate the intersection between two sets of elements
#     """
#     for element in A:
#         if element in B:
#             return True
#     return False
#
# def dedup(T):
#     SS = []
#     for i in range(len(T)):
#         for j in range(len(T)):
#             if T[i] == T[j] and T[j] not in SS:
#                 SS.append(T[j])
#     return SS
#
# def print_components_sizes(distance, points):
#     """
#     affichage des tailles triees de chaque composante
#     """
#     dict_points = dict()
#     for point in points:
#         dict_points[point] = []
#     for point_1 in points:
#         for point_2 in points:
#             if point_1.distance_to(point_2) <= distance:
#                 dict_points[point_1].append(point_2)
#     tables = [value for value in dict_points.values()]
#     # print(tables)
#     # print(20*'*')
#     # print(dict_points)
#     results = []
#     for table_1 in tables:
#         for table_2 in tables:
#             if table_2 != table_1:
#                 if intersectionNonVide(table_1, table_2):
#                     table_1 += table_2
#         results.append(table_1)
#     # print(results)
#     # print(20*'*')
#     kda = [list(set(l)) for l in results]
#     dedupKda = dedup(kda)
#     kda_2 = [len(e) for e in dedupKda]
#
#     print(sum(kda_2))
#     # print(kda_2)
#     print(len(points))
#

def main():
    """
    ne pas modifier: on charge une instance et on affiche les tailles
    """
    for instance in argv[1:]:
        distance, points = load_instance(instance)
        print_components_sizes(distance, points)


main()
