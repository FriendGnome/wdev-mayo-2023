"""
1.Elabore un programa en Python que, solicite al usuario el ingreso de un número entero y 
posteriormente, mediante un menú permita seleccionar entre realizar una sumatoria o el 
factorial de los números, hasta el número ingresado o bien, realizar una cuenta regresiva 
por pantalla desde el número ingresado y hasta cero.
"""
numero = int(input("Ingrese un número entero: "))

opcion = 0
while opcion != 4:
    print("\n Menú" )
    print("1. Sumatoria")
    print("2. Factorial")
    print("3. Cuenta regresiva")
    print("4. Salir")

    opcion = int(input("Seleccione una opción (1-4): "))

    if opcion == 1:
        suma = 0
        for i in range(1, numero + 1):
            suma += i
        print(f"La sumatoria hasta el número {numero} es: {suma}")
    elif opcion == 2:
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        print(f"El factorial de {numero} es: {factorial}")
    elif opcion == 3:
        for i in range(numero, -1, -1):
            print(i)
    elif opcion == 4:
        print("¡Hasta luego!")
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

"""
2.Elabore un programa en Python que, solicite al usuario los ingresos mensuales, y después 
de totalizarlos, calcule la cantidad de meses requeridos para obtener un ahorro de 500 mil 
colones si por mes se logra ahorrar un 2% del ingreso mensual.
"""

total_ingresos = 0

ingreso_mensual = float(input("Ingrese el ingreso mensual (0 para finalizar): "))

while ingreso_mensual != 0:
    total_ingresos += ingreso_mensual
    ingreso_mensual = float(input("Ingrese el ingreso mensual (0 para finalizar): "))

ahorro_mensual = total_ingresos * 0.02

ahorro_objetivo = 500000
meses = 0
ahorro_actual = 0

while ahorro_actual < ahorro_objetivo:
    ahorro_actual += ahorro_mensual
    meses += 1

print(f"\nTotal de ingresos: {total_ingresos} colones")
print(f"Ahorro mensual: {ahorro_mensual} colones")
print(f"Cantidad de meses requeridos para alcanzar el ahorro de 500,000 colones: {meses} meses")

"""
Elabore un programa en Python que, mediante un menú en pantalla permita al usuario 
seleccionar entre 5 tipos diferentes de comida y sus respectivos precios. Una vez seleccionado,
se le debe calcular el 13% por concepto de IVA. Es importante considerar que el plato de 
niños cuenta con un 30% de descuento y que puede seleccionar más de un plantillo en la 
compra.
"""

comida_1 = "Hamburguesa"
precio_1 = 1000

comida_2 = "Pizza"
precio_2 = 1500

comida_3 = "Pasta"
precio_3 = 800

comida_4 = "Ensalada"
precio_4 = 600

comida_5 = "Plato de niños"
precio_5 = 700

subtotal = 0
compra = ""

opcion = 0

while opcion != 6:
    print("\n--- Menú ---")
    print("1. " + comida_1 + " - " + str(precio_1) + " colones")
    print("2. " + comida_2 + " - " + str(precio_2) + " colones")
    print("3. " + comida_3 + " - " + str(precio_3) + " colones")
    print("4. " + comida_4 + " - " + str(precio_4) + " colones")
    print("5. " + comida_5 + " - " + str(precio_5) + " colones")
    print("6. Salir")

    opcion = int(input("Seleccione una opción (1-6): "))

    if opcion == 6:
        break

    if opcion < 1 or opcion > 6:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        continue

    cantidad = int(input("Ingrese la cantidad de platos: "))

    descuento = 0
    if opcion == 5:
        descuento = 0.3

    if opcion == 1:
        subtotal += precio_1 * cantidad * (1 - descuento)
        if compra != "":
            compra += ", "
        compra += str(cantidad) + " " + comida_1
    elif opcion == 2:
        subtotal += precio_2 * cantidad * (1 - descuento)
        if compra != "":
            compra += ", "
        compra += str(cantidad) + " " + comida_2
    elif opcion == 3:
        subtotal += precio_3 * cantidad * (1 - descuento)
        if compra != "":
            compra += ", "
        compra += str(cantidad) + " " + comida_3
    elif opcion == 4:
        subtotal += precio_4 * cantidad * (1 - descuento)
        if compra != "":
            compra += ", "
        compra += str(cantidad) + " " + comida_4

iva = subtotal * 0.13
total = subtotal + iva

print("\n--- Resumen de compra ---")
print(compra)

print("\nSubtotal: " + str(subtotal) + " colones")
print("IVA (13%): " + str(iva) + " colones")
print("Total a pagar: " + str(total) + " colones")