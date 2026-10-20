#####################################################
# S. Germani (stefano.germani@unipg.it)             #
#                                                   #
# Universià degli Studi di Perugia                  #
# Corso di Metodi Computazionali per la Fisica      #
#---------------------------------------------------#
# Esercitazione 2 - Le Basi di Python:              #
#                                                   #
#   Liste e Dizionari                               #
#                                                   #
#####################################################


# Lista con giorni della settimana
week = ['Lunedì', 'Martedì', 'Mercoledì', 'Giovedì', 'Venerdì', 'Sabato', 'Domenica']

print(week)


# Lista con gioni della settimana nel mese di ottobre 2025
ottobre = week[3:]+week*3+week[:6]

print(ottobre)


# Dizionario ottobre 2025 per giorno del mese e della settimana (metodo base)
dict_ottobre = {}
for i in range(len(ottobre)):
    dict_ottobre.update({ i+1: ottobre[i] })

print()
print('Dizionario metodo base', dict_ottobre)



# Dizionario ottobre 2026 per giorno del mese e della settimana (metodo con list comprehension)
dict_ottobre_lc = { i+1 : ottobre[i] for i in range(len(ottobre)) }

print()
print('Dizionario da list comprehension',  dict_ottobre_lc)




# Stampa a schermo dizionario
print('\n=======================================================')
print('================= Ottobre 2025 ========================')
print('=======================================================')
for k in dict_ottobre_lc:

    print('||{:5d}{:.>36}{:>12}'.format(k, dict_ottobre_lc[k], '||') )
print('=======================================================')
      
