#####################################################
# S. Germani (stefano.germani@unipg.it)             #
#                                                   #
# Universià degli Studi di Perugia                  #
# Corso di Metodi Computazionali per la Fisica      #
#---------------------------------------------------#
# Esercitazione 7 - Integrazione e Derivazione:     #
#                                                   #
#   Minimi Segnali Oscilloscopio                    #
#                                                   #
#####################################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import argparse


# Funzione che implementa una versione della differenza centarle con 
# f'(i) =  [f(i+n)-f(i-n)] / [x(i+n)-x[i-n]]
def differenza_centrale(xx, yy, nh):
    dd = yy[nh:] - yy[:-nh]
    hh = xx[nh:] - xx[:-nh]
    
    for ih in range(int(nh/2)):
        dd = np.append(yy[nh-ih-1]-yy[0], dd)
        dd = np.append(dd, yy[-1]-yy[-(nh-ih)])
    
        hh = np.append(xx[nh-ih-1]-xx[0], hh)
        hh = np.append(hh, xx[-1]-xx[-(nh-ih)])
    
    print('dd', dd)
    print('hh', hh)
    return dd/hh






def signal_times():

    # leggi file con segnali oscilloscopio
    dfsig = pd.read_csv('oscilloscope.csv')


    #################  Controlli  preliminari ############################# 

    print('Dimensioni dati', dfsig.shape )

    print('Colonne Data Frame', dfsig.columns)

    # grafico dei segnali
    plt.subplots(figsize=(10, 8))
    plt.title('Segnali Oscilloscopio', fontsize=16, color='slategray')
    plt.plot(dfsig['time'], dfsig['signal1'], color='limegreen',   label='Canale 1')
    plt.plot(dfsig['time'], dfsig['signal2'], color='darkorange',  label='Canale 2')                 
    plt.legend(fontsize=14)
    plt.xlabel('t [ns]')
    plt.ylabel('V [mV]')
    plt.show()



    #################  Calcolo derivate  ################################ 

    # derivata con differenza centrale dh=2
    dc1_ch1 = differenza_centrale(dfsig['time'].to_numpy(), dfsig['signal1'].to_numpy(), 2)  # canale 1
    dc1_ch2 = differenza_centrale(dfsig['time'].to_numpy(), dfsig['signal2'].to_numpy(), 2)  # canale 2

    # grafico derivata dh=2
    plt.subplots(figsize=(10, 8))
    plt.title('Derivata Segnali Oscilloscopio - h=2 ns', fontsize=16, color='slategray')
    plt.plot(dfsig['time'], dc1_ch1, color='limegreen',   label='Canale 1')
    plt.plot(dfsig['time'], dc1_ch2, color='darkorange',  label='Canale 2')                 
    plt.legend(fontsize=14)
    plt.xlabel('t [ns]')
    plt.ylabel('V/s [mV/ns]')
    plt.show()



    

    # derivata con differenza centrale dh=100
    dc100_ch1 = differenza_centrale(dfsig['time'].to_numpy(), dfsig['signal1'].to_numpy(), 100)  # canale 1
    dc100_ch2 = differenza_centrale(dfsig['time'].to_numpy(), dfsig['signal2'].to_numpy(), 100)  # canale 2

    # grafico derivata dh=100
    plt.subplots(figsize=(10, 8))
    plt.title('Derivata Segnali Oscilloscopio - h=100 ns', fontsize=16, color='slategray')
    plt.plot(dfsig['time'], dc100_ch1, color='limegreen',   label='Canale 1')
    plt.plot(dfsig['time'], dc100_ch2, color='darkorange',  label='Canale 2')                 
    plt.legend(fontsize=14)
    plt.xlabel('t [ns]')
    plt.ylabel('V/s [mV/ns]')
    plt.show()



    


    #################  Calcolo media mobile per derivata  ################################ 

    der_sig1 = np.convolve(dc100_ch1,  np.ones(5), 'same') / 5
    der_sig2 = np.convolve(dc100_ch2,  np.ones(5), 'same') / 5


    # grafico derivata dh=100 avg 5
    plt.subplots(figsize=(10, 8))
    plt.title('Derivata Segnali Oscilloscopio - h=100 ns - media 5', fontsize=16, color='slategray')
    plt.plot(dfsig['time'], der_sig1, color='limegreen',   label='Canale 1')
    plt.plot(dfsig['time'], der_sig2, color='darkorange',  label='Canale 2')                 
    plt.legend(fontsize=14)
    plt.xlabel('t [ns]')
    plt.ylabel('V/s [mV/ns]')
    plt.show()


    #################  Selezione minimi  ################################ 
    # Selezione punti con derivata vicina a zero (<0.015)
    #  e segnale superiore alla soglia di 10 mV (in negativo)
    #
    # Più valori vicini soddisfano al condizione nella posizione intorno al minimo
    #  viene considerato solo il primo in una finestra di  20 ns

    selmask_sig1 = (np.abs(der_sig1)< 0.015 ) & (dfsig['signal1'].to_numpy() < -10)
    selmask_sig2 = (np.abs(der_sig2)< 0.015 ) & (dfsig['signal2'].to_numpy() < -10)

    print('---der0 sig1 ---', dfsig['time'].to_numpy()[selmask_sig1])
    print('---der0 sig2 ---', dfsig['time'].to_numpy()[selmask_sig2])


    # accorpamento punti per Canale 1
    tpeak_sig1 = np.empty(0)
    vpeak_sig1 = np.empty(0)
    tsum = dfsig['time'].to_numpy()[selmask_sig1][0]
    nsum = 1
    for it in range( 1, len(dfsig['time'].to_numpy()[selmask_sig1])):
        if ( (dfsig['time'].to_numpy()[selmask_sig1][it]-dfsig['time'].to_numpy()[selmask_sig1][it-1]) > 20)  or (it == (len(dfsig['time'].to_numpy()[selmask_sig1]))-1):
            print(tsum)
            tpeak_sig1 = np.append( tpeak_sig1, tsum)
            vpeak_sig1 = np.append( vpeak_sig1, dfsig['signal1'].to_numpy()[tsum] )
            tsum = dfsig['time'].to_numpy()[selmask_sig1][it]

   
    # accorpamento punti per Canale 2
    tpeak_sig2 = np.empty(0)
    vpeak_sig2 = np.empty(0)
    tsum = dfsig['time'].to_numpy()[selmask_sig2][0]
    nsum = 1
    for it in range( 1, len(dfsig['time'].to_numpy()[selmask_sig2])):
        if ( (dfsig['time'].to_numpy()[selmask_sig2][it]-dfsig['time'].to_numpy()[selmask_sig2][it-1]) > 20 ) or it == ( len(dfsig['time'].to_numpy()[selmask_sig2]))-1 :
            tpeak_sig2 = np.append( tpeak_sig2, tsum)
            vpeak_sig2 = np.append( vpeak_sig2, dfsig['signal2'].to_numpy()[tsum] )
            tsum = dfsig['time'].to_numpy()[selmask_sig2][it]

            
    #print(tpeak_sig1)
    

    #print( dfsig['time'].to_numpy()[selmask_sig1] )

    #################  Grafico Segnali e Minimi  ################################ 
    plt.subplots(figsize=(10,8))
    plt.title('Segnali Oscilloscopio con Minimi identificati', fontsize=16, color='slategray')
    plt.plot( dfsig['time'].to_numpy(), dfsig['signal1'].to_numpy(), color='limegreen',  label='Canale 1' )
    plt.plot( dfsig['time'].to_numpy(), dfsig['signal2'].to_numpy(), color='darkorange', label='Canale 2' )
    plt.plot( tpeak_sig1, vpeak_sig1, 'o', color='darkgreen',  label='Min. Canale 1' )
    plt.plot( tpeak_sig2, vpeak_sig2, 'o', color='red',        label='Min. Canale 2' )
    plt.legend(fontsize=14)
    plt.xlabel('t [ns]')
    plt.ylabel('V [mV]')
    plt.ylim(-90, 10)
    plt.show()


    
    
if __name__ == "__main__":

    signal_times()
