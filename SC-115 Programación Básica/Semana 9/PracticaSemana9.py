"""
1.Eduardo es un joven ciclista, cada semana debe reportar a su entrenador la cantidad de kilometros recorridos 
en sus prácticas. Haga un programa que le permita almacenar para cada día los kilómetros recorridos y luego 
al final de la semana muestre por cada día, junto con el total de la semana. Para la solución, utilice arreglos y ciclos. 
"""

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
kilometros_semana = [0, 0, 0, 0, 0, 0, 0]

for i in range(len(dias_semana)):
    kilometros_dia = float(input("Ingrese los kilómetros recorridos el día {}: ".format(dias_semana[i])))
    kilometros_semana[i] = kilometros_dia

print("\nReporte Semanal:")
for i in range(len(dias_semana)):
    print("{}: {} kilómetros".format(dias_semana[i], kilometros_semana[i]))

total_semana = sum(kilometros_semana)
print("Total Semanal: {} kilómetros".format(total_semana))

"""
2.En una sala de teatro se requiere almacenar los nombres de las personas que ocuparan las 
butacas de una fila, cada fila tiene 10 butacas. Cree un programa en python que almacena 
los nombres en las posiciones que le van indicando, por ejemplo: Ana Jiménez, 4 (el cuatro 
indica el número de butaca).
"""

fila = [""] * 10  # Inicializamos la fila con 10 espacios vacíos

while True:
    nombre = input("Ingrese el nombre de la persona (o 'salir' para terminar): ")
    if nombre.lower() == "salir":
        break

    butaca = int(input("Ingrese el número de butaca: "))

    if butaca < 1 or butaca > 10:
        print("El número de butaca debe estar entre 1 y 10. Intente nuevamente.")
        continue

    fila[butaca - 1] = nombre  # Restamos 1 para ajustar el índice del arreglo

print("\nEstado de la sala de teatro:")
for i in range(len(fila)):
    if fila[i] != "":
        print("Butaca {}: {}".format(i + 1, fila[i]))

"""
3.Se requiere un programa que imprima una palabra al revés, debe
funcionar para cualquier palabra, por lo cual debe utilizar instrucciones
de lectura. En la solución utilice ciclos     
"""
palabra = input("Ingrese una palabra: ")
palabra_al_reves = ""

for i in range(len(palabra) - 1, -1, -1):
    palabra_al_reves += palabra[i]

print("Palabra al revés: ", palabra_al_reves)

"""
4.Jimena es una joven que trabaja para pagarse sus estudios. Se ha
inscrito en una de las plataformas de entrega de comida y otros.
Haga un programa que le permita a Jimena registrar el monto ganado
en cada día, al finalizar la semana le mostrará el total y le indicará el día
que ganó menos dinero.
"""
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
monto_semana = []
total_semana = 0
dia_menos_dinero = None
menor_monto = float('inf')  # Inicializamos con un valor muy grande para comparar

for i in range(len(dias_semana)):
    monto_dia = float(input("Ingrese el monto ganado el día {}: ".format(dias_semana[i])))
    monto_semana.append(monto_dia)
    total_semana += monto_dia

    if monto_dia < menor_monto:
        menor_monto = monto_dia
        dia_menos_dinero = dias_semana[i]

print("\nReporte Semanal:")
for i in range(len(dias_semana)):
    print("{}: ${}".format(dias_semana[i], monto_semana[i]))

print("\nTotal Semanal: ${}".format(total_semana))
print("Día con menos dinero ganado: {}".format(dia_menos_dinero))

