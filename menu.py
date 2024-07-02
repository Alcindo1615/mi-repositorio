import os
import time
import json
import csv
import random
os.system('cls')




def menuGeneral():
    print('-------- MENU GENERAL -------')
    print('[1] ------')
    print('[2] ------')
    print('[3] ------')
    print('[4] ------')
    print('[5] ------')

def limpiar():
    os.system('cls')

def display():
    time.sleep(1.5)

def errorLetra():
    print('*** La opción debe ser númerica ***')
    display()
    limpiar()

def errorRango():
    print('*** La opción esta fuera de rango ***')
    display()
    limpiar()

def main():
    menu = True
    while menu:
        menuGeneral()
        opc1 = 0
        try:
            opc1 = int(input('\nIngrese una opción: '))
            if opc1 < 1 or opc1 > 5:
                errorRango()
            else:
                if opc1 == 1:
                    input('Opcion 1')
                elif opc1 == 2:
                    input('Opcion 2')
                elif opc1 == 3:
                    input('Opcion 3')
                elif opc1 == 4:
                    input('Opcion 4')   
                elif opc1 == 5:
                    limpiar()
                    print('<<< ¡Hasta Pronto! >>>')
                    display()
                    limpiar()
                    menu = False
        except:
            errorLetra()
if __name__ == '__main__':
    main()