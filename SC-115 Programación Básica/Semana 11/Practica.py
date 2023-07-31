import os

def archivo_existe(nombre_archivo):
    return os.path.exists(nombre_archivo)

def agregar_informacion(nombre_archivo):
    if archivo_existe(nombre_archivo):
        with open(nombre_archivo, 'a') as archivo:
            nombre = input("Ingrese el nombre del estudiante: ")
            grupo = input("Ingrese el número de grupo: ")
            calificacion = input("Ingrese la calificación: ")

            linea = f"{nombre},{grupo},{calificacion}\n"
            archivo.write(linea)

        print("Información agregada correctamente.")
    else:
        print("El archivo no existe. Asegúrese de crearlo antes de agregar información.")

def mostrar_informacion(nombre_archivo):
    if archivo_existe(nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            print("Información de los estudiantes:")

            for linea in archivo:
                nombre, grupo, calificacion = linea.strip().split(',')
                print(f"Nombre: {nombre}, Grupo: {grupo}, Calificación: {calificacion}")
    else:
        print("El archivo no existe o no se ha creado información.")

nombre_archivo = 'notas_estudiantes.txt'
condicion = True

while condicion:
    print("\n--- Menú ---")
    print("1. Agregar información de un estudiante")
    print("2. Mostrar información de todos los estudiantes")
    print("3. Salir")

    opcion = input("Seleccione una opción (1/2/3): ")

    if opcion == '1':
        agregar_informacion(nombre_archivo)
    elif opcion == '2':
        mostrar_informacion(nombre_archivo)
    elif opcion == '3':
        print("Saliendo del programa...")
        condicion = False
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
