import os
import time
import json
import csv
import random
os.system('cls')

def cargarDatos():
    with open('empleados.csv', 'r', newline='', encoding='utf-8') as archivoEmpleados:
        empleados = list(csv.DictReader(archivoEmpleados))
    with open('datos.json', 'r', encoding='utf-8') as archivoDATOS:
        dato = json.load(archivoDATOS)
        unidades = dato['unidad']
        cargos = dato['cargo']
    return empleados, unidades, cargos

def asignarSueldo(empleados):
    for empleado in empleados:
        empleado['sueldo_bruto'] = random.choice(range(500_000, 2_500_000, 1_000))
        print(empleado)

def listarMayorMenorSueldo(empleados):
    mayorSueldo = {'id_empleado':None, 'nombre':None, 'sueldo':0}
    menorSueldo = {'id_empleado':None, 'nombre':None, 'sueldo':2_500_000}
    for empleado in empleados:
        sueldo = int(empleado['sueldo_bruto'])
        if sueldo > mayorSueldo['sueldo']:
            mayorSueldo['id_empleado'] = empleado['id_empleado']
            mayorSueldo['nombre'] = empleado['nombre']
            mayorSueldo['sueldo'] = empleado['sueldo_bruto']
        if sueldo < menorSueldo['sueldo']:
            menorSueldo['id_empleado'] = empleado['id_empleado']
            menorSueldo['nombre'] = empleado['nombre']
            menorSueldo['sueldo'] = empleado['sueldo_bruto']
    print(f'El Mayor sueldo de los empleados es: {mayorSueldo}')
    print(f'El Menor sueldo de los empleados es: {menorSueldo}')
    return mayorSueldo, menorSueldo

def filtrarUsuarioPorDepartamento(empleados, unidades, cargos, indexArea):  
    for unidad in unidades:
        if indexArea == unidad['id_departamento']:
            for cargo in cargos:
                if cargo['unidad_id_unidad'] == unidad['id_departamento']:
                    for empleado in empleados:
                        if int(empleado['cargo_idcargo']) == cargo['idcargo']:
                            print(f'ID: {empleado['id_empleado']}\nNombre: {empleado['nombre']}\nCargo: {cargo['nombreCargo']}\nDepartamento: {unidad['nombreDepartamento']}')
                            print()

def filtrarUsuarioPorCargo(empleados, unidades, cargos, indexCargo):
    for cargo in cargos:
        if indexCargo == cargo['idcargo']:
            for empleado in empleados:
                if int(empleado['cargo_idcargo']) == cargo['idcargo']:
                    for unidad in unidades:
                        if unidad['id_departamento'] == cargo['unidad_id_unidad']:
                            print(f'ID: {empleado['id_empleado']}\nNombre: {empleado['nombre']}\nDepartamento: {unidad['nombreDepartamento']}\nCargo: {cargo['nombreCargo']}')
                            print()
def menuGeneral():
    print('-------- MENU GENERAL -------')
    print('[1] Asignar Sueldos Aleatorios')
    print('[2] Listar Mayor Menor Sueldo')
    print('[3] Filtrar Usuario por Departamento')
    print('[4] Filtrar Usario por Cargo')
    print('[5] Calculo Sueldo Mensual')
    print('[6] Salir')

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
    empleados, unidades, cargos = cargarDatos()
    menu = True
    while menu:
        menuGeneral()
        opc1 = 0
        try:
            opc1 = int(input('\nIngrese una opción: '))
            if opc1 < 1 or opc1 > 6:
                errorRango()
            else:
                if opc1 == 1:
                    asignarSueldo(empleados)
                elif opc1 == 2:
                    listarMayorMenorSueldo(empleados)
                elif opc1 == 3:
                    print('\nIngrese el ID del Departamento: ')
                    index = 1
                    for unidad in unidades:
                        print(f'[{index}] {unidad['nombreDepartamento']}')
                        index += 1
                    try:
                        indexArea = int(input('Ingrese una opcion: '))
                    except:
                        errorLetra()
                    filtrarUsuarioPorDepartamento(empleados, unidades, cargos, indexArea)
                elif opc1 == 4:
                    print('\nIngrese el ID del cargo que desea consultar: ')
                    index = 1
                    for cargo in cargos:
                        print(f'[{index}] {cargo['nombreCargo']}')
                        index += 1
                    try:
                        indexCargo = int(input('Ingrese una opcion: '))
                    except:
                        errorLetra()
                    filtrarUsuarioPorCargo(empleados, unidades, cargos, indexCargo)  
                elif opc1 == 5:
                    input('Opcion 5') 
                elif opc1 == 6:
                    limpiar()
                    print('<<< ¡Hasta Pronto! >>>')
                    display()
                    limpiar()
                    menu = False
        except:
            errorLetra()
            display()
            limpiar()
if __name__ == '__main__':
    main()
