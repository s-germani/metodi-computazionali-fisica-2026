#####################################################
# S. Germani (stefano.germani@unipg.it)             #
#                                                   #
# Universià degli Studi di Perugia                  #
# Corso di Metodi Computazionali per la Fisica      #
#---------------------------------------------------#
# Esercitazione 5 - Funzioni Moduli e Classi:       #
#                                                   #
#   Semplice modulo con alcune funzioni             #
#                                                   #
#####################################################

import sys,os
import numpy as np


def somma_n(n):
    """
    Funzione che calcola la somma dei primi n numeri naturali
    
    somma_n(n):

    Parametri
    -----------
        n:   valore massimo dei numeri naturali da sommare
    
    Restituisce
    -----------
       ans: somma dei valori interi compresi fra 1 e n    
    """

    an = np.arange(n+1)
    return an.sum()

def somma_sqrtn(n):
    """
    Funzione che calcola la somma delle radici dei primi n numeri naturali

    somma_sqrtn(n):
    
    Parametri
    -----------
        n:   valore massimo dei numeri naturali da considerare
    
    Restituisce
    -----------
       rns: somma delle radici dei valori interi compresi fra 1 e n    
    """

    an = np.arange(n+1)
    rn = np.sqrt(an)
    return rn.sum()



def sommaprod_n(n):
    """
    Funzione che calcola la somma e il prodotto dei primi n numeri naturali

    sommaprod_n(n)
    
    Parametri
    -----------
        n:   valore massimo dei numeri naturali da sommare
    
    
    Restituisce
    -----------
        san,pan
        san :  somma dei valori interi compresi fra 1 e n    
        pan :  prodotto dei valori interi compresi fra 1 e n    

    """


    san = somma_n(n)
    an = np.arange(n+1)

    pan = 0
    for v in an:
        pan*=v
    
    return san, pan



def sommaexp_n(n, alpha=1, **kwargs):
    """
    Funzione che calcola la somma i^alpha con i compreso fra 1 e il valore massimo n
    
    sommaexp_n(n, alpha=1)

    Parametri
    -----------
        n:      valore massimo dei numeri naturali da considerare
        alpha:  esponente dei termini della somma
    
    
    Restituisce
    -----------
        sexp: sommatoria i^alpha con i compreso fra 1 e n        

    """

    
    an = np.arange(n+1)

    sexp = np.power( an, alpha)

    return sexp.sum()
