#####################################################
# S. Germani (stefano.germani@unipg.it)             #
#                                                   #
# Universià degli Studi di Perugia                  #
# Corso di Metodi Computazionali per la Fisica      #
#---------------------------------------------------#
# Esercitazione 4 - Numpy, Pandas, Matplotlib:      #
#                                                   #
#   Lettura File CSV (nella sottocartella dati)     #
#   + prduzione grafici curva di  luce              #
#                                                   #
#####################################################

import sys,os
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


################################### Dati Input  ##########################################
# Lettura file 
kplr1 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2026/refs/heads/main/dati/moduli_scientifici/kplr010666592-2011240104155_slc.csv'
#kplr1 = 'dati/kplr010666592-2011240104155_slc.csv'

kplrdf = pd.read_csv(kplr1)

print('Columns:', kplrdf.columns)
#print(lcdf)


# ------------- Colonne usate per i grafici ----------------------------------------------
#  TIME           : BJD - 2454833 --> barycenter corrected JD
#  PDCSAP_FLUX    : e-/s          --> Pre-search Data Conditioning (PDC)
#                                      aperture photometry flux, (electrons per second) 
#  PDCSAP_FLUX_ERR: e-/s          --> PDC aperture photometry flux error
#-----------------------------------------------------------------------------------------


#############################  Grafici senza errori  #####################################


## grafico Flusso vs. Tempo
plt.subplots(figsize=(12,6))
plt.plot(kplrdf['TIME'], kplrdf['PDCSAP_FLUX'] )
plt.xlabel('Time (BJD - 2454833)', fontsize=14)
plt.ylabel(r'Flux ($e^-/s$)', fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()


## grafico Flusso vs. Tempo con simbolo (no linea)
plt.subplots(figsize=(12,6))
plt.plot(kplrdf['TIME'], kplrdf['PDCSAP_FLUX'], 'o')
plt.xlabel('Time (BJD - 2454833)', fontsize=14)
plt.ylabel(r'Flux ($e^-/s$)',      fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()



#############################  Grafici con  errori  #####################################

## grafico Flusso vs. Tempo salvato come png e pdf
plt.subplots(figsize=(12,6))
plt.errorbar(kplrdf['TIME'], kplrdf['PDCSAP_FLUX'], yerr=kplrdf['PDCSAP_FLUX_ERR'], fmt='.' )
plt.xlabel('Time (BJD - 2454833)', fontsize=14)
plt.ylabel(r'Flux ($e^-/s$)',      fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.savefig('curva_luce.png')
plt.savefig('curva_luce.pdf')
plt.show()




## Zoom grafico Flusso vs. Tempo salvato come png e pdf
plt.subplots(figsize=(12,6))
plt.errorbar(      kplrdf.loc[ (kplrdf['TIME']> 947.9) & (kplrdf['TIME']< 948.35), 'TIME'],
                   kplrdf.loc[ (kplrdf['TIME']> 947.9) & (kplrdf['TIME']< 948.35), 'PDCSAP_FLUX'],
              yerr=kplrdf.loc[ (kplrdf['TIME']> 947.9) & (kplrdf['TIME']< 948.35), 'PDCSAP_FLUX_ERR'], fmt='.',  color='royalblue')

plt.xlabel('Time (BJD - 2454833)', fontsize=14)
plt.ylabel(r'Flux ($e^-/s$)',      fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.savefig('curva_luce_zoom.png')
plt.savefig('curva_luce_zoom.pdf')
plt.show()




## grafico Flusso vs. Tempo con riquadro, salvato come png e pdf 
fig, ax = plt.subplots(figsize=(12,6))
plt.errorbar(kplrdf['TIME'], kplrdf['PDCSAP_FLUX'], yerr=kplrdf['PDCSAP_FLUX_ERR'], fmt='.', color='cornflowerblue' )
plt.xlabel('Time (BJD - 2454833)', fontsize=14)
plt.ylabel(r'Flux ($e^-/s$)',      fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ylim(1.012e6, 1.030e6)

# creo inset 
ins_ax = ax.inset_axes([.65, .62, .32, .32])  # [x, y, width, height] w.r.t. ax
ins_ax.errorbar(      kplrdf.loc[ (kplrdf['TIME']> 947.9) & (kplrdf['TIME']< 948.35), 'TIME'],
                      kplrdf.loc[ (kplrdf['TIME']> 947.9) & (kplrdf['TIME']< 948.35), 'PDCSAP_FLUX'],
                 yerr=kplrdf.loc[ (kplrdf['TIME']> 947.9) & (kplrdf['TIME']< 948.35), 'PDCSAP_FLUX_ERR'], fmt='.',  color='royalblue')


# salvataggio su file
plt.savefig('curva_luce_inset.png')
plt.savefig('curva_luce_inset.pdf')

plt.show()





