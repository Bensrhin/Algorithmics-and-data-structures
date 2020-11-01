#!/usr/bin/env python3
"""
Class Nuage et structe du graphe
"""

class Nuage:

  def __init__(self, coords):
    self.x = coords[0]
    self.y = coords[1]

class Graphe:
  def __init__(self, nbrSommets):
    """
    initialisation du graphe
    """
    self.dictionnaire = {}
    self.nbrSommets = nbrSommets

  def connexes(self):
    """
    calcul des composante connexes suivant la premiere methode
    """

    points = iter(self.dictionnaire.keys())
    suivants = [next(points)]
    composantes = []
    taille = 0
    t = set()

    try:

      while True:

        if not suivants:

          if (taille >= 1):

            composantes.append(taille)
            taille = 0

          suivants.append(next(points))

        courant = suivants.pop()

        if courant not in t:

          t.add(courant)
          taille += 1
          fils = self.dictionnaire[courant]
          suivants += fils

    except StopIteration:

      return composantes, (self.nbrSommets - sum(composantes))


  def ajouter_arete(self, arete):
    """ ajouter une arete """
    a = arete
    if a[0] not in self.dictionnaire:
      self.dictionnaire[a[0]]  = [a[1]]
    else:
      self.dictionnaire[a[0]] += [a[1]]
    if a[1] not in self.dictionnaire:
      self.dictionnaire[a[1]]  = [a[0]]
    else:
      self.dictionnaire[a[1]] += [a[0]]
