import os
import time
import json
import random
import csv
os.system('cls')


def cargarDatos():
    with open('empleados.json', 'r', encoding='utf-8') as archivoEMPLEADOS:
        empleados = json.load(archivoEMPLEADOS)
    with open('cargos.json', 'r', encoding='utf-8') as archivoCARGOS:
        cargos =  json.load(archivoCARGOS)
    with open('ventas.json', 'r', encoding='utf-8') as archivoVENTAS:
        ventas = json.load(archivoVENTAS)
    return empleados, cargos, ventas

def crearCSV(estadisticas):
    with open('ESTADISTICA.csv', 'w', newline='\n', encoding='utf-8') as archivo:
        escribir = csv.writer(archivo)
        escribir.writerow(estadisticas)
        escribir.writerow([estadisticas['Venta Menor'], estadisticas['Venta Menor'], estadisticas['Promedio Ventas']])

def idVenta(ventas):
    id_venta = 0
    for venta in ventas['ventas']:
        if int(venta['id_venta']) > id_venta:
            id_venta = int(venta['id_venta'])
    return id_venta

def precargarVenta(empleados,ventas):
    id_venta = idVenta(ventas)
    for i in range(50):
        id_venta += 1
        empleado = random.choice(empleados)
        id_empleado = empleado['id_empleado']
        fecha = '06/08/2024'
        total_venta = random.choice(range(30_000, 70_000, 100))
        propina = int(total_venta*0.1)
        #print(id_venta, id_empleado, fecha, total_venta, propina)
        nuevaVenta = {
            "id_venta": id_venta,
            "empleado": id_empleado,
            "fecha": fecha,
            "total_venta": total_venta,
            "propina": propina
        }
        ventas['ventas'].append(nuevaVenta)
    print(ventas)
    print('Venta Agregadas con exito')
    time.sleep(2)
    limpiar()
      
def crearVenta(empleados, ventas):
    id_venta = idVenta(ventas)
    for empleado in empleados:
        print(f'ID: {empleado['id_empleado']} -->> {empleado['nombre']} {empleado['apellido']}')
    print('---'*9)
    id_venta += 1
    id_empleado = input('Ingrese el ID del empleado que realiza la venta: ')
    fecha = '06/08/2024'
    total_venta = int(input('Ingrese el monto de la venta: '))
    propina = int(total_venta*0.1)
    #print(id_venta, id_empleado, fecha, total_venta, propina)
    nuevaVenta = {
        "id_venta": id_venta,
        "empleado": id_empleado,
        "fecha": fecha,
        "total_venta": total_venta,
        "propina": propina
    }
    ventas['ventas'].append(nuevaVenta)
    print('Venta Agregadas con exito')
    time.sleep(1)

def reporteSueldos(empleados, ventas):
    for empleado in empleados:
        total_ventas = 0
        propinas = 0
        bono = 0
        salud = int(empleado['sueldo_base']*0.07)
        afp = int(empleado['sueldo_base']*0.12)
        
        for venta in ventas['ventas']:
            if venta['empleado'] == empleado['id_empleado']:
                total_ventas += venta['total_venta']
                propinas += venta['propina']
        if total_ventas >= 2_000_000:
            bono = int(empleado['sueldo_base']*0.05)
        elif total_ventas >= 1_000_000:
            bono = int(empleado['sueldo_base']*0.03)
        elif total_ventas >= 500_000:
            bono = int(empleado['sueldo_base']*0.1)
        
        sueldoLiquido = (empleado['sueldo_base']-salud-afp) + bono + afp
        print(f'Nombre: {empleado['nombre']} {empleado['apellido']} | Sueldo Base: {empleado['sueldo_base']} | Propinas: {propinas} | Bono: {bono} | Desc. Salud: {salud} | Desc. AFP: {afp} Sueldo Liquido: {sueldoLiquido}')

def estadisticas(empleados, ventas):
    ventaMenor = ventas['ventas'][0]['total_venta']
    ventaMayor = ventas['ventas'][0]['total_venta']
    total_ventas = 0
    contador = 0
    for venta in ventas['ventas']:
        if ventaMenor > venta['total_venta']:
            ventaMenor = venta['total_venta']
        elif ventaMayor < venta['total_venta']:
            ventaMayor = venta['total_venta']
        total_ventas += venta['total_venta']
        contador += 1
    promendioVenta = round(total_ventas/contador)
    print(f'Venta Menor: ${ventaMenor:,}'.replace(',','.'))
    print(f'Venta Mayor: ${ventaMayor:,}'.replace(',','.'))
    print(f'Promedio Ventas: ${promendioVenta:,}'.replace(',','.'))

    estadisticas = {
        'Venta Menor': ventaMenor,
        'Venta Mayor': ventaMayor,
        'Promedio Ventas': promendioVenta
    }
    crearCSV(estadisticas)

def menuGeneral():
    print('------- MENU GENERAL -------')
    print('[1] Precargar Venta')
    print('[2] Crear Venta')
    print('[3] Reporte de Sueldos')
    print('[4] Ver Estadisticas')
    print('[5] Salir\n')

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
    empleados, cargos, ventas = cargarDatos()
    menu1 = True
    while menu1:
        menuGeneral()
        opc1 = 0
        try:
            opc1 = int(input('INGRESE UNA OPCION: '))
            if opc1 < 1 or opc1 > 7:
                errorRango()
            else:
                if opc1 == 1:
                    precargarVenta(empleados,ventas)
                elif opc1 == 2:
                    crearVenta(empleados, ventas)
                    print(ventas)
                elif opc1 == 3:
                    reporteSueldos(empleados, ventas)
                elif opc1 == 4:
                    estadisticas(empleados, ventas)
                elif opc1 == 5:
                    limpiar()
                    print('>>>> ¡HASTA PRONTO! <<<<')
                    time.sleep(1.5)
                    limpiar()
                    menu1 = False
        except:
            errorLetra()
if __name__ == '__main__':
    main() 