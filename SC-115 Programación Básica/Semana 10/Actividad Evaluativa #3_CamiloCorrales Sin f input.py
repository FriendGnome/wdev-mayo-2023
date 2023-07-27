#Actividad Evaluativa 3 Camilo Corrales
#Profesor Salas Sevilla Oscar Francisco
#Programación Básica (Introducción a la Programación) Campus 
#Virtual 2023 Segundo Cuatrimestre LAB:V (6pm-9pm) [NA] Grupo No.8

"""
1.Una fábrica de zapatos recibe un pedido de zapatos de forma masiva. Para llevar un control se requiere elaborar un programa en 
Python que solicite la cantidad de zapatos a fabricar, el precio de cada zapato fabricado y al final imprima por cada zapato el 
monto respectivo. Se debe totalizar al final la cantidad de zapatos fabricados y el monto total del pedido. Se deben usar funciones 
y ciclos y no se deben usar funciones de librería.

"""

def obtener_precio(numero_zapato):
    precio = float(input(f"Ingrese el precio del zapato: "))
    #Profe no me mates por usar un f input, quería que mi programa se viera bonito :´v
    return precio


print("Bienvenido a la fábrica de zapatos.")
cantidad = input("Ingrese la cantidad de zapatos a fabricar (o escriba 'salir' para finalizar): ")

if cantidad.lower() == "salir":
    print("Gracias por usar el programa.")
else:
    cantidad = int(cantidad)  
    precio_total = 0.0

    for i in range(cantidad):
        numero_zapato = i + 1
        precio = obtener_precio(numero_zapato)
        precio_total += precio

    print("Monto total del pedido:", precio_total)
    print("Total de zapatos fabricados:", cantidad)


"""
2.Un supermercado está realizando el inventario de 5 productos en bodega: Arroz, Frijoles, Leche, Macarrones y Salsas. Elabore un 
programa en Python que, por cada producto solicite la cantidad de cada uno, y posteriormente imprima el arreglo de cantidades 
por pantalla. En cada impresión debe evaluar si la cantidad del producto es menor a 10 unidades, debe indicarle al usuario que 
debe realizar un pedido de reabastecimiento. Usar funciones, arreglos y ciclos. Solo lo visto en clase.
"""

def obtener_cantidad(producto):
    cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
    #f input de nuevo :3c
    return cantidad

productos = ["Arroz", "Frijoles", "Leche", "Macarrones", "Salsas"]
inventario = [0] * len(productos)

print("Inventario de productos en bodega:")

for i in range(len(productos)):
    producto = productos[i]
    cantidad = obtener_cantidad(producto)
    inventario[i] = cantidad
    if cantidad < 10:
        print(f"¡Pedido de reabastecimiento para {producto} necesario!")

print("\nCantidad de productos en bodega:")
for i in range(len(productos)):
    producto = productos[i]
    cantidad = inventario[i]
    print(producto, cantidad)


"""
3.Una compañía está elaborando un programa para dispositivos móviles que permita registrar la lista de actividades de una persona durante 
la semana y que permita asignar nuevas tareas a cada día de la semana. Usted ha sido contratado para elaborar un programa en Python que, 
mediante arreglos (uno dinámico por cada día de la semana), solicite al usuario las actividades que realiza para cada día y al final imprima 
en pantalla los arreglos con la cantidad de actividades realizadas. Se debe usar ciclos, funciones y arreglos. Solo lo visto en clase.
"""
def obtener_actividades(dia):
    actividades = []
    condicion = True
    while condicion:
        actividad = input(f"Ingrese una actividad para el día {dia} (o escriba 'salir' para finalizar): ")
        if actividad == "salir":
            condicion = False
        else:
            actividades = actividades + [actividad]
    return actividades

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
actividades_lunes = []
actividades_martes = []
actividades_miercoles = []
actividades_jueves = []
actividades_viernes = []
actividades_sabado = []
actividades_domingo = []

print("Bienvenido al programa de registro de actividades.")

opcion = 0
while opcion != 8:
    print("\nMenu:")
    print("1. Lunes")
    print("2. Martes")
    print("3. Miércoles")
    print("4. Jueves")
    print("5. Viernes")
    print("6. Sábado")
    print("7. Domingo")
    print("8. Finalizar programa")

    opcion = input("Seleccione un día (1-8): ")
    opcion = int(opcion)
    if 1 <= opcion <= 7:
        dia_elegido = dias_semana[opcion - 1]
        actividades_dia = obtener_actividades(dia_elegido)
        if dia_elegido == "Lunes":
            actividades_lunes = actividades_dia
        elif dia_elegido == "Martes":
            actividades_martes = actividades_dia
        elif dia_elegido == "Miércoles":
            actividades_miercoles = actividades_dia
        elif dia_elegido == "Jueves":
            actividades_jueves = actividades_dia
        elif dia_elegido == "Viernes":
            actividades_viernes = actividades_dia
        elif dia_elegido == "Sábado":
            actividades_sabado = actividades_dia
        elif dia_elegido == "Domingo":
            actividades_domingo = actividades_dia
        elif opcion == 8:
            print("Gracias por usar el programa. Finalizando...")
        else:
            print("Opción inválida. Por favor, seleccione un numero válido.")

print("\nCantidad de actividades por día:")
print(f"Lunes:", len(actividades_lunes))
print(f"Martes:", len(actividades_martes))
print(f"Miércoles:", len(actividades_miercoles))
print(f"Jueves:", len(actividades_jueves))
print(f"Viernes:", len(actividades_viernes))
print(f"Sábado:", len(actividades_sabado))
print(f"Domingo:", len(actividades_domingo))