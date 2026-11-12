#####################################################
# S. Germani (stefano.germani@unipg.it)             #
#                                                   #
# Universià degli Studi di Perugia                  #
# Corso di Metodi Computazionali per la Fisica      #
#---------------------------------------------------#
# Esercitazione 6 - Metodi Monte Carlo             #
#                                                   #
#   script  per plot  Diffusione 2D                 #
#                                                   #
#####################################################


import sys,os
import numpy as np
import pandas as pd

from scipy import integrate

import matplotlib.pyplot as plt

import argparse

import random_walk as rw
               



#####################################################################
#            Funzione principale per grafici                        #
#####################################################################

               
def diffusione_2d():
    """
    Funzione che utilizza il modulo random_walk mostra grafici per la diffusione 2D simmetrica e asimmetrica
    """

    # Definizione lunghezza passo (step) e numero passi
    step    = 1
    Nsteps5 = 10000
    MaxDist = 200

    #--------------------------------------------------------#
    #  Random Walk  Unforme                                  # 
    #--------------------------------------------------------#


    ### --------------- plot  5 walker ----------------------

    # Liste per gli array con le posizioni dei random walker
    xx5 = []
    yy5 = []

    # Ciclo per calcolo 5 random walk uniformi da 1000 passi 
    plt.subplots(figsize=(9,8))
    for i in range(5):
        x0,y0 = rw.random_walk2d(step, Nsteps5)
        xx5.append(x0)
        yy5.append(y0)
        plt.scatter(x0,y0, s=3)

    plt.xlabel(r'$\Delta x$')
    plt.ylabel(r'$\Delta y$')
    plt.xlim(-200, 200)
    plt.ylim(-200, 200)
    plt.show()





    ### --------------- plot  5 walker con due pannelli ---------------

    fig, ax = plt.subplots(1,2, figsize=(14,8))
    for i in range(5):
        ax[0].scatter(xx5[i],yy5[i], s=3)
        ax[1].plot(xx5[i]**2+yy5[i]**2) 

    ax[0].set_xlabel(r'$\Delta x$')
    ax[0].set_ylabel(r'$\Delta y$')
    ax[0].set_xlim(-200, 200)
    ax[0].set_ylim(-200, 200)

    ax[1].set_xlabel('step')
    ax[1].set_ylabel(r'$d^2$')
    ax[1].set_ylim(0, MaxDist**2)

    plt.show()




        




                         
if __name__ == "__main__":

    diffusione_2d()
