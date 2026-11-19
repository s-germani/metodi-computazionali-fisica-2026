#####################################################
# S. Germani (stefano.germani@unipg.it)             #
#                                                   #
# Universià degli Studi di Perugia                  #
# Corso di Metodi Computazionali per la Fisica      #
#---------------------------------------------------#
# Esercitazione 7 - Integrazione e Derivazione:     #
#                                                   #
#   Periodo Oscillatore Anarmonico                  #
#                                                   #
#####################################################

import sys,os
import numpy as np
from  scipy import integrate 
import matplotlib.pyplot as plt

import argparse

# Funzioni per Energia potenziale

def V6(x, c):
    """
    Energia potenziale dipendnente da x^6

    V(x,c)=cx^6    
    """
    return c*x**6
    

def V4(x, c):
    """
    Energia potenziale dipendnente da x^4

    V(x,c)=cx^4    
    """
    return c*x**4

def V2(x, c):
    """
    Energia potenziale dipendnente da x^2

    V(x,c)=cx^2    
    """

    return c*x**2


def V15(x, c):
    """
    Energia potenziale dipendnente da |x|^3/2

    V(x,c)=c|x|^3/2
    """
    return c*np.power(np.abs(x),1.5)


def parse_arguments():
    parser = argparse.ArgumentParser(description='Calcolo periodo oscillatori non armonici.')
    parser.add_argument('--v6',    action='store_true', help='Potenziale V = c x^6')
    parser.add_argument('--v4',    action='store_true', help='Potenziale V = c x^4')
    parser.add_argument('--v2',    action='store_true', help='Potenziale V = c x^2')
    parser.add_argument('--v15',   action='store_true', help='Potenziale V = c |x|^3/2')
    parser.add_argument('--vall',  action='store_true', help='Confronto diversi potenziali')
    return  parser.parse_args()


# Funzione principale con clacolo e grafico periodi
def oscillatore():


    args = parse_arguments()

    
    # Costante per V(x,c)
    vc = 1

    # Massa
    m = 1 # kg


    # Lista per ampiazza massima
    al   = [] 

    # Array per Periodi
    T15 = np.empty(0)
    T2  = np.empty(0)
    T4  = np.empty(0)
    T6  = np.empty(0)

    # dx usato per la regola di Simpson
    dx = 0.0001

    
    # Ciclo per diverse ampiezze massime
    for x0 in np.arange(0.5, 6, 0.1):

        # ampiezza massima a = x0
        al  += [ x0 ]

        # valori x per lintegrazione (0-x0)
        xx = np.arange(0, x0, dx)

        # Funzioni integrande: 1/sqrt(V(x0) - V(x))
        integrand15 = 1./np.sqrt(V15(x0, vc) - V15(xx, vc))
        integrand2  = 1./np.sqrt(V2(x0, vc)  - V2(xx, vc))
        integrand4  = 1./np.sqrt(V4(x0, vc)  - V4(xx, vc))
        integrand6  = 1./np.sqrt(V6(x0, vc)  - V6(xx, vc))

        # Integrali secondo la regola di Simpson
        integral15 = integrate.simpson(integrand15, dx=dx)
        integral2  = integrate.simpson(integrand2,  dx=dx)
        integral4  = integrate.simpson(integrand4,  dx=dx)
        integral6  = integrate.simpson(integrand6,  dx=dx)


        # Calcolo periodi
        T15 = np.append( T15, np.sqrt(8*m) * integral15)
        T2  = np.append( T2,  np.sqrt(8*m) * integral2 )
        T4  = np.append( T4,  np.sqrt(8*m) * integral4 )
        T6  = np.append( T6,  np.sqrt(8*m) * integral6 )


    # Array ampiezze da lista
    a = np.array(al)
        
    # Periodo teorico per oscillatore armonico: 2pi sqrt(m/k) 
    k = 2*vc
    Tarm = 2*np.pi *np.sqrt(m/k)


    
    ############## Grafici periodo e energia potenziali #####################


    if args.v6 == True:
        fig,ax = plt.subplots(2,1, figsize=(10, 10) )

        # subplot periodo
        ax[0].plot(a, T6,   color='magenta',          lw=3, label='V(x)=c$x^6$')
        ax[0].axhline(Tarm, color='tomato',   ls=':', label=r'$2 \pi \sqrt{2c/m}$')

        ax[0].legend(loc='upper center', fontsize=13)
        ax[0].set_xlabel(r'$x_0$ [m]')
        ax[0].set_ylabel(r'T [s]')
        ax[0].set_ylim(0, 14)

        # subplot energia potenziale
        xa = np.linspace(-1.15, 1.15, 100)

        ax[1].plot(xa, V6(xa, vc),   color='magenta',   lw=3, label='V(x)=c$x^6$')

        ax[1].legend(fontsize=13)
        ax[1].set_xlabel(r'$x$ [m]')
        ax[1].set_ylabel(r'V [J]')

        plt.show()



    if args.v4 == True:
        fig,ax = plt.subplots(2,1, figsize=(10, 10) )

        # subplot periodo
        ax[0].plot(a, T4,   color='royalblue',         lw=3, label='V(x)=c$x^4$')
        ax[0].axhline(Tarm, color='tomato',    ls=':', label=r'$2 \pi \sqrt{2c/m}$')

        ax[0].legend(loc='upper center', fontsize=13)
        ax[0].set_xlabel(r'$x_0$ [m]')
        ax[0].set_ylabel(r'T [s]')
        ax[0].set_ylim(0, 14)

        # subplot energia potenziale
        xa = np.linspace(-1.15, 1.15, 100)

        ax[1].plot(xa, V4(xa, vc),   color='royalblue', lw=3, label='V(x)=c$x^4$')

        ax[1].legend(fontsize=13)
        ax[1].set_xlabel(r'$x$ [m]')
        ax[1].set_ylabel(r'V [J]')

        plt.show()

    if args.v2 == True:
        fig,ax = plt.subplots(2,1, figsize=(10, 10) )

        # subplot periodo
        ax[0].plot(a, T2,   color='limegreen',         lw=3, label='V(x)=c$x^2$')
        ax[0].axhline(Tarm, color='tomato',    ls=':', label=r'$2 \pi \sqrt{2c/m}$')

        ax[0].legend(loc='upper center', fontsize=13)
        ax[0].set_xlabel(r'$x_0$ [m]')
        ax[0].set_ylabel(r'T [s]')
        ax[0].set_ylim(0, 14)

        # subplot energia potenziale
        xa = np.linspace(-1.15, 1.15, 100)

        ax[1].plot(xa, V2(xa, vc),   color='limegreen', lw=3, label='V(x)=c$x^2$')

        ax[1].legend(fontsize=13)
        ax[1].set_xlabel(r'$x$ [m]')
        ax[1].set_ylabel(r'V [J]')

        plt.show()


        
    if args.v15 == True:
        fig,ax = plt.subplots(2,1, figsize=(10, 10) )

        # subplot periodo
        ax[0].plot(a, T15,  color='slategray',         lw=3, label='V(x)=c$|x|^{3/2}$')
        ax[0].axhline(Tarm, color='tomato',    ls=':', label=r'$2 \pi \sqrt{2c/m}$')

        ax[0].legend(loc='upper center', fontsize=13)
        ax[0].set_xlabel(r'$x_0$ [m]')
        ax[0].set_ylabel(r'T [s]')
        ax[0].set_ylim(0, 14)

        # subplot energia potenziale
        xa = np.linspace(-1.15, 1.15, 100)

        ax[1].plot(xa, V15(xa, vc),  color='slategray', lw=3, label='V(x)=c$|x|^{3/2}$')

        ax[1].legend(fontsize=13)
        ax[1].set_xlabel(r'$x$ [m]')
        ax[1].set_ylabel(r'V [J]')

        plt.show()

        
    if args.vall == True:
        fig,ax = plt.subplots(2,1, figsize=(10, 10) )

        # subplot periodo
        ax[0].plot(a, T15,  color='slategray',        lw=3, label='V(x)=c$|x|^{3/2}$')
        ax[0].plot(a, T2,   color='limegreen',        lw=3, label='V(x)=c$x^2$')
        ax[0].plot(a, T4,   color='royalblue',        lw=3, label='V(x)=c$x^4$')
        ax[0].plot(a, T6,   color='magenta',          lw=3, label='V(x)=c$x^6$')
        ax[0].axhline(Tarm, color='tomato',   ls=':', label=r'$2 \pi \sqrt{2c/m}$')

        ax[0].legend(loc='upper center', fontsize=13)
        ax[0].set_xlabel(r'$x_0$ [m]')
        ax[0].set_ylabel(r'T [s]')
        ax[0].set_ylim(0, 14)

        # subplot energia potenziale
        xa = np.linspace(-1.15, 1.15, 100)

        ax[1].plot(xa, V15(xa, vc),  color='slategray', lw=3, label='V(x)=c$|x|^{3/2}$')
        ax[1].plot(xa, V2(xa, vc),   color='limegreen', lw=3, label='V(x)=c$x^2$')
        ax[1].plot(xa, V4(xa, vc),   color='royalblue', lw=3, label='V(x)=c$x^4$')
        ax[1].plot(xa, V6(xa, vc),   color='magenta',   lw=3, label='V(x)=c$x^6$')

        ax[1].legend(fontsize=13)
        ax[1].set_xlabel(r'$x$ [m]')
        ax[1].set_ylabel(r'V [J]')

        plt.show()

    



if __name__ == "__main__":

    oscillatore()


