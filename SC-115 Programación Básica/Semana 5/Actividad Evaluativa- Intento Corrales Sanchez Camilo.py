#Actividad Evaluativa 
#Integrante: Corrales Sánchez Camilo,
#Profesor: Salas Sevilla Oscar Francisco
#Nota(los miembros de mi grupo usaron el punto dos de este archivo para su grupo
#con mi permiso pero igual quería entregar el que hize por aparte)

"""
1.Elabore un programa en Python que, solicite al usuario un número entero e imprima en 
pantalla si es un número par o impar.
"""

numero = int(input("Ingrese un número entero:"))

if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")


"""
2.Desarrolle un programa en Python para determinar el pago bruto de varios empleados de una 
empresa.La empresa paga un “turno ordinario” por las primeras 40 horas trabajadas por cada 
empleado y paga un “turno y medio” por las demás horas extras trabajadas, después de las primeras 
40 horas. Su programa debe permitir solicitar la tarifa por hora del empleado, la cantidad de horas 
trabajadas y desplegar el pago bruto del empleado.  
"""
variable_empleado=int(input("Bienvenido!\n" 
          "Ingrese su número de empleado:\n"
          "1. Corrales Sánchez Camilo\n"
          "2. Luna Urbina David Guillermo\n"
          "3. Piñas Perez Julio Andres\n"
          "4. Hernandez Urbina Eliecer Josue\n"
          "5. Salas Sevilla Oscar Francisco\n"))

if variable_empleado == 1:
    print("Bienvenido: Corrales Sánchez Camilo.")
elif variable_empleado == 2:
    print("Bienvenido: Luna Urbina David Guillermo")
elif variable_empleado == 3:
    print("Bienvenido: Piñas Perez Julio Andres")
elif variable_empleado == 4:
    print("Bienvenido: Hernandez Urbina Eliecer Josue")
elif variable_empleado == 5:
    print("Bienvenido: Salas Sevilla Oscar Francisco")
else:
    print("No es una opción valida, el sistema continuara,\n"
          "contacte a su administrador para ingresar un nuevo empleado.")

  
opcion=int(input("Seleccione una opcion:\n"
        "1.Solicitar la tarifa por hora del empleado y salario Bruto ordinario.\n"
        "2.Solicitar la cantidad de horas trabajadas y salario Bruto personalizado.\n"))

if opcion == 1:
    print("Su tarifa por hora es",3500)
    print("Su pago bruto por jornada de 40 horas es:",140000)
elif opcion == 2:
    horas_trabajadas= int(input("Ingrese el número de horas trabajadas:"))
    if horas_trabajadas <= 40:
        print("Su salario bruto ordinario es igual a:",horas_trabajadas*3500)
    elif horas_trabajadas >= 41:
        horas_extras= horas_trabajadas-40
        print("Su salario bruto personalizado es igual a:",horas_trabajadas*3500+horas_extras*5250)

print("Gracias por usar el programa!")

"""
3.Elabore un programa en Python que, solicite al usuario el precio de cuatro productos diferentes y 
tras sumarlos, si el monto es mayor a 15 mil colones, le aplique un descuento del 10%, mostrando 
por pantalla el resultado final al cliente.
"""
precio1 = float(input("Ingrese el precio del primer producto: "))
precio2 = float(input("Ingrese el precio del segundo producto: "))
precio3 = float(input("Ingrese el precio del tercer producto: "))
precio4 = float(input("Ingrese el precio del cuarto producto: "))

subtotal = precio1 + precio2 + precio3 + precio4

if subtotal > 15000:
    descuento = subtotal * 0.1
    total = subtotal - descuento
    print("El monto total con descuento es de:", total, "colones.")
else:
    print("El monto total es de:", subtotal, "colones.")

print("Gracias por usar el programa!")

"""
4.La tienda de ropa “Vestimentas OnLine” cuenta con una promoción en las siguientes prendas:
Pantalones, si son 2 o más pantalones, aplica un 10% de descuento.
Camisas de vestir, si compra 2, la segunda es a mitad de precio.
Más de 4 prendas (si son camisas o pantalones, o ambas) un 30% de descuento.

Elabore un programa en Python que, solicite al usuario el tipo de prenda que está comprando, la cantidad 
de prendas, el monto individual de cada una y calcule el monto total a pagar con base en los descuentos 
indicados anteriormente."
"""
print("Bienvenidos a Vestimentas online")
tipo_prenda = int(input("Ingrese el numero del tipo de prenda que está comprando\n" 
                        "1.pantalones.\n" 
                        "2.camisas.\n"
                        "3.combinado pantalos y camisas.\n"))
if tipo_prenda == 1:
    cantidad_pantalones = int(input("Ingrese la cantidad de pantalones: "))
    monto_individual_pantalones = float(input("Ingrese el monto individual de cada pantalon: "))
elif tipo_prenda == 2:
    cantidad_camisas = int(input("Ingrese la cantidad de camisas: "))
    monto_individual_camisas = float(input("Ingrese el monto individual de cada camisa: "))
elif tipo_prenda == 3:
    cantidad_camisas = int(input("Ingrese la cantidad de camisas: "))
    monto_individual_camisas = float(input("Ingrese el monto individual de cada camisa: "))
    cantidad_pantalones = int(input("Ingrese la cantidad de pantalones: "))
    monto_individual_pantalones = float(input("Ingrese el monto individual de cada pantalon: "))
else:
    print("No escogió un número valido. El programa continuará")

if tipo_prenda == 1:
    subtotal=cantidad_pantalones*monto_individual_pantalones 
elif tipo_prenda == 2:
    subtotal=cantidad_camisas*monto_individual_camisas 
elif tipo_prenda == 3:
     subtotal=cantidad_pantalones*monto_individual_pantalones+cantidad_camisas*monto_individual_camisas 

descuento = 0

if tipo_prenda == 1 and cantidad_pantalones >= 2:
    descuento = subtotal * 0.1
elif tipo_prenda == 2 and cantidad_camisas >= 2:
    descuento = monto_individual_camisas * 0.5

if cantidad_camisas > 4 or cantidad_pantalones > 4 or cantidad_pantalones+cantidad_camisas > 4:
    descuento = subtotal * 0.3

total = subtotal - descuento

print("El monto total a pagar es de:", total, "colones.")
