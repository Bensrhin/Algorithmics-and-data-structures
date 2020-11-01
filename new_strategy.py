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
     i = 0
     proche = [SortedY[i]]
     while abs(SortedY[i].y - SortedY[i + 1].y) < d/sqrt(2) and i + 2 < len(SortedY):
         proche.append(SortedY[i + 1])
         i += 1
     return proche

 def prochesX(SortedX, d):
     i = 0
     proche = [SortedX[i]]
     while abs(SortedX[i].x - SortedX[i + 1].x) < d/sqrt(2) and i + 2 < len(SortedX):
         proche.append(SortedX[i + 1])
         i += 1
     return proche

 def print_components_sizes(distance, points):
     """
     affichage des tailles triees de chaque composante
     """
     SortedX = sorted([point for point in points], key = abscisse)

     result = prochesX(SortedX, distance)
     dernier_pointX_1 = result[len(result)-1]
     dernier_indice = SortedX.index(dernier_pointX_1)

     origine = Point([0.0, 0.0])
     segment_1 = Segment([Point([dernier_pointX_1.x, 0]), Point([dernier_pointX_1.x, 1])])

     SortedY = sorted([point for point in result], key = ordonnee)
     result_bis = prochesY(SortedY, distance)
     dernier_pointXbis_1 = result_bis[len(result_bis)-1]
     dernier_indice_bis = SortedX.index(dernier_pointXbis_1)

     segment_2 = Segment([Point([0, dernier_pointXbis_1.y]), Point([1, dernier_pointXbis_1.y])])
     tycat(origine, points, (segment_1, segment_2))
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
     tycat(origine, total, segments)

 def main():
     """
     ne pas modifier: on charge une instance et on affiche les tailles
     """
     for instance in argv[1:]:
         distance, points = load_instance(instance)
         # tycat(points)
         print(distance)
         print_components_sizes(distance, points)
     # r = dedup([1,1,1,1,2])
     # print(r)



 main()
