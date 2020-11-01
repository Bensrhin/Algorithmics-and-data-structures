#!/usr/bin/env python3

"""
compute sizes of all connected components.
sort and display.
"""
from sys import argv
from time import time
from graph import Nuage

def load_instance(filename):
  """
  loads .pts file.
  returns distance limit and points.
  """
  with open(filename, "r") as instance_file:
      lines = iter(instance_file)
      distance = float(next(lines))
      points = [Nuage([float(f) for f in l.split(",")]) for l in lines]

  return distance, points

from math import sqrt
from graph import Graphe
from itertools import product, combinations


def distance_carre(p1, p2):
  """
  calcule la distance entre deux points
  """
  return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def voisins(plan, coordonne, limites):
  """
  Donne les cases voisines de coordonne
  """
  deplacement = [(-1,1), (0,1), (1,1), (1,0)]
  voisins = []

  for d in deplacement:
    voisin_x = coordonne[0] + d[0]
    voisin_y = coordonne[1] + d[1]

    if voisin_x <= limites[0] and voisin_y <= limites[1]:

      if (voisin_x, voisin_y) in plan:
        voisins += plan[voisin_x, voisin_y]

  return voisins


def Bornes(d):
    a, b = 0, 0
    for x,y in d.keys():
      if x > a:
          a = x
      if y > b:
          b = y
    return (a, b)

def decoupe(distance, points):
  """
  decoupe de l'espace en une grille de largeur distance
  """
  largeur = distance
  plan = {}

  for p in points:
    abscisse = p.x
    ordonnee = p.y
    plan_x = int(abscisse / largeur)
    plan_y = int(ordonnee / largeur)

    if (plan_x, plan_y) in plan:
      plan[plan_x, plan_y] += [p]
    else:
      plan[plan_x, plan_y] = [p]

  return plan


def liste_composantes(distance, points):
  """
  calcul des composantes
  """
  plan = decoupe(distance, points)
  limites = Bornes(plan)
  graph = Graphe(len(points))

  for i, j in plan.keys():
    courant = plan[i, j]
    proches = voisins(plan, (i, j), limites)

    for couple in product(courant, proches):
      if distance_carre(*couple) <= distance :

        graph.ajouter_arete(couple)

    for couple in combinations(courant, r = 2):
      if distance_carre(*couple) <= distance :

        graph.ajouter_arete(couple)

  connexes, non_connectes = graph.connexes()
  connexes.sort(reverse = True)

  return connexes + non_connectes*[1]

def print_components_sizes(distance, points):
  """
  affichage des tailles triees de chaque composante
  """
  print(liste_composantes(distance, points))

def main():
  """
  ne pas modifier: on charge une instance et on affiche les tailles
  """
  for instance in argv[1:]:
      distance, points = load_instance(instance)
      tmps1=time()
      print_components_sizes(distance, points)
      tmps2=time()
      print(tmps2-tmps1)
main()
