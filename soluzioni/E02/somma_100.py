#####################################################
# S. Germani (stefano.germani@unipg.it)             #
#                                                   #
# Universià degli Studi di Perugia                  #
# Corso di Metodi Computazionali per la Fisica      #
#---------------------------------------------------#
# Esercitazione 2 - Le Basi di Python:              #
#                                                   #
#   Somma primi 100 numeri naturali                 #
#                                                   #
#####################################################

import sys,os


nmax = 100

somma = 0

for n in range(1,nmax+1):
    
    somma = somma + n

    #print( n, 'somma temporanea:', somma)


print('La somma dei primi 100 numeri naturali è:', somma)

