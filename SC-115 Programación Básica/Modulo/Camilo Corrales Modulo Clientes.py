#SC-115-Programación Basica
#Avance 2 del Proyecto
#Grupo los Erizos Grupo 3
#Entrega Individual Camilo Corrales
"""
Descripción General del requerimiento Tienda en línea “Intermediación y Venta de productos”

Como parte de la digitalización de modelos de negocio, la tienda “Entrega a Domicilio” a 
decidido establecer su negocio en la WEB inspirado en la tienda AMAZON, razón por la cual 
ustedes han sido contratados para desarrollar una aplicación en Python como primer paso a 
la modernización.

La tienda cuenta con un Administrador, quién es el responsable de activar clientes, administrar 
los productos propios y de terceros, junto con el cobro y la logística de entrega de los 
productos comprados.
Los clientes pueden inscribirse brindando los datos básicos, junto con la dirección de entrega, 
sin embargo, pueden realizar compras o vender productos únicamente si son aceptados por el 
Administrador.
Cuando un cliente quiere realizar una compra, se activa el “carrito de compras”, el cual 
contiene un listado de productos, sus respectivos precios, junto con el 2% de gastos de 
administración y un porcentaje de transporte el cual se desglosa de la siguiente forma:

San José, un 3%
Heredia, Alajuela y Cartago un 5%
Guanacaste, Limón y Puntarenas un 10%.

El local tiene transporte los cinco días a la semana, y cuenta con dos transportistas, sin 
embargo, únicamente puede realizar las entregas de una misma provincia en un mismo día y cada 
transportista no realiza entregas a una misma provincia el mismo día.
"""
#print("3. Venta de Productos")
    #print("4. Listado de Productos")
    #print("5. Consulta de Cliente")

"""
Módulo de Clientes: En este módulo se podrá realizar lo siguiente:

Registrar un nuevo cliente, solicitando la siguiente información:

Identificación.
Nombre
Primer Apellido
Segundo Apellido.
Teléfono
Correo
Provincia de residencia
Otras señas de ubicación.

Nota: Al registrar un nuevo cliente, se debe validar que este no exista previamente; además los 
clientes deben ser persistentes, no se deben perder al cerrar el programa.

-Actualizar un cliente existente: Permitiendo modificar toda la información del cliente, 
únicamente dejando intacto la Identificación.

-Consultar un cliente: Solicitando la identificación, desplegará la información básica del cliente.

-Venta de productos: el cliente puede vender un producto, incluyendo la información del producto, 
descripción y precio y quedará a la espera de la aprobación del administrador.

-Listado de productos comprados, mediante la orden de compra, visualizará los productos

"""
print("Bienvenido a Tienda Online El Canalito")

cliente = "Cliente no ha sido registrado"
condicion = True
condicion_cliente = False
failsafe = False
acumulador = 0


while condicion == True:
    print("***MENU***")
    print("Elija una de las siguientes opciones para continuar:")
    print("1. Registrar un cliente")
    print("2. Actualizar un cliente")
    print("3. Venta de Productos")
    print("4. Listado de Productos")
    print("5. Consulta de Cliente")
    print("6. Salir del Programa")
    opcion_menu=int(input("Ingrese la opción: "))

    if opcion_menu == 1:
             
            nombre = input("Ingrese el nombre del cliente: ")
            identificacion = input("Ingrese el número de identificación nacional en la cedula de identidad: ")
            pais = input("Ingrese el país: ")
            provincia = input("Ingrese la provincia: ")
            canton = input("Ingrese el cantón: ")
            distrito = input("Ingrese el distrito: ")
            direccion = input("Ingrese la dirección: ")
            edad = int(input("Ingrese la edad: "))
            forma_pago = input("Ingrese la forma de pago (efectivo, transferencia, tarjeta de crédito): ")
            if condicion_cliente == True:
                print("Lo lamento, el sistema solo puede registrar un solo cliente y este ya está registrado. Debe ingresar en la opcion de actualizar. ")
            elif cliente != nombre:
                print("¡Cliente registrado exitosamente!")
                nombre1 = nombre
                cliente=nombre1
                identificacion1 = identificacion
                pais1 = pais
                provincia1 = provincia
                canton1 = canton
                distrito1 = distrito
                direccion1 = direccion
                edad1 = edad
                forma_pago1 = forma_pago
                condicion_cliente = True
                print("El administrado contactará al cliente en 3-5 días hábiles si el cliente cumple los requisitos para realizar compras o vender productos.")
            else:
                 print ("El cliente con este nombre ya fue registrado y no se puede registrar de nuevo")
    
    elif opcion_menu == 2:
        nombre = input("Ingrese el nombre del cliente como aparece en el registro: ")
        nombre2 = input("Ingrese el nombre del cliente de nuevo si desea actualizarlo: ")
        identificacion = input("Ingrese el número de identificación: ")
        pais = input("Ingrese el país: ")
        provincia = input("Ingrese la provincia: ")
        canton = input("Ingrese el cantón: ")
        distrito = input("Ingrese el distrito: ")
        direccion = input("Ingrese la dirección: ")
        edad = int(input("Ingrese la edad: "))
        forma_pago = input("Ingrese la forma de pago (efectivo, transferencia, tarjeta de crédito): ")
        
        if cliente == nombre:
            print("¡Cliente actualizado exitosamente!")
            nombre1 = nombre2
            cliente=nombre1
            identificacion1 = identificacion
            pais1 = pais
            provincia1 = provincia
            canton1 = canton
            distrito1 = distrito
            direccion1 = direccion
            edad1 = edad
            forma_pago1 = forma_pago
        elif cliente != nombre or condicion_cliente == False:
            print ("El cliente no se puede actualizar porque no existe oh porque ningun cliente ha sido registrado. Debe digitar el nombre del cliente tal como aparece en el registro.")

    elif opcion_menu == 3:
        if condicion_cliente == True:
            print("Lo lamento el cliente aún no ha sido aceptado por el Administrador y esta opción no está habilitada.")
        else:
            print("Ningun cliente ha sido registrado. Esta opción no está habilitada.")
    elif opcion_menu == 4:
        if condicion_cliente == True:
            print("Lo lamento el cliente aún no ha sido aceptado por el Administrador y esta opción no está habilitada.")
        else:
            print("Ningun cliente ha sido registrado. Esta opción no está habilitada.")
    elif opcion_menu == 5:
        print("Nombre del cliente:", nombre1)
        print("Número de identificación:", identificacion1)
        print("País:", pais1)
        print("Provincia:", provincia1)
        print("Canton:", canton1)
        print("Distrito:", distrito1)
        print("Direccion:", direccion1)
        print("Edad:", edad1)
        print("Forma de pago:", forma_pago1)
    elif opcion_menu == 6:
        condicion = False
    elif opcion_menu > 6 or opcion_menu < 1:
        print("Opción Invalida.")

print("El programa terminará. Gracias por preferir Tienda Online el Canalito")

