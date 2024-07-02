import json
import random
import csv

def cargar_datos():
    with open('empleados.json', 'r') as file:
        empleados = json.load(file)
    with open('tiendas.json', 'r') as file:
        tiendas = json.load(file)
    with open('ventas.json', 'r') as file:
        ventas = json.load(file)
    return empleados, tiendas, ventas

def guardar_datos(ventas):
    with open('ventas.json', 'w') as file:
        json.dump(ventas, file, indent=4)

def generar_venta(id_venta, id_tienda, empleado):
    return {
        "id_venta": id_venta,
        "empleado": empleado,
        "id_tienda": id_tienda,
        "mes": "junio",
        "total_venta": random.randint(50000, 200000)
    }

def precargar_ventas():
    empleados, tiendas, ventas = cargar_datos()
    for _ in range(100):
        id_venta = f"{1000000 + len(ventas['ventas']) + 1}"
        id_tienda = random.choice(tiendas)['id_tienda']
        empleado = random.choice(empleados)['id_vendedor']
        ventas['ventas'].append(generar_venta(id_venta, id_tienda, empleado))
    guardar_datos(ventas)
    print("Ventas precargadas exitosamente.")

def crear_venta():
    empleados, tiendas, ventas = cargar_datos()
    id_venta = f"{1000000 + len(ventas['ventas']) + 1}"
    id_tienda = int(input("Ingrese el ID de la tienda: "))
    empleado = input("Ingrese el ID del vendedor: ")
    venta = generar_venta(id_venta, id_tienda, empleado)
    ventas['ventas'].append(venta)
    guardar_datos(ventas)
    print("Venta creada exitosamente.")

def calcular_sueldo(empleado, ventas):
    sueldo_base = empleado['sueldo_base']
    total_ventas = sum(venta['total_venta'] for venta in ventas if venta['empleado'] == empleado['id_vendedor'])
    salud = sueldo_base * 0.07
    afp = sueldo_base * 0.12
    bono = 0
    if total_ventas > 20000000:
        bono = total_ventas * 0.02
    elif total_ventas > 10000000:
        bono = total_ventas * 0.01
    elif total_ventas > 5000000:
        bono = total_ventas * 0.005
    sueldo_liquido = sueldo_base - salud - afp + bono
    return sueldo_base, salud, afp, bono, sueldo_liquido

def reporte_sueldos():
    empleados, _, ventas = cargar_datos()
    for empleado in empleados:
        sueldo_base, salud, afp, bono, sueldo_liquido = calcular_sueldo(empleado, ventas['ventas'])
        print(f"Empleado: {empleado['nombre']} {empleado['apellido']}")
        print(f"Sueldo Bruto: {sueldo_base}")
        print(f"Salud: {salud}")
        print(f"AFP: {afp}")
        print(f"Bono: {bono}")
        print(f"Sueldo Líquido: {sueldo_liquido}")
        print("="*30)

def estadisticas():
    _, _, ventas = cargar_datos()
    total_ventas = sum(venta['total_venta'] for venta in ventas['ventas'])
    ultima_venta = max(ventas['ventas'], key=lambda x: x['total_venta'])
    promedio_ventas = total_ventas / len(ventas['ventas'])
    with open('estadisticas.csv', 'w', newline='') as csvfile:
        fieldnames = ['Total Ventas', 'Ultima Venta Mayor Monto', 'Promedio Ventas']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'Total Ventas': total_ventas, 'Ultima Venta Mayor Monto': ultima_venta['total_venta'], 'Promedio Ventas': promedio_ventas})
    with open('estadisticas.txt', 'w') as txtfile:
        txtfile.write(f"Total de Ventas: {total_ventas}\n")
        txtfile.write(f"Última Venta por Mayor Monto: {ultima_venta['total_venta']}\n")
        txtfile.write(f"Promedio de Ventas: {promedio_ventas}\n")
    print("Estadísticas guardadas exitosamente.")

def menu():
    while True:
        print("1. Precargar ventas y guardar en ventas.json")
        print("2. Crear nuevas ventas")
        print("3. Reporte de sueldos")
        print("4. Ver estadísticas por tienda")
        print("5. Salir")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            precargar_ventas()
        elif opcion == 2:
            crear_venta()
        elif opcion == 3:
            reporte_sueldos()
        elif opcion == 4:
            estadisticas()
        elif opcion == 5:
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
