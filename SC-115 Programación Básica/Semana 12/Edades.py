def obtener_numero_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")

def crear_arreglo():
    n = obtener_numero_entero("Ingrese el tamaño del arreglo: ")
    arreglo = [0] * n
    return arreglo

def rellenar_arreglo(arreglo):
    for i in range(len(arreglo)):
        edad = obtener_numero_entero(f"Ingrese la edad {i + 1}: ")
        arreglo[i] = edad

def realizar_calculos(arreglo):
    edad_minima = min(arreglo)
    edad_maxima = max(arreglo)
    edad_promedio = sum(arreglo) / len(arreglo)
    mayores_18 = sum(1 for edad in arreglo if edad > 18)
    mayores_30 = sum(1 for edad in arreglo if edad > 30)
    resultados = [edad_minima, edad_maxima, edad_promedio, mayores_18, mayores_30]
    return resultados

def guardar_datos(edades, resultados):
    with open("edades.txt", "w") as file_edades:
        file_edades.write(",".join(map(str, edades)))
    
    with open("resultados.txt", "w") as file_resultados:
        file_resultados.write(",".join(map(str, resultados)))

def cargar_datos():
    with open("edades.txt", "r") as file_edades:
        edades = list(map(int, file_edades.read().split(",")))
    
    with open("resultados.txt", "r") as file_resultados:
        resultados = list(map(float, file_resultados.read().split(",")))
    
    return edades, resultados

def mostrar_datos(edades, resultados):
    print("Edades:")
    print("\t".join(map(str, edades)))
    
    print("Resultados:")
    print("\t".join(map(str, resultados)))

def main():
    edades = []
    resultados = []
    
    while True:
        print("\nMenú:")
        print("1. Crear arreglo de edades")
        print("2. Rellenar arreglo")
        print("3. Realizar cálculos")
        print("4. Guardar datos")
        print("5. Cargar datos")
        print("6. Mostrar datos")
        print("7. Salir")
        
        opcion = obtener_numero_entero("Seleccione una opción: ")
        
        if opcion == 1:
            edades = crear_arreglo()
        elif opcion == 2:
            if not edades:
                print("Primero debe crear el arreglo de edades.")
            else:
                rellenar_arreglo(edades)
        elif opcion == 3:
            if not edades:
                print("Primero debe crear el arreglo de edades.")
            else:
                resultados = realizar_calculos(edades)
        elif opcion == 4:
            if not edades or not resultados:
                print("Primero debe crear el arreglo de edades y realizar los cálculos.")
            else:
                guardar_datos(edades, resultados)
        elif opcion == 5:
            edades, resultados = cargar_datos()
        elif opcion == 6:
            if not edades or not resultados:
                print("No hay datos para mostrar.")
            else:
                mostrar_datos(edades, resultados)
        elif opcion == 7:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
