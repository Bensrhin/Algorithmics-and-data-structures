#!/usr/bin/env python3.6

from timeit import timeit
from sys import argv
from connectes import *
from geo.point import Point
from geo.tycat import tycat
from geo.segment import Segment

import sys
import time
try:
    assert(len(sys.argv)==3)
    filename = sys.argv[1]
    if sys.argv[2] == '--hash':
        hashing=True
    elif sys.argv[2] == '--no-hash':
        hashing=False
    else:
        raise()
    t = time.time()
    print("on charge les segments")
    segment = load_instance(filename)
    m = len(segment)
    # print("on crée le graphe")
    # graph = Graph(segment)
    n=len(graph.vertices)
    print("on reconnecte le graphe")
    # graph.reconnect(hashing)
    print("on rend tous les sommets de degrés pairs")
    # graph.even_degrees(hashing)
    print("on génère le cycle eulérien")
    # C=graph.eulerian_cycle()
    print("l'execution a pris ",time.time() -t,"second")
    print("le graphe avait {} arêtes et {} sommets".format(m,n))
except:
    print("Usage:",sys.argv[0],"$filename","HashOption = hash ? --hash , --no-hash  ")
