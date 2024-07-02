import os
import time
import json
import csv
import random
os.system('cls')

def cargarDatos():
    with open('empleados.json', 'r', encoding='utf-8') as archivoEmpleados:
        empleados = json.load(archivoEmpleados)
    with open('tiendas.json', 'r', encoding='utf-8') as archivoTiendas:
        tiendas = json.load(archivoTiendas)
    with open('ventas.json', 'r', encoding='utf-8') as archivoVentas:
        ventas = json.load(archivoVentas)
    return empleados, tiendas, ventas 

def guardarDatos(ventas):
    with open('MIVENTA.json', 'w', encoding='utf-8') as guardar:
        json.dump(ventas, guardar, indent=4)

def guardarVenta(ventas):
    with open('ventas.json', 'w', encoding='utf-8') as archivo_guardar:
        json.dump(ventas, archivo_guardar, indent=4)

def crearCSV(estadisticas):
    with open('ESTADISTICA.csv', 'w', newline='\n', encoding='utf-8') as archivo_csv:
        escribir =  csv.writer(archivo_csv)
        escribir.writerow(estadisticas)
        escribir.writerow([estadisticas['total ventas realizada'], estadisticas['venta mayor'], estadisticas['promedio venta']])


def idVenta(ventas):
    id_venta = 0
    for venta in ventas['ventas']:
        if int(venta['id_venta']) > id_venta:
            id_venta = int(venta['id_venta'])
    return id_venta

def precargarVenta(empleados, ventas):
    id_venta = idVenta(ventas)
    for i in range(100):
        id_venta += 1
        empleado = random.choice(empleados)
        id_empleado = empleado['id_vendedor']
        tienda = random.choice(range(100))
        mes = 'junio'
        total_venta = random.choice(range(50_000, 200_000, 100))
        nuevaVenta = {
            "id_venta": id_venta,
            "empleado": id_empleado,
			"id_tienda": tienda,
            "mes": mes,
            "total_venta": total_venta
        }
        ventas['ventas'].append(nuevaVenta)
    print(ventas)
    guardarDatos(ventas)
    input()

def crearVenta(empleados, ventas, tiendas):
    id_venta = idVenta(ventas)
    for empleado in empleados:
        print(f'ID: {empleado['id_vendedor']} -->> {empleado['nombre']} {empleado['apellido']}')
    print('------'*7)
    id_empleado = input('Ingrese el ID del empleado que realiza la venta: ')
    print('------'*7)
    id_venta += 1
    index = 1
    for tienda in tiendas:
        print(f'[{index}] {tienda['nombre']}')
        index += 1
    id_tienda = int(input('Ingrese le tipo de tienda: '))
    mes = 'junio'
    print('------'*7)
    total_venta = int(input('Ingrese el monto de la venta: '))

    nuevaVenta = {
        "id_venta": id_venta,
        "empleado": id_empleado,
        "id_tienda": id_tienda,
        "mes": mes,
        "total_venta": total_venta
    }
    ventas['ventas'].append(nuevaVenta)
    print(ventas)
    guardarVenta(ventas)

def reporteSueldo(empleados,ventas):
    for empleado in empleados:
        tota_venta = 0
        bono = 0
        salud = int(empleado['sueldo_base']*0.07)
        afp = int(empleado['sueldo_base']*0.12)

        for venta in ventas['ventas']:
            if venta['empleado'] == empleado['id_vendedor']:
                tota_venta =  tota_venta + venta['total_venta']
        if tota_venta >= 20_000_000:
            bono = int(venta['total_venta']*0.02)
        elif tota_venta >= 10_000_000:
            bono = int(venta['total_venta']*0.01)
        elif tota_venta >= 5_000_000:
            bono = int(venta['total_venta']*0.005)
        sueldoLiquido = (empleado['sueldo_base']-salud-afp) + bono
        print(f'Nombre: {empleado['nombre']} {empleado['apellido']} | Sueldo Base: {empleado['sueldo_base']} | Bono: {bono} | Desc. Salud: {salud} | Desc. AFP: {afp} | Sueldo Liquido: ${sueldoLiquido}')

def estadisticas(ventas):
    total_ventas = sum(venta['total_venta'] for venta in ventas['ventas'])
    venta_mayor = max(venta['total_venta'] for venta in ventas['ventas'])
    promedio_venta = int(total_ventas/len(ventas['ventas']))
    #print(total_ventas, venta_mayor, promedio_venta)
    
    estadisticas = {
        'total ventas realizada':total_ventas,
        'venta mayor':venta_mayor,
        'promedio venta':promedio_venta
    }
    crearCSV(estadisticas)

    with open('VEHICULO.txt', 'w', encoding='utf-8') as archivotxt:
        archivotxt.write(f'total ventas realizada: {total_ventas}\n')
        archivotxt.write(f'venta mayor: {venta_mayor}\n')
        archivotxt.write(f'promedio venta: {promedio_venta}\n')
    

def menuGeneral():
    print('-------- MENU GENERAL -------')
    print('[1] Precargar ventas y guardar ventas.json')
    print('[2] Crear nuevas ventas')
    print('[3] Reporte de sueldos')
    print('[4] Ver estadisticas por tienda')
    print('[5] Salir')

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
    empleados, tiendas, ventas = cargarDatos()
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
                    precargarVenta(empleados, ventas)
                    idVenta(ventas)
                elif opc1 == 2:
                    crearVenta(empleados, ventas, tiendas)
                elif opc1 == 3:
                    reporteSueldo(empleados,ventas)
                elif opc1 == 4:
                    estadisticas(ventas)   
                elif opc1 == 5:
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