#####################################################
# S. Germani (stefano.germani@unipg.it)             #
#                                                   #
# Universià degli Studi di Perugia                  #
# Corso di Metodi Computazionali per la Fisica      #
#---------------------------------------------------#
# Esercitazione 4 - Numpy, Pandas, Matplotlib:      #
#                                                   #
#   Lettura File CSV (nella sottocartella dati)     #
#   + prduzione scatter                             #
#   + prduzione scatter plot e istogrammi           #
#     in immagine con più riquqdri                  #
#                                                   #
#####################################################

import sys,os
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


################################### Dati Input  ##########################################
## Lettura file
exofile = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2025/refs/heads/main/dati/moduli_scientifici/ExoplanetsPars_2026.csv'
#exofile = 'ExoplanetsPars_2025.csv'
exodf   = pd.read_csv(exofile, comment='#')   

## Stampa nomi Colonne 
print('Columns:', exodf.columns)
#print(lcdf)


###################################  Parametri Pianeti Sistema Solare  ##################

ss_orbper  = np.array( [ 88, 225, 365, 687, 4333, 10759, 30687, 60190])
ss_orbsmax = np.array( [ 0.47, 0.73, 1.02, 1.67, 5.45, 10.07, 20.09, 30.32])

ss_bmasse = np.array( [ 0.06, 0.82, 1.0, 0.11, 317.89,  95.17, 14.56, 17.24, ] )
ss_bmassj = ss_bmasse/317.89



###################################  Scatter Plot ######################################

## Scatter plot Periodo vs. Massa
fig, ax = plt.subplots(figsize=(12,6))
plt.scatter(exodf['pl_orbper'], exodf['pl_bmassj'], alpha=0.3, color='gold',      label='Exoplanets')
plt.scatter(ss_orbper,          ss_bmassj,                     color='slategray', label='Solar System')
plt.xlabel('Period [days]',         fontsize=16)
plt.ylabel(r'Planet Mass [$m_J$]',  fontsize=16)
plt.xscale('log')
plt.yscale('log')
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend(fontsize=16)
plt.savefig('Exoplanets_ScatterPlot.pdf')
plt.savefig('Exoplanets_ScatterPlot.png')
plt.show()



fig, ax = plt.subplots(figsize=(12,6))
plt.scatter(exodf['pl_orbper'],(exodf['pl_orbsmax']**2)/exodf['st_mass'], alpha=0.3, color='gold', label='Exoplanets')
plt.scatter(ss_orbper, ss_orbsmax**2, color='slategray', label='Solar System')
plt.xlabel('Period [days]',                        fontsize=16)
plt.ylabel(r'$R_{max}^2/m_{\star}$ [$m_{\odot}^2/days$]',  fontsize=16)
plt.xscale('log')
plt.yscale('log')
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend(fontsize=14)
plt.savefig('Exoplanets_ScatterPlot_StMass.pdf')
plt.savefig('Exoplanets_ScatterPlot_StMass.png')
plt.show()



###################################  Scatter Plot con Selezione #######################
## grafico Flusso vs. Tempo 
fig, ax = plt.subplots(figsize=(12,6))
plt.scatter( exodf.loc[exodf['discoverymethod']=='Transit', 'pl_orbper'],
             exodf.loc[exodf['discoverymethod']=='Transit', 'pl_bmassj'],         alpha=0.3, label='Transit')
plt.scatter( exodf.loc[exodf['discoverymethod']=='Radial Velocity', 'pl_orbper'],
             exodf.loc[exodf['discoverymethod']=='Radial Velocity', 'pl_bmassj'], alpha=0.3, label='Radial Velocity')
plt.scatter(ss_orbper, ss_bmassj, color='slategray', label='Solar System')
plt.xlabel('Period [days]',         fontsize=16)
plt.ylabel(r'Planet Mass [$m_J$]',  fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

plt.xscale('log')
plt.yscale('log')
plt.legend(fontsize=14)
plt.savefig('Exoplanets_ScatterPlot_Selezione.pdf')
plt.savefig('Exoplanets_ScatterPlot_Selezione.png')
plt.show()






#############################  Scatter plot con istogrammi   ###########################

# Creo riquadro figura
fig = plt.figure(figsize=(12,11))

# creo griglia 2x2 per subplot con asse X in comune per le colonne e asse Y inb comune per le righe 
gs = fig.add_gridspec(2, 2, hspace=0, wspace=0)
ax = gs.subplots( sharex='col', sharey='row')

ax[1,0].scatter( np.log10(exodf.loc[exodf['discoverymethod']=='Transit',         'pl_orbper']),
                 np.log10(exodf.loc[exodf['discoverymethod']=='Transit',         'pl_bmassj']), color='limegreen',  alpha=0.3, label='Transit')
ax[1,0].scatter( np.log10(exodf.loc[exodf['discoverymethod']=='Radial Velocity', 'pl_orbper']),
                 np.log10(exodf.loc[exodf['discoverymethod']=='Radial Velocity', 'pl_bmassj']), color='darkorange', alpha=0.3, label='Radial Velocity')
ax[1,0].scatter(np.log10(ss_orbper), np.log10(ss_bmassj), color='slategray', label='Solar System')

ax[1,0].tick_params(axis='both', which='major', labelsize=14)
ax[1,0].set_xlabel('log(Period [days])',         fontsize=16)
ax[1,0].set_ylabel(r'log(Planet Mass [$m_J$])',  fontsize=16)
ax[1,0].legend(fontsize=16)


# Istogramma Periodo
ax[0,0].hist( np.log10(exodf.loc[exodf['discoverymethod']=='Transit', 'pl_orbper']),
              bins=50, range=(-2, 5), color='limegreen',  alpha=0.5, label='Transit')

ax[0,0].hist( np.log10(exodf.loc[exodf['discoverymethod']=='Radial Velocity', 'pl_orbper']),
              bins=50, range=(-2, 5), color='darkorange',  alpha=0.5, label='Radial Velocity')
ax[0,0].tick_params(axis='both', which='major', labelsize=14)
ax[0,0].set_ylabel(r'Number of planets',        fontsize=16)
ax[0,0].legend(fontsize=16)


# Istogramma Massa pianeta
ax[1,1].hist( np.log10(exodf.loc[exodf['discoverymethod']=='Transit', 'pl_bmassj']),
              bins=50, range=(-4, 4), color='limegreen',  alpha=0.5, orientation='horizontal', label='Transit')

ax[1,1].hist( np.log10(exodf.loc[exodf['discoverymethod']=='Radial Velocity', 'pl_bmassj']),
              bins=50, range=(-4, 4), color='darkorange',  alpha=0.5, orientation='horizontal', label='Radial Velocity')

ax[1,1].tick_params(axis='both', which='major', labelsize=14)
ax[1,1].set_xlabel( 'Number of planets',        fontsize=16)
ax[1,1].legend(fontsize=16)

# Rimuovo assi per riquadro non necessario
ax[0,1].axis('off')

plt.savefig('Exoplanets_Period_vs_Mass_Detection.pdf')
plt.savefig('Exoplanets_Period_vs_Mass_Detection.png')
plt.show()
