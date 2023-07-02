print("Bienvenido a hotel El Canalito")

cliente = "Cliente 1"
condicion = True
failsafe = False

while condicion == True:
    print("Este programa tiene la función de Registrar Clientes nuevos al Hotel.")
    opcion = input("¿Desea registrar un nuevo cliente? (s/n): ")

    if opcion == 's':
        nombre = input("Ingrese el nombre del cliente: ")
        identificacion = input("Ingrese el número de identificación: ")
        pais = input("Ingrese el país: ")
        provincia = input("Ingrese la provincia: ")
        canton = input("Ingrese el cantón: ")
        distrito = input("Ingrese el distrito: ")
        direccion = input("Ingrese la dirección: ")
        edad = int(input("Ingrese la edad: "))
        forma_pago = input("Ingrese la forma de pago (efectivo, transferencia, tarjeta de crédito): ")
        print("¡Cliente registrado exitosamente!")
        failsafe == True

    if opcion == 's':
        condicion == False

print("Su cliente fue registrado exitosamente. Elija una de las siguientes opciones")

print("\n--- Clientes registrados ---")
print("\nNombre:", nombre)
print("Identificación:", identificacion)
print("País:", pais)
print("Provincia:", provincia)
print("Cantón:", canton)
print("Distrito:", distrito)
print("Dirección:", direccion)
print("Edad:", edad)
print("Forma de pago:", forma_pago)