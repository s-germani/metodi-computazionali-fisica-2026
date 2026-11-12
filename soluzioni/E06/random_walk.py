#####################################################
# S. Germani (stefano.germani@unipg.it)             #
#                                                   #
# Universià degli Studi di Perugia                  #
# Corso di Metodi Computazionali per la Fisica      #
#---------------------------------------------------#
# Esercitazione 5 - Metodi Monte Carlo:            #
#                                                   #
#   modulo per random wallk per Diffusione 2D       #
#   - random_walk2d:      diffusione simmetrica     #
#                                                   #
#####################################################


import sys,os
import numpy as np
import pandas as pd

from scipy import integrate


############################################################
#            Random Walk 2D Uniforme                       #
############################################################


def random_walk2d(step, N):
    """
    funzione random_walk2d(step, N) per generare una sequenza di random walk 2D
        ad ogni passo il moto sarà lungo la direzione casuale 
        dettata dall'angolo phi  
    step: passo del random walk
    N   : numero di passi

    per ogni passo delta_X = step*cos(phi), delta_Y = step*sin(phi), 
    reuturn deltax, deltay: array con coordinate per i diversi passi
    """

    # Array posizioni x e y (partenza dalla posizione 0,0)
    deltax = np.array([0])
    deltay = np.array([0])

    # Valori random di phi per gli N passi distribuiti uniformemente
    phi = np.random.uniform(low=0, high=2*np.pi, size=N)

    # Ciclo sui valori di phi per calcolare gli spostamenti 
    for p in phi:

        # Valori temporanei con nuovo step
        tmpx = deltax[-1] + step*np.cos(p)
        tmpy = deltay[-1] + step*np.sin(p)

        # Appendo nuove posizione agli array degli spostamenti
        deltax = np.append(deltax, tmpx)
        deltay = np.append(deltay, tmpy)
        
    return deltax, deltay
