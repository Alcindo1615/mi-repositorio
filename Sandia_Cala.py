import os
import time
import json
import csv
import random
os.system('cls')


def conexLeerCargos():
    with open('cargos.json', 'r', encoding='utf-8') as archivoCargos:
        cargos = json.load(archivoCargos)
    return cargos

def conexLeerEmpleados():
    with open('empleados.json', 'r', encoding='utf-8') as archivoEmpleados:
        empleados = json.load(archivoEmpleados)
    return empleados

def conexGuardar(empleados):
    with open('empleados.json', 'w', encoding='utf-8') as archivoGuardar:
        json.dump(empleados, archivoGuardar, ensure_ascii=False, indent=4)

def crearCSV(empleados):
    with open('MI_ARCHIVO.csv', 'w',newline='\n', encoding='utf-8') as archivoCSV:
        escribir = csv.writer(archivoCSV)
        escribir.writerow(empleados[0].keys())
        for empleado in empleados:
            escribir.writerow([empleado['id_empleado'], empleado['nombre'], empleado['apellido'], empleado['edad'], empleado['sueldo_base'], empleado['id_cargo']])
    
def registraUsuario(cargos):
    id = 1_000_000
    id_empleado = id+1
    id += 1
    nombre = input('Ingrese el nuevo nombre Usuario: ')
    apellido = input('Ingrese el apellido del Usuario: ')
    edad = random.choice(range(22, 45))
    cargo = random.choice(cargos)
    id_cargo = cargo['id_cargo']
    if id_cargo == 'C1':
        sueldo_base = random.choice(range(2_000_000, 3_000_000, 1000))
    elif id_cargo == 'C2':
        sueldo_base = random.choice(range(800_000, 2_000_000, 1000))
    empleado = {
        "id_empleado": id_empleado,
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "sueldo_base": sueldo_base,
        "id_cargo": id_cargo
    }
    empleados = conexLeerEmpleados()
    empleados.append(empleado)
    conexGuardar(empleados)

def buscarUsuario():
    id_empleado = input('Ingrese el id del empleado a buscar: ')
    empleados = conexLeerEmpleados()
    for empleado in empleados:
        if empleado['id_empleado'] == id_empleado:
            print(empleado)

def editarUsuario():
    id_empleado = int(input('Ingrese el id del empleado que desea editar: '))
    empleados = conexLeerEmpleados()
    for empleado in empleados:
        if empleado['id_empleado'] == id_empleado:
            menu1 = True
            while menu1:
                print('[1] Nombre')
                print('[2] Apellido')
                print('[3] Edad')
                print('[4] id_cargo')
                print('[5] Sueldo Base')
                print('[6] Guardar y Salir')
                opc1 = 0
                try:
                    opc1 = int(input('Ingrese una opcion: '))
                    if opc1 < 1 or opc1 > 6:
                        errorRango()
                    else:
                        if opc1 == 1:
                            empleado['nombre'] = input('Ingrese el nuevo nombre: ')
                        
                        elif opc1 == 2:
                            empleado['apellido'] = input('Ingrese el nuevo apellido: ')
                        
                        elif opc1 == 3:
                            empleado['edad'] = input('Ingrese el nuevo edad: ')
                        
                        elif opc1 == 4:
                            empleado['id_cargo'] = input('Ingrese el nuevo id_cargo: ')
                        
                        elif opc1 == 5:
                            empleado['sueldo_base'] = input('Ingrese el nuevo Suedo: ')
                        
                        elif opc1 == 6:
                            print('Saliendo...')
                            time.sleep(2)
                            limpiar()
                            menu1 = False
                except:
                    errorLetra()
            conexGuardar(empleados)

def eliminarUsuario():
    id_empleado = int(input('Ingrese el id del empleado que desea eliminar: '))
    empleados = conexLeerEmpleados()
    for empleado in empleados:
        if empleado['id_empleado'] == id_empleado:
            empleados.remove(empleado)
    """ print('Empleado eliminado exitosamente')
    time.sleep(2) """
    conexGuardar(empleados)

def listarUsuarios():
    empleados = conexLeerEmpleados()
    for empleado in empleados:
        print(empleado)
    crearCSV(empleados)

def menuGeneral():
    print('------- MENU GENERAL -------')
    print('[1] Registra Usuario')
    print('[2] Buscar Usuario')
    print('[3] Editar Usuario')
    print('[4] Eliminar Usuario')
    print('[5] Listar Usuarios y exportar avCSV')
    print('[6] Salir del Programa\n')


def limpiar():
    os.system('cls')
def errorLetra():
    print('\n**** LA OPCION DEBE SER NUMERICA ****')
    time.sleep(1.5)
    limpiar()
def errorRango():
    print('\n**** LA OPCION ESTA FUERA DE RANGO ****')
    time.sleep(1.5)
    limpiar()

    

def main():
    cargos = conexLeerCargos()
    menu1 = True
    while menu1:
        menuGeneral()
        opc1 = 0
        try:
            opc1 = int(input('INGRESE UNA OPCION: '))
            if opc1 < 1 or opc1 > 6:
                errorRango()
            else:
                if opc1 == 1:
                    registraUsuario(cargos)
                elif opc1 == 2:
                    buscarUsuario()
                elif opc1 == 3:
                    editarUsuario()
                elif opc1 == 4:
                   eliminarUsuario()
                elif opc1 == 5:
                    listarUsuarios()
                
                elif opc1 == 6:
                    limpiar()
                    print('>>>> ¡HASTA PRONTO! <<<<')
                    time.sleep(1.5)
                    limpiar()
                    menu1 = False
        except:
            errorLetra()
if __name__ == '__main__':
    main()
        