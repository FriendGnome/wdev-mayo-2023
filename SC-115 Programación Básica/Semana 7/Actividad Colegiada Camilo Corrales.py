#Actividad Colegiada Camilo Corrales
#Profesor Salas Sevilla Oscar Francisco
#Holas, por aquello entrego lo que hize tambien

"""
1.Se requiere analizar las estaturas de los N niños de una escuela y extraer la siguiente
estadística:
• Cantidad de niños que miden menos de 100 cm.
• Cantidad de niños que miden entre 100 y 120 cm.
• Cantidad de niños que miden entre 121 y 130 cm.
• Cantidad de niños que miden entre 131 y 140 cm.
• Cantidad de niños que miden más de 140 cm.
• Promedio de estaturas.
• Muestre los resultados obtenidos.
"""
acum_menor_100 = 0
acum_100_120 = 0
acum_121_130 = 0
acum_131_140 = 0
acum_mas_140 = 0
total_estaturas = 0
contador_estaturas = 0
opcion='s'

while opcion == 's':
    estatura = float(input("Ingrese la estatura (cm): "))
    
    if estatura < 100:
        acum_menor_100 += 1
    elif estatura >= 100 and estatura <= 120:
        acum_100_120 += 1
    elif estatura >= 121 and estatura <= 130:
        acum_121_130 += 1
    elif estatura >= 131 and estatura <= 140:
        acum_131_140 += 1
    else:
        acum_mas_140 += 1
    
    total_estaturas += estatura
    contador_estaturas += 1
    opcion = input("¿Desea ingresar otra estatura? (s/n)"
                   "\nNota: El programa solo acepta (s) para sí o (n) para no en minusculas: ")
    

promedio_estaturas = total_estaturas / contador_estaturas

print("Cantidad de niños que miden menos de 100 cm:", acum_menor_100)
print("Cantidad de niños que miden entre 100 y 120 cm:", acum_100_120)
print("Cantidad de niños que miden entre 121 y 130 cm:", acum_121_130)
print("Cantidad de niños que miden entre 131 y 140 cm:", acum_131_140)
print("Cantidad de niños que miden más de 140 cm:", acum_mas_140)
print("Promedio de estaturas:", promedio_estaturas);


"""
2.Desarrollar un programa que le solicite al usuario un valor y muestre los primeros
10 números divisibles entre este valor. 
"""
valor = int(input("Ingrese un valor y se mostraran los 10 primeros números divisibles entre este valor.: "))

contador = 0
numero = 1

while contador < 10:
    if numero % valor == 0:
        print(numero)
        contador += 1
    numero += 1

    print("Gracias por usar el programa!")

"""
3.Desarrolle un programa que le solicita al usuario 15 salarios y que le indique cuánto
dinero se necesita para que al menos todos ganen $500.
"""
acum_falta_500 = 0
contador_mayor_500 = 0
contador=0
while contador < 15:
    salario = float(input("Ingrese el valor del salario: "))
    contador+=1
    if salario < 500:
        acum_falta_500 += (500 - salario)
    elif salario > 500:
        contador_mayor_500 += 1
    

print("Falta acumulada para alcanzar $500 en todos los salarios:", acum_falta_500)
print("Número de salarios que ya son mayores a $500:", contador_mayor_500)
print("Gracias por usar el programa!")

    