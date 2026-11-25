#####################################################
# S. Germani (stefano.germani@unipg.it)             #
#                                                   #
# Universià degli Studi di Perugia                  #
# Corso di Metodi Computazionali per la Fisica      #
#---------------------------------------------------#
# Esercitazione  7 - Equazioni e Minimizzazione:    #
#                                                   #
#   Fit di un set di dati                           #
#                                                   #
#####################################################

import sys,os
import numpy as np
import pandas as pd

from scipy import optimize

import matplotlib.pyplot as plt

import argparse



# Funzione per calcolo massa invariante
def invariant_mass(E1, p1, E2, p2):
    """
    invariant_mass(E1, p1, E2, p2)
    
    Calcola massa invariante a partire dal  quadrimpulso di due particelle

    Parametri
    ---------------
    E1 : energia particella 1
    p1 : quantità di moto particella 1 (vettore 3d)
    E2 : energia particella 2
    p3 : quantità di moto particella 2 (vettore 3d)


    Restituisce
    ---------------
    mi : equivalente in energia della mssa invarante (m c^2)    
    """
    return  np.sqrt( (E1+E2)**2 - ( (p1[0]+p2[0])**2 + (p1[1]+p2[1])**2 + (p1[2]+p2[2])**2) )




# Funzione  per Fit  con una Gaussiana (Segnale) + polinomio di grado 1 (Fondo)
def fung1(x, m, A, s, p0, p1):
    """
    fung1(x, m, A, s, p0, p1)
    
    Calcola somma di una funzione di Gauss + un polinimio di primo grado

    Parametri
    ---------------
    x  : valore o array di valori in cui calcolare la funzione 
    m  : media della funzione di Gauss
    A  : fattore di normalizzazione della funzione di Gauss
    s  : sigma della funzione di Gauss
    p0 : termine costante del polinomio di primo grado
    p1 : coefficiente del polinomio di primo grado

    Restituisce
    ---------------
    fung1(x) = g(x) + bkg(x)

       dove: g(x)   = A*np.exp( -0.5*(x-m)**2/s**2)
             bkg(x) = p1*x+p0
    """

    bkg = p1*x+p0
    sig = A*np.exp( -0.5*(x-m)**2/s**2) 

    return bkg+sig



# Funzione  per Fit  con due Gaussiane (Segnale) + polinomio di grado 1 (Fondo)
def fung2(x, m, A1, A2, s1,s2, p0, p1):
    """
    fung2(x, m, A1, A2, s1,s2, p0, p1)
    
    Calcola somma di due funzione di Gauss con stessa media + un polinimio di primo grado

    Parametri
    ---------------
    x  : valore o array di valori in cui calcolare la funzione 
    m  : media delle due funzioni di Gauss
    A1 : fattore di normalizzazione della prima funzione di Gauss
    A2 : fattore di normalizzazione della seconda funzione di Gauss
    s1 : sigma della prima funzione di Gauss
    s2 : sigma della seconda funzione di Gauss
    p0 : termine costante del polinomio di primo grado
    p1 : coefficiente del polinomio di primo grado

    Restituisce
    ---------------
    fung2(x) = g1(x) + g2(x) + bkg(x)

       dove: g1(x)  = A1*np.exp( -0.5*(x-m)**2/s1**2)
             g2(x)  = A2*np.exp( -0.5*(x-m)**2/s2**2)
             bkg(x) = p1*x+p0
    """

    bkg = p1*x+p0
    gf1 = A1*np.exp(-0.5*(x-m)**2 / s1**2)
    gf2 = A2*np.exp(-0.5*(x-m)**2 / s2**2)
    
    sig=gf1+gf2
    
    return bkg+sig



def parse_arguments():

    parser = argparse.ArgumentParser(description='Plot e fit dati.',
                                     usage      ='python3 fit_data.py  --opzione')
    parser.add_argument('--columns',        action='store_true',    help='Stampa nomi colonne file di dati')
    parser.add_argument('--preliminary',    action='store_true',    help='Grafici preliminari')
    parser.add_argument('--fitg1',          action='store_true',    help='Esegue fit con una funzione di Gauss per il segnale')
    parser.add_argument('--fitg2',          action='store_true',    help='Esegue fit con due funzion1 di Gauss per il segnale')
    
    return  parser.parse_args()


def jpsimass_fit():


    args = parse_arguments()
    
    ################################### Dati Input  ##########################################
    # Lettura file

    # CMS public dataset for  J/Psi --> mu mu  
    dataset = pd.read_csv('http://opendata.cern.ch/record/5203/files/Jpsimumu.csv')
    
    #print(dataset)
    if args.columns == True:
        # Colonne Data Frame
        print('Columns:', dataset.columns)


    ################################### Calcolo Massa  Invariante  ###########################
    E1 = dataset['E1']
    E2 = dataset['E2']

    px1 = dataset['px1']
    py1 = dataset['py1']
    pz1 = dataset['pz1']

    px2 = dataset['px2']
    py2 = dataset['py2']
    pz2 = dataset['pz2']

    mm = invariant_mass( E1, (px1, py1, pz1),
                         E2, (px2, py2, pz2)  )
    
    

    #############################  Grafici Preliminari  ######################################
    if args.preliminary == True:

        ## Grafico Massa Invariante mu mu 
        plt.subplots(figsize=(9,6))
        n, bins, _ = plt.hist(mm, bins=200)
        bw=bins[1]-bins[0]
        
        plt.xlabel(r'$m_{\mu\mu}$ [GeV]', fontsize=14)
        plt.ylabel(r'Events / {:0.3f} GeV'.format(bw), fontsize=14)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        plt.show()


        ## Zoom Grafico Massa Invariante mu mu 
        plt.subplots(figsize=(9,6))
        zn, zbins, _ = plt.hist(mm, bins=200, range=(2.85,3.35))
        zbw=zbins[1]-zbins[0]
        plt.xlabel(r'$m_{\mu\mu}$ [GeV]', fontsize=14)
        plt.ylabel(r'Events / {:0.4f} GeV'.format(zbw), fontsize=14)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        plt.show()



    pnames = None
    params = None
    params_covariance = None
    yfit   = None
    
    #####################################  Fit  con 1 o 2 Gaussiane ###################################
    if args.fitg1 == True or args.fitg2 == True:

        # Plot solo istogramma
        plt.subplots(figsize=(9,6))
        n, bins, _ = plt.hist(mm, bins=200, range=(2.85,3.35))
        bw=bins[1]-bins[0] 
        plt.xlabel(r'$m_{\mu\mu}$ [GeV]', fontsize=14)
        plt.ylabel(r'Events / {:0.3f} GeV'.format(bw), fontsize=14)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        plt.show()

        
        ee = (bins[:-1]+bins[1:])/2

        # Fit per trovare parametri
        xdata = ee
        ydata = n
        if args.fitg1 == True:
            pnames = ['m', 'A', 'sigma', 'p0', 'p1']
            pstart = np.array([3, 100,  0.5, 10, -0.1])            
            params, params_covariance = optimize.curve_fit(fung1, xdata, ydata, sigma=np.sqrt(ydata), absolute_sigma=True,p0=[pstart])
            yfit = fung1(xdata, params[0], params[1], params[2], params[3], params[4])
        
        if args.fitg2 == True:
            pnames = ['m', 'A1', 'A2', 'sigma1', 'sigma2', 'p0', 'p1']
            pstart = np.array([3, 200, 50, 0.5, 2,  10, -0.1])            
            params, params_covariance = optimize.curve_fit(fung2, xdata, ydata, sigma=np.sqrt(ydata), absolute_sigma=True,p0=[pstart])
            yfit = fung2(xdata, params[0], params[1], params[2], params[3], params[4], params[5], params[6])
            
        print('params', params )
        #print('params_cov', params_covariance)
        print('errori params', np.sqrt(params_covariance.diagonal()))
        
        print('--------------------------------------------------------')
        print('           Risultati Fit Massa Invariante               ')
        for name,p,pe in zip(pnames, params, np.sqrt(params_covariance.diagonal()) ):
            print('{:6}  {:>10.4f} +- {:>7.4f}'.format(name,p,pe))

        print('--------------------------------------------------------')
        print('Massa Invarinate = {:>10.4f} +- {:.4f}  Gev/c^2'.format(params[0], np.sqrt(params_covariance[0,0] )) )

            
        fig,ax = plt.subplots(3,1, figsize=(9,9), gridspec_kw={'height_ratios': [3, 1,1]}, sharex=True)
        fig.subplots_adjust(hspace=0)
        ax[0].errorbar(xdata, ydata, yerr=np.sqrt(ydata), fmt='.', label='Data')
        #ax[0].plot(xdata, myfun(xdata, params[0], params[1], params[2], params[3], params[4]))
        ax[0].plot(xdata, yfit, color='darkorange', label='Fit')

        # visualizzazione grafico singole funzioni nel caso di doppia gaussiana
        if args.fitg2 == True:
            ygf1 = params[1]*np.exp(-0.5*(xdata-params[0])**2 / params[3]**2)
            ygf2 = params[2]*np.exp(-0.5*(xdata-params[0])**2 / params[4]**2)
            ax[0].plot(xdata, ygf1, color='grey', ls=':',  label='Gauss1')
            ax[0].plot(xdata, ygf2, color='grey', ls='--', label='Gauss2')

        ax[0].set_ylabel('Events / {:0.4f} GeV'.format(bw))
        ax[0].legend(fontsize=14, frameon=False)
        
        ax[1].errorbar(xdata, ydata-yfit, yerr=np.sqrt(ydata), fmt='.')
        ax[1].axhline(y=0, color='darkorange' )
        ax[1].set_ylabel('Data-Fit')
        ax[1].set_ylim(-45,45)  
        ax[1].set_yticks(np.arange(-25, 26, 25))
        ax[1].grid(True, axis='y')
        
        ax[2].errorbar(xdata, (ydata-yfit)/np.sqrt(ydata), yerr=1, fmt='.')
        ax[2].axhline(y=0, color='darkorange')
        ax[2].set_ylabel(r'(Data-Fit)/$\sigma$')
        ax[2].set_ylim(-4.5,4.5)  
        ax[2].set_yticks(np.arange(-2.5, 2.6, 2.5))
        ax[2].grid(True, axis='y')
        
        ax[2].set_xlabel(r'$m_{\mu\mu}$ [GeV]')

        fig.align_ylabels()
        plt.show()


    




if __name__ == "__main__":

    jpsimass_fit()
    
