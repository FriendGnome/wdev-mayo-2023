#Game of Progra/Actividad Evaluativa
#Grupo los Erizos   
#Camilo Corrales Sanchez, Eliecer Hernandez Urbina , Julio Andres Perez Piñas,
"""
Realice los siguientes ejercicios de forma individual en la clase:
Investigue la función SPLIT de Python y elabore mediante funciones un ejemplo de uso.


Elabore un menú en Python que permita:
Solicitar un número entero, mediante el cual se creará un arreglo de números enteros.
Rellenar el arreglo, mediante esta opción se incluirán números enteros con edades de personas hasta completar el tamaño del arreglo.
Realizar cálculo, mediante esta opción, se creará un arreglo unidimensional que manejará en cada posición del arreglo los siguientes resultados:
Edad mínima.
Edad máxima.
Edad promedio.
Cantidad de personas mayores a 18.
Cantidad de personas mayores de 30.
Guardar datos, mediante esta opción se crearán dos archivos, el primero llamado edades.txt, guardará el arreglo de edades, cada una separada por comas. El segundo arreglo, denominado resultado.txt guardará el arreglo de los cálculos separados por comas.
Cargar datos, mediante esta opción se abrirán ambos archivos y se cargarán los datos en cada uno de los arreglos.
Mostrar datos, imprimirá ambos arreglos por pantalla de tabulada para facilitar su lectura.
Salir, saldrá del programa.
1
"""

def ingresar_datos():
    print("Ingrese las edades (ingrese 's' para salir):")
    condicion = True
    while condicion:
        edad = input("Ingrese una edad: ")
        if edad.lower() == 's':
            condicion = False
        else:
            try:
                edad = int(edad)
                edades.append(edad)
            except ValueError:
                print("Entrada inválida. Ingrese una edad válida o 's' para salir.")


def guardar_datos():
    with open("edades.txt", "w") as file:
        for edad in edades:
            file.write(str(edad))
            file.write(",")

    resultado_min = min(edades)
    resultado_max = max(edades)
    resultado_promedio = sum(edades) / len(edades)
    resultado_mayores_18 = 0
    resultado_mayores_30 = 0

    for edad in edades:
        if edad > 18:
            resultado_mayores_18 += 1
            if edad > 30:
                resultado_mayores_30 += 1

    with open("resultados.txt", "w") as file:
        file.write(str(resultado_min) + ",")
        file.write(str(resultado_max) + ",")
        file.write(str(resultado_promedio) + ",")
        file.write(str(resultado_mayores_18) + ",")
        file.write(str(resultado_mayores_30))

    print("Datos guardados correctamente.")


import os

def cargar_datos():
    global edades, resultados
    edades_temp = []
    resultados_temp = []

    #para que no se caiga dependiendo de la compu o directorio
    edades_file_path = os.path.join(os.path.dirname(__file__), "edades.txt")
    resultados_file_path = os.path.join(os.path.dirname(__file__), "resultados.txt")

    with open(edades_file_path, "r") as file:
        edades_data = file.read().split(",")
        for edad in edades_data:
            try:
                edades_temp.append(int(edad))
            except ValueError:
                pass
    with open(resultados_file_path, "r") as file:
        resultados_data = file.read().split(",")
        for resultado in resultados_data:
            try:
                resultados_temp.append(float(resultado))
            except ValueError:
                pass

    edades = edades_temp
    resultados = resultados_temp

def mostrar_datos():
    if not edades:
        print("No hay datos ingresados.")
    else:
        print("Edades:", edades)
        if resultados:
            print("Resultados: Edad mínima, Edad máxima, Edad promedio, Personas mayores a 18, Personas mayores a 30 abajo en ese orden:")
            print("           ", resultados)
        else:
            print("Aún no se han generado los resultados.")


edades = []
resultados = []
condicion = True

while condicion:
    print("\n--- Menú ---")
    print("1. Ingresar Datos (edades)")
    print("2. Guardar Datos")
    print("3. Cargar Datos")
    print("4. Mostrar Datos")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        ingresar_datos()
    elif opcion == '2':
        print("Guardando datos...")
        guardar_datos()
    elif opcion == '3':
        print("Cargando datos...")
        cargar_datos()
    elif opcion == '4':
        mostrar_datos()
    elif opcion == '5':
        print("Gracias por utilizar el programa. ¡Hasta luego!")
        condicion = False
    else:
        print("Opción inválida. Seleccione una opción válida del menú.")
