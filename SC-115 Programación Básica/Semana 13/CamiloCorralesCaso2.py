#Camilo Corrales Caso 2
import os
personasarreglo = []
personas_act=[]
calculos=[]

def cargar_datos():
    with open("Personas.csv", "r") as archivo:
        primera_linea = True
        for linea in archivo:
            if primera_linea == True:
                primera_linea = False
            else:
                columnas = linea.split(",")
                for i in range(len(columnas)):
                    if columnas[i][-1] == "\n":
                        columnas[i] = columnas[i][:-1]
                personasarreglo.append(columnas)
    for persona in personasarreglo:
        if len(persona) > 1:  
            print(persona)
        else:
            print("Error: No hay suficientes datos en la línea para imprimir.")

def actualizar_datos():
    
    for persona in personasarreglo:
        if len(persona) > 1:  
            edad_actual = 2023 - int(persona[1]) 
            peso = float(persona[3])  
            estatura = float(persona[4])  
            imc = peso / (estatura * estatura)
            persona.append(str(edad_actual))
            persona.append(str(imc))
        else:
            print("Actualizando datos...")

def mostrar_resultados():
    contador_imc_mayor_30 = 0
    edad_maxima = 0
    edad_minima = 0
    contador_menores_18_mayor_30 = 0
    contador_mayores_18_mayor_30 = 0
    primera_edad = True
    
    for persona in personasarreglo:
        if len(persona) > 1:
            edad = int(persona[5])
            imc = float(persona[6])
            
            if primera_edad:
                edad_maxima = edad
                edad_minima = edad
                primera_edad = False
                
            if edad > edad_maxima:
                edad_maxima = edad
                
            if edad < edad_minima:
                edad_minima = edad
                
            if edad < 18 and imc > 30:
                contador_menores_18_mayor_30 += 1
            
            if edad >= 18 and imc > 30:
                contador_mayores_18_mayor_30 += 1
            
            if imc > 30:
                contador_imc_mayor_30 += 1
        else:
            print("Mostrando resultados...")
    
    print("Cantidad de personas con IMC mayor a 30:", contador_imc_mayor_30)
    print("Edad máxima:", edad_maxima)
    print("Edad mínima:", edad_minima)
    print("Cantidad de personas menores de 18 con IMC mayor a 30:", contador_menores_18_mayor_30)
    print("Cantidad de personas mayores a 18 con IMC mayor a 30:", contador_mayores_18_mayor_30)


def guardar_datos():
    with open("Personas_act.txt", "w") as archivo:
        for persona in personasarreglo:
            datos_a_guardar = ''
            for i in range(5):
                if len(persona) > 1: 
                    datos_a_guardar += persona[i]
                    if i < 4:
                        datos_a_guardar += ','  
                else:
                    print("Guardando...")
            archivo.write(datos_a_guardar + '\n')

def cargar_datos2():
    with open("Personas_act.txt", "r") as archivo:
        
        for linea in archivo:
            columnas = linea.split(",")
            for i in range(len(columnas)):
                if columnas[i][-1] == "\n":
                    columnas[i] = columnas[i][:-1]
            personas_act.append(columnas)
    
    for persona in personas_act:
        if len(persona) > 1:  
            print(persona)
        else:
            print("Error: No hay suficientes datos en la línea para imprimir.")

condicion = True
while condicion:
    print("\n--- Menú ---")
    print("1. Cargar Datos Generales. Debe escoger esta opcion para empezar o el programa fallara.")
    print("2. Actualizar Datos")
    print("3. Mostrar Resultados")
    print("4. Guardar Datos")
    print("5. Cargar Datos Guardados y Mostrarlos")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        print("Cargando datos...")
        cargar_datos()
    elif opcion == '2':
        print("Actualizando datos...")
        actualizar_datos()
    elif opcion == '3':
        print("Mostrando resultados...")
        mostrar_resultados()
    elif opcion == '4':
        guardar_datos()
    elif opcion == '5': 
        cargar_datos2()
    elif opcion == '6':
        condicion = False
        print("Gracias por utilizar el programa. ¡Hasta luego!")
    else:
        print("Opcion no valida")



    

"""
        for persona in personasarreglo:
            if len(persona) > 1:  
                print(persona[1])
            else:
                print("Error: No hay suficientes datos en la línea para imprimir.")
"""
""" 
    elif opcion == '4':
        print("test")
    elif opcion == '5':
        print("pending")
    elif opcion == '6':
        print("Gracias por utilizar el programa. ¡Hasta luego!")
        condicion = False
    else:
        print("Opción inválida. Seleccione una opción válida del menú.")
"""   


"""
    print("3. Mostrar Resultados")
    print("4. Guardar Resultados")
    print("5. Mostrar Resultados")
"""

