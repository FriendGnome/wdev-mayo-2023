#Actividad/Caso Evaluativa Camilo Corrales
#Profesor Salas Sevilla Oscar Francisco
#Programación Básica (Introducción a la Programación) Campus 
#Virtual 2023 Segundo Cuatrimestre LAB:V (6pm-9pm) [NA] Grupo No.8

"""
1.Una persona invierte 1.000 dólares en una cuenta de ahorro con un 5% de interés. Se asume que todo el interés se deja en 
depósito dentro de la cuenta (no se realizan retiros). Elabore un algoritmo en phyton que cálcule y despliegue el monto 
acumulado de la cuenta al final de cada año durante 10 años. La fórmula para determinar estos montos es: (15 pts) 
a=p (1 + r)ᴺ
donde:
p= es el monto de la inversión original (es decir, la inversión principal)
r=es la tasa de interés anual
N = es el número de años
a=es el monto del depósito al final del año n.

"""
p = 1000  
r = 0.05  
N = 10  

n = 1
while n <= N:
    a = p * (1 + r)**n
    print("Año", n, ": El monto total acumulado durante el año ",n," es igual a=", a)
    n += 1

print("Muchas gracias por usar el programa!")

"""
2.Una empresa telefónica esta realizando una campaña de venta entre 
sus clientes preferidos a quienes les ofrece las siguientes opciones
de paquetes de internet:

Solo internet por un coste de 30 dólares.
Internet y Cable por un coste de 50 doláres.
Internet, Cable y 3 paquetes de canales “Premium” por un coste de 75 doláres.

Cuando se está realizando el registro del cliente, se le consulta el paquete deseado, si tiene algún servicio previo y 
de ser el caso se le aplica un 10% de descuento al monto. En caso de tener un servicio previo y tener meses en mora, 
se le aplica un 13% de impuesto por cada mes en mora.

Desarrolle un programa en Pyton que, solicite la cantidad de clientes a registrar y por cada uno permita registrar 
el paquete seleccionado, si tiene servicios previos y muestre por cada cliente el monto a pagar por mes en el alquiler 
del sevicio.

"""

cantidad_clientes = int(input("Ingrese la cantidad de clientes que desea registrar: "))

contador = 0

while contador < cantidad_clientes:
    paquete = int(input("Seleccione el paquete que el cliente prefiere:"
                        "\n1. Solo Internet costo: 30 dolares"
                        "\n2. Internet y Cable costo: 50 dolares"
                        "\n3. Internet, Cable y 3 paquetes Premium costo: 75 dolares\n"))
    
    servicios_previos = input("¿Tiene servicios previos? (s/n): "
                              "\nNote: El programa solo acepta (s) para sí o (n) para no en minusculas: ")
    #weeeeeeeeno realmente acepta s para si o cualquier otro valor para no jiji
    meses_mora = int(input("Ingrese la cantidad de meses en mora:"
                           "\nSi no tiene meses en mora digite 0: "))

    costo = 0

    if paquete == 1:
        costo = 30
    elif paquete == 2:
        costo = 50
    elif paquete == 3:
        costo = 75
    if meses_mora == 0:
        print("Gracias por no tener meses en mora!")
    if servicios_previos == 's':
        costo *= 0.9

        impuesto_por_mes = 0.13 * meses_mora
        costo += costo * impuesto_por_mes

    print("Su monto a pagar por mes por el uso de nuestro servicio es igual a:", costo, "Que lo disfrute!")
    print("El programa empezara de nuevo para registrar a otro cliente o terminara si no hay mas clientes por registrar.")
    contador += 1
print("El programa ha terminado gracias por usar el programa")
"""
3.Una agencia de viajes vende paquetes para cuatro destinos diferentes,
“España, Inglaterra, Brazil y Argentina”. Cada paquete tiene un 
valor de 800, 1200, 600 y 800 dólares por persona respectivamente. 
Elabore un programa en Python que, mediante un menú solicite el 
paquete seleccionado, la cantidad de personas que van a viajar y 
despliegue en pantalla el monto a pagar por el paquete seleccionado.
Es importante considerar que menores de 2 años no pagan tiquete ni 
hospedaje y que si se viaja en el los meses de Enero, Julio y 
Diciembre, se le debe aplicar un 10% por “temporada alta”. 
El menú debe permitir ingresar únicamente uno de los destinos 
indicados anteriormente. (15 pts).


"""

precio_1 = 800
precio_2 = 1200
precio_3 = 600
precio_4 = 800

print("Espero estés muy bien y gracias por preferirnos para realizar tu viaje."
      "\nEstos son los destinos que tenemos disponibles:")
print("1. España - Precio: 800 dólares")
print("2. Inglaterra - Precio: 1200 dólares")
print("3. Brazil - Precio: 600 dólares")
print("4. Argentina - Precio: 800 dólares")

destino_seleccionado = int(input("Seleccione el número del destino deseado: "))
cantidad_personas = int(input("Ingrese la cantidad de personas que van a viajar: "))
temporada_alta = input("¿Es temporada alta? (s/n)"
                       "\nNota 1: Enero, julio o diciembre se consideran temporada alta."
                       "\nNota 2: El programa solo acepta (s) para sí o (n) para no en minúsculas: ")

monto_pagar = 0
destino = ""

if destino_seleccionado == 1:
    monto_pagar = precio_1 * cantidad_personas
    if temporada_alta == "s":
        monto_pagar *= 1.1
        destino = "España"
elif destino_seleccionado == 2:
    monto_pagar = precio_2 * cantidad_personas
    if temporada_alta == "s":
        monto_pagar *= 1.1
        destino = "Inglaterra"
elif destino_seleccionado == 3:
    monto_pagar = precio_3 * cantidad_personas
    if temporada_alta == "s":
        monto_pagar *= 1.1
        destino = "Brazil"
elif destino_seleccionado == 4:
    monto_pagar = precio_4 * cantidad_personas
    if temporada_alta == "s":
        monto_pagar *= 1.1
        destino = "Argentina"

print("El monto a pagar por tu viaje a", destino, "será de:", monto_pagar)
print("¡Muchas gracias por preferirnos para hacer tus viajes! Espero que te vaya muy bien.")