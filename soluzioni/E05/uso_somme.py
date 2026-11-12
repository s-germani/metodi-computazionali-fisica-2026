#####################################################
# S. Germani (stefano.germani@unipg.it)             #
#                                                   #
# Universià degli Studi di Perugia                  #
# Corso di Metodi Computazionali per la Fisica      #
#---------------------------------------------------#
# Esercitazione 5 - Funzioni Moduli e Classi:       #
#                                                   #
#   Utilizzo e test del modulo somme                #
#                                                   #
#####################################################

import somme


print('Utilizzo modulo somme ...')

#print(somme.somma_n.__doc__)
sn = somme.somma_n(10)
print('somma_n(10)', sn)


#print(somme.somma_sqrtn.__doc__)
sr = somme.somma_sqrtn(10)
print('somma_sqrtn(10)',sr)


#print(somme.sommaprod_n.__doc__)
sp = somme.sommaprod_n(10)
print('sommaprod_n(10)', sp)


#print(somme.sommaexp_n.__doc__)
sea1 = somme.sommaexp_n(10)
print('sommaexp_n(10)', sea1)

sea3 = somme.sommaexp_n(10, alpha=3)
print('sommaexp_n(10, alpha=3)', sea3)
