#!/usr/bin/env python3
import numpy as np
from random import random
from os import system
import matplotlib.pyplot as plt
def generer(nombre, distance):
    """
    generer un fichier de n points
    """
    with open("test/{}.pts".format(nombre), "w") as file:
        file.write("{}\n".format(distance))
        for _ in range(nombre):
            point = random(), random()
            file.write("{}, {}\n".format(point[0], point[1]))
        file.close()
def executer(file):
    """
    executer un fichier ordonné
    """
    system("./connectes.py {} > {}.txt".format(file, file))


def lecture_time(file):
    """
    lecture du temps pour un fichier
    """
    with open(file, "r") as file_time:
        next(file_time)
        lines = iter(file_time)
        time = float(next(lines))
    file_time.close()
    return(time)

def dessin(distance):
    """
    dessin courbe performance
    """
    nombres = [i for i in range(20, 500)]
    time = []
    for nombre in nombres:
        generer(nombre, distance)
        executer("test/{}.pts".format(nombre))
        time += [lecture_time("test/{}.pts.txt".format(nombre))]
    nombres = np.array(nombres)
    time = np.array(time)
    plt.plot(nombres, time)
    plt.xlabel("le nombre de points",fontsize=16)#l'axe des abscisses
    plt.ylabel("temps (s)",fontsize=16)# l'axe des ordonnées
    plt.title("le temps d'exécution de connectes.py ") # le titre de la représentation
    plt.show()
dessin(0.1)
