import os
import time
import json
import csv
import random
os.system('cls')

def cargarDAtos():
    with open('empleados.json', 'r', encoding='utf-8') as archivo_empleados:
        empleados = json.load(archivo_empleados)
    with open('cargos.json', 'r', encoding='utf-8') as archivo_cargos:
        cargos = json.load(archivo_cargos)
    with open('ventas.json', 'r', encoding='utf-8') as archivo_ventas:
        ventas = json.load(archivo_ventas)
    return empleados, cargos, ventas

def guardarVenta(ventas):
    with open('ventas.json', 'w', encoding='utf-8') as archivoGuardar:
        json.dump(ventas, archivoGuardar, indent=4)

def guardarCSV(estadisticas):
    with open('VENTAS.csv', 'w', newline='\n', encoding='utf-8') as archivoCSV:
        escribir = csv.writer(archivoCSV)
        escribir.writerow(estadisticas)
        escribir.writerow([estadisticas['venta maxima'], estadisticas['venta minima'], estadisticas['promedio venta']])

def guardaaTXT(estadisticas):
    with open('VENTAS.txt', 'w') as archivoTXT:
        archivoTXT.write(f'venta maxima: {estadisticas['venta maxima']}\n')
        archivoTXT.write(f'venta minima: {estadisticas['venta minima']}\n')
        archivoTXT.write(f'promedio venta: {estadisticas['promedio venta']}\n')

def idVenta(ventas):
    id_venta = 0
    for venta in ventas['ventas']:
        if int(venta['id_venta']) > id_venta:
            id_venta = int(venta['id_venta'])
    return id_venta

def precargarVenta(empleados, ventas):
    id_venta = idVenta(ventas)
    for i in range(50):
        id_venta += 1
        empleado = random.choice(empleados)
        id_empleado = empleado['id_empleado']
        fecha = '22/22/24'
        total_venta = random.choice(range(30_000, 70_000, 100))
        propina = int(total_venta*0.1)
        nuevaVenta = {
            "id_venta": id_venta,
            "empleado": id_empleado,
            "fecha": fecha,
            "total_venta": total_venta,
            "propina": propina
        }
        ventas['ventas'].append(nuevaVenta)
    print(ventas)
    print('\nVentas Precargadas con exito')
    display()

def crearVenta(empleados, ventas):
    id_venta = idVenta(ventas)
    for empleado in empleados:
        print(f'ID: {empleado['id_empleado']} -->> Nombre: {empleado['nombre']} {empleado['apellido']}')
    print('---'*7)
    id_venta += 1
    id_empleado = input('Ingrse el  ID del empleado que desea realizar la venta: ')
    fecha = '22/22/24'
    total_venta = int(input('Ingrese el monto de la venta: '))
    propina = int(total_venta*0.1)
    nuevaVenta = {
        "id_venta": id_venta,
        "empleado": id_empleado,
        "fecha": fecha,
        "total_venta": total_venta,
        "propina": propina
    }
    ventas['ventas'].append(nuevaVenta)
    guardarVenta(ventas)

def reporteSueldo(empleados, ventas):
    for empleado in empleados:
        tota_venta = 0
        propina = 0
        bono = 0
        salud = int(empleado['sueldo_base']*0.07)
        afp = int(empleado['sueldo_base']*0.12)
        for venta in ventas['ventas']:
            if venta['empleado'] == empleado['id_empleado']:
                tota_venta = tota_venta + venta['total_venta']
                propina = propina + venta['propina']
        if tota_venta >= 2_000_000:
            bono = int(empleado['sueldo_base']*0.05)
        elif tota_venta >= 1_000_000:
            bono = int(empleado['sueldo_base']*0.02)
        elif tota_venta >= 500_000:
            bono = int(empleado['sueldo_base']*0.01)
        sueldoLiquido = int(empleado['sueldo_base']-salud-afp) + propina + bono

        print(f'Empleado: {empleado['nombre']} | Sueldo Base: {empleado['sueldo_base']} | Bono: {bono} | Propina: {propina} | Desc. Salud: {salud} | Desc. AFP: {afp} | Sueldo Liquido: {sueldoLiquido:,}'.replace(',','.'))

def estadisticas(empleados, ventas):
    venta_maxima = max([venta['total_venta'] for venta in ventas['ventas']])
    total_venta = sum([venta['total_venta'] for venta in ventas['ventas']])
    venta_minima = min([venta['total_venta'] for venta in ventas['ventas']])
    promedio_venta = int(total_venta/len(ventas['ventas']))
    
    print(f'Venta Maxima: {venta_maxima}')
    print(f'Total Venta: {total_venta}')
    print(f'Venta Minima: {venta_minima}')

    estadisticas = {
        'venta maxima':venta_maxima,
        'venta minima': venta_minima,
        'promedio venta': promedio_venta
    }
    guardarCSV(estadisticas)
    guardaaTXT(estadisticas)
    print('\nEstadistica creada con exito')
    display()




def menuGeneral():
    print('-------- MENU GENERAL -------')
    print('[1] Precargar Venta')
    print('[2] Crear Venta')
    print('[3] Reporte de Sueldo')
    print('[4] Ver estadisticas')
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
    empleados, cargos, ventas = cargarDAtos()
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
                    idVenta(ventas)
                    precargarVenta(empleados, ventas)
                elif opc1 == 2:
                    crearVenta(empleados, ventas)
                elif opc1 == 3:
                    reporteSueldo(empleados, ventas)
                elif opc1 == 4:
                    estadisticas(empleados, ventas)   
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