#####################################################
# S. Germani (stefano.germani@unipg.it)             #
#                                                   #
# Universià degli Studi di Perugia                  #
# Corso di Metodi Computazionali per la Fisica      #
#---------------------------------------------------#
#                                                   #
#    Esempio utilizzo modulo argparse               #
#                                                   #
#####################################################

import sys,os
import argparse


def parse_arguments():
    
    parser = argparse.ArgumentParser(description='Esempio utilizzo argarse.',
                                     usage      ='python3 argparse_example.py  --opzione')
    parser.add_argument('-b', '--opzione1',    action='store_true',                     help='Esempio di opzione booleana')
    parser.add_argument('-v', '--opzione2',    action='store',                          help='Esempio di opzione con valore')
    parser.add_argument('-d', '--opzione3',    action='store',  type=int,  default=10,  help='Esempio di opzione con valore tipo e default')
    return  parser.parse_args()


def main():

    args = parse_arguments()

    # print 
    #print(args)

    if args.opzione1 == True:
        print('---------------------------------------------')
        print('   Opzione 1 = True')
        print('---------------------------------------------')

    if args.opzione2 != None:
        print('---------------------------------------------')
        print('   Valore Opzione2:', args.opzione2)
        print('---------------------------------------------')


    if args.opzione3 > 100:
        print('---------------------------------------------')
        print('   Valore Opzione3 > 100:')
        print('---------------------------------------------')



if __name__ == "__main__":

    main()
