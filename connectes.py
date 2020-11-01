#!/usr/bin/env python3
"""
compute sizes of all connected components.
sort and display.
"""
from time import time
from timeit import timeit
from sys import argv
from geo.tycat import tycat
from geo.point import Point


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

def ancetres_fils(distance, points):
    """
    premiere etape:
        On considère que l'ensemble des points constitue un graphe.
        On modelise chaque composante connexe par un arbre.
        on utilise un dictionnaire, dont les clefs sont les points
        (les fils) et les valeurs sont des listes de points (pères).
    """
    dictionnaire = dict()
    existe = set()
    for point1 in iter(points):
        if point1 in existe:
            # on choisit l'un des pères comme représentant
            commun = dictionnaire[point1][0]
        else:
            # sinon, un point est fils de lui même
            dictionnaire[point1] = [point1]
            existe.add(point1)
            commun = point1
        # Après avoir séléctionner le nouveau père, on détècte
        # les arêtes possibles ( càd les distances vérifiant la condition)
        for point2 in iter(points):
            if point2 not in dictionnaire:
                dictionnaire[point2] = []
            if point1.distance_to(point2) <= distance:
                dictionnaire[point2].append(commun)
                existe.add(point2)
    return dictionnaire

def arbres_possibles(dictionnaire, points):
    """
    Deuxieme étape: On utilise un dictionnaire
    dont les clefs sont les (points) racines des arbres et
    les valeurs sont les voisins de chaque point.
    """
    ensembles = dict()
    for point1 in iter(points):
        if point1 not in ensembles:
            ensembles[point1] = []
        for point2 in dictionnaire[point1]:
            if point2 not in ensembles:
                ensembles[point2] = []
            ensembles[point2] += [point1]
    return ensembles

def union_arbres(ensembles, points):
    """
    Troisième étape: On fait l'union des arbres qui ont des points communs,
    tout en supprimant les arbres dont les somments sont déjà existent
    dans d'autres arbres plus grands au niveau de nombre des sommets.
    """
    listes = []
    for point in iter(points):
        ajout = True
        indix = []
        sous_liste = []
        for indice, liste in enumerate(listes):
            if set(ensembles[point]) & set(liste):
                indix += [indice]
                sous_liste += liste
                ajout = False
        if ajout:
            if ensembles[point]:
                listes.append(ensembles[point])
        else:
            for indice in indix[-1: ]:
                del listes[indice]
            listes.append(sous_liste + ensembles[point])
    return listes

def tri_size(listes, points):
    """
    Finalement: On tri la liste selon la longueur de ses sous-listes
                tout en supprimant les listes qui se répètent.
    """

    size = []
    listes = sorted(listes, key=len)
    listes.reverse()
    ajout = True
    for i, liste in enumerate(listes):
        ajout = True
        for j in range(i):
            if set(listes[i]) & set(listes[j]):
                ajout = False
                break
        if ajout:
            if set(liste) | set(points) == set(points):
                size += [len(list(set(liste)))]
    size = sorted(size)
    size.reverse()
    return size

def print_components_sizes(distance, points):
    """
    affichage des tailles triees de chaque composante
    """
    tmps1=time()
    dictionnaire = ancetres_fils(distance, points)
    ensembles = arbres_possibles(dictionnaire, points)
    listes = union_arbres(ensembles, points)
    size = tri_size(listes, points)
    print(size)
    tmps2=time()
    print(tmps2-tmps1)



def main():
    """
    ne pas modifier: on charge une instance et on affiche les tailles
    """
    for instance in argv[1:]:
        distance, points = load_instance(instance)
        print_components_sizes(distance, points)

main()
