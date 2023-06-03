#Ejercicio 1. Elaborar un programa de bienvenida que muestre un mensaje de bienvenida para una persona. 
#Debe imprimir la información como se muestra a continuación: 
#Bienvenido, estimado Nombre PrimerApellido SegundoApellido 

"""
nombre = input("Ingrese su nombre: ")
primer_apellido = input("Ingrese su primer apellido: ")
segundo_apellido = input("Ingrese su segundo apellido: ")

mensaje_bienvenida = "Bienvenido, estimado " + nombre + " " + primer_apellido + " " + segundo_apellido
print(mensaje_bienvenida)
"""

# Ejercicio 2 hacer una calculadora simple que de suma resta multiplicacion division potencia division entera y modulo de dos numeros
"""
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

def potencia(a, b):
    return a ** b

def division_entera(a, b):
    return a // b

def modulo(a, b):
    return a % b

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

resultado_suma = suma(num1, num2)
resultado_resta = resta(num1, num2)
resultado_multiplicacion = multiplicacion(num1, num2)
resultado_division = division(num1, num2)
resultado_potencia = potencia(num1, num2)
resultado_division_entera = division_entera(num1, num2)
resultado_modulo = modulo(num1, num2)

print("Suma:", resultado_suma)
print("Resta:", resultado_resta)
print("Multiplicación:", resultado_multiplicacion)
print("División:", resultado_division)
print("Potencia:", resultado_potencia)
print("División Entera:", resultado_division_entera)
print("Modulo:", resultado_modulo)
"""

#Ejercicio 3 algo que calcule el area y perimetro de un cuadrado

"""
lado = int(input("Ingrese la longitud del lado del cuadrado: "))

area = lado ** 2
perimetro = 4 * lado

print("El área del cuadrado es:", area)
print("El perímetro del cuadrado es:", perimetro)
"""
"""
luis_edad = int(input("Ingrese la edad de Luis:"))
pedro_edad = int(input("Ingrese la edad de Pedro:"))

temp = luis_edad
luis_edad = pedro_edad
pedro_edad = temp

print("Edad de Luis:", luis_edad)
print("Edad de Pedro:", pedro_edad)

base = float(input("Ingrese el número base: "))
exponente = int(input("Ingrese el exponente: "))
"""


#Desorrolle un programa en python que eleve un numero a una potencia. 
#Debe utilizar instrucciones de lectura y operaciones aritméticas. 
"""
potencia: int(input("Escriba la base:"))
base: int(input("Escriba el exponente:"))

potencia = base ** exponente

print("El resultado de", base, "elevado a la potencia", exponente, "es:", potencia)
"""
#Elabore un programa en Python que, reciba el nombre de 5 productos, solicte sus precios y 
# al final muestre el total a pagar. #Nota: Considere solicitar el porcentaje de impuesto 
# que se debe aplicar al total de la compra. Cómo es una tienda virtual, debe realizar la 
# conversión del monto en dólares y cobrar 4 mil colones de transporte.

"""
producto1 = input("Digite el nombre del primer producto:")
producto2 = input("Digite el nombre del segundo producto:")
producto3 = input("Digite el nombre del tercer producto:")
producto4 = input("Digite el nombre del cuarto producto:")
producto5 = input("Digite el nombre del quinto producto:")

precio1 = int(input("Digite el precio del primer producto:"))
precio2 = int(input("Digite el precio del segundo producto:"))
precio3 = int(input("Digite el precio del tercer producto:"))
precio4 = int(input("Digite el precio del cuarto producto:"))
precio5 = int(input("Digite el precio del quinto producto:"))

total_de_precio = (precio1+precio2+precio3+precio4+precio5)
total_de_precio_con_impuesto = (total_de_precio+total_de_precio*0.13)
transporte = 4000
total_de_precio_en_colones = (total_de_precio_con_impuesto+transporte)
total_de_precio_en_dolares = (total_de_precio_en_colones*0.0019)
print("El total de precio en colones con 4000 de transporte es:", total_de_precio_en_colones)
print("El total de precio en dolares con transporte incluido es:", total_de_precio_en_dolares)
print("su envio está en camino saludes")
"""

#
#
#