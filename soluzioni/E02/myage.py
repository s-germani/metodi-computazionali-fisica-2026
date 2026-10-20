#####################################################
# S. Germani (stefano.germani@unipg.it)             #
#                                                   #
# Universià degli Studi di Perugia                  #
# Corso di Metodi Computazionali per la Fisica      #
#---------------------------------------------------#
# Esercitazione 2 - Le Basi di Python:              #
#                                                   #
#   Calcolo età in anni, gioni e secondi            #
#                                                   #
#####################################################

import sys,os
from datetime import datetime, timedelta


# Richiesta data di nascita 
print('Questo programma calcola la vostra età in anni, giorni e secondi')
mybirthday = input('Immettere la data di nascita (d-m-y): ')
# definisco data da stringa formattata giorno-mese-anno
mybdaydate = datetime.strptime(mybirthday, "%d-%m-%Y")

# data e ora attuale
datenow = datetime.now()
print('La data attuale è: {:d}-{:d}-{:d}'.format( datenow.day, datenow.month, datenow.year))

# calcolo direttamente dfferenza in anni
age_years = datenow.year - mybdaydate.year
if datenow.month < mybdaydate.month or ( datenow.month == mybdaydate.month and datenow.day < mybdaydate.day):
    age_years-=1


# calcolo differenza temporale con datetime
datediff = datenow - mybdaydate

# differenza temporale in secondi 
datediff_sec = datediff.total_seconds()

# età in secondi
age_secs  = int( datediff_sec )

# età in ore
age_hours = int( datediff_sec / (60 * 60) )



# stampa risultati 
print('-------------------------------------------------------')
print('  Data di nascita  {:02d}-{:02d}-{:d}'.format( mybdaydate.day, mybdaydate.month, mybdaydate.year))
print('  Data attuale     {:02d}-{:02d}-{:d}'.format( datenow.day,    datenow.month,    datenow.year))
print()
print('  Età    [anni]: {:>12d}'.format(age_years))
print('  Età     [ore]: {:>12d} - {:>6d} khr'.format(age_hours, int(age_hours/1000)))
print('  Età [secondi]: {:>12d} - {:>6d} Ms'.format(age_secs,   int(age_secs/1e6)  ))
print('-------------------------------------------------------')
