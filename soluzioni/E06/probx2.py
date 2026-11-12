#####################################################
# S. Germani (stefano.germani@unipg.it)             #
#                                                   #
# Universià degli Studi di Perugia                  #
# Corso di Metodi Computazionali per la Fisica      #
#---------------------------------------------------#
# Esercitazione 5 - Metodi Monte Carlo:            #
#                                                   #
#   Distribuzione di Probabilità p(x) ~ x^2         #
#                                                   #
#####################################################


import sys,os
import numpy as np

import matplotlib.pyplot as plt



def prob(x):
    """
    funzione per probabilità di x p(x) = 6/1000 x^2
    
    return 3/1000 x^2
    """
    return 3/1000*x**2
    

def x_cum(N):
    """
    funzione per generare una distribuzione random di valori x con p(x)=3/1000 x^2
    N   : dimensione dell'array di valori di phi  generato

    Genera N valori random della cumulativa (cum) con probabilità uniforme nell'intervallo [0,1]
    Calcola il valore di x dalla cumulativa inversa x = (1000*cum)^1/3

    return x
    """
    
    # valore random per cumulativa 
    cum = np.random.random(N)
    # x da inversa cumulativa
    x = (1000*cum)**(1/3)
        
    return x

def x_hitmiss(N):
    """
    funzione per generare una distribuzione random di valori x con p(x)=6/1000 x^2
    N   : dimensione dell'array di valori di phi  generato

    Genera N valori random per la x [0,10] e altrettanti per la y [0, pmax=0.3]
    Restituisce solo  i valori di x per cui y<p(x)

    return x
    """
    
    # valore random per x e y
    x = np.random.uniform(0,  10, N)
    y = np.random.uniform(0, 0.6, N)

    # maschera su p(x)
    ymask = y < 3/1000 *x**2

    # restituisco x con maschera        
    return x[ymask]





def distribution():

    
    # array con valori di phi per grafico prob(x)
    xx = np.arange(0, 10, 0.1)

    # Grafico prob(x)
    plt.plot(xx, prob(xx) )
    plt.xlabel(r'X')
    plt.ylabel(r'Y')
    plt.show()
    
    
    #----------------------------------------------------------#
    # Genrazione distribuzione secondo p(phi)
    #----------------------------------------------------------#
    
    N = 100000    # eventi generati
    
    xbins = 99         # numero bin per histogramma phi
    binw = (10/xbins)  #largezza bin

    
    # Fattori di conversione fra altezza bin e probabilità 
    p2n = N*binw  # fattore di conversione da probabilità ad altezza bin
    n2p = 1/p2n   # fattore di conversione da altezza bin a probabilità 

    
    # Genero N valori di x secondo la distrbuzione di probabilità prob(x)
    myx_cum     = x_cum(N)
    myx_hitmiss = x_hitmiss(N)

    # ulteriore fattore di conversione per Hit or Miss
    hmc = len(myx_hitmiss)/N

    
    # Istogramma valori di x generati  con la cumulativa sovrapposta la curva di valori attesi
    nb,xbins,_ = plt.hist(myx_cum, bins=xbins, color='royalblue', label='Cumulativa' )
    plt.plot(xx, p2n*prob(xx),  color='orange', label=r'$N \cdot prob(x)$')
    plt.xlabel(r'X')
    plt.ylabel(r'Eventi')
    plt.legend(fontsize=14)
    plt.show()

    # Istogramma valori di x generati  con metodo Hit or Miss sovrapposta la curva di valori attesi
    nb,xbins,_ = plt.hist(myx_hitmiss, bins=xbins, color='limegreen', label='Hit or Miss' )
    plt.plot(xx, p2n*hmc*prob(xx),  color='orange', label=r'$N_{sel} \cdot prob(x)$')
    plt.xlabel(r'X')
    plt.ylabel(r'Eventi')
    plt.legend(fontsize=14)
    plt.show()

    #print(nb)
    #print(xbins)


    # Confornto Istogramma valori di x generati  con la cumulativa e con metodo Hit or Miss
    plt.hist(myx_cum,     bins=xbins, color='royalblue',  label='Cumulativa' )
    plt.hist(myx_hitmiss, bins=xbins, color='limegreen', label='Hit or Miss' )
    plt.xlabel(r'X')
    plt.ylabel(r'Eventi')
    plt.legend(fontsize=14)
    plt.show()



    
if __name__ == "__main__":

    distribution()
