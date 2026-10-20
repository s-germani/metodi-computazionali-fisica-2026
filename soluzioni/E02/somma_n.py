#####################################################
# S. Germani (stefano.germani@unipg.it)             #
#                                                   #
# Universià degli Studi di Perugia                  #
# Corso di Metodi Computazionali per la Fisica      #
#---------------------------------------------------#
# Esercitazione 2 - Le Basi di Python:              #
#                                                   #
#   Somma primi N numeri naturali a scelta          #
#                                                   #
#####################################################

import sys,os


# Richiesta numero per somma
print('Questo programma calcola la somma dei primi N numeri naturali')
Nin = input('Immettere il valore di N: ')

# converto input in intero
nmax = int(Nin)

somma = 0

for n in range(1,nmax+1):
    
    somma = somma + n

    #print( n, 'somma temporanea:', somma)


print('-----------------------------------------------------------')
print('La somma dei primi {:d} numeri naturali è: {:d}'.format(nmax, somma))
print('-----------------------------------------------------------')

