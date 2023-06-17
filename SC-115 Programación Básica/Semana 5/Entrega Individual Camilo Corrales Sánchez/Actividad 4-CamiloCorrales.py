#Actividad Evaluativa 
#Integrante: Corrales Sánchez Camilo,
#Profesor: Salas Sevilla Oscar Francisco

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
