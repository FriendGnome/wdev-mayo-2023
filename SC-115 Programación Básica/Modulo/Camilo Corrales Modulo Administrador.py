#SC-115-Programación Basica
#Avance 2 del Proyecto
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

-----Listado de productos comprados, mediante la orden de compra, visualizará los productos-----

"""
arreglo = []
arreglo_producto = []

def agregar_usuario(identificacion, nombre, primer_apellido, segundo_apellido, telefono, correo, provincia, otras_señas):
    for cliente in arreglo:
        if cliente[0] == identificacion:
            print("Este cliente ya existe previamente y no puede ser ingresado de nuevo.")
            return

    arreglo.append([identificacion, nombre, primer_apellido, segundo_apellido, telefono, correo, provincia, otras_señas])

def buscar_usuario(id_usuario):
    if id_usuario >= len(arreglo):
        return print("Eso no es ID de un usuario existente.")
    else:
        return arreglo[id_usuario]

def actualizar_cliente(id_usuario):
    if id_usuario < len(arreglo):
        cliente_actual = arreglo[id_usuario]
        print("Actualizando información del cliente con ID", id_usuario)

        identificacion = int(input("Ingrese la nueva identificacion nacional del usuario: "))
        nombre = input("Ingrese el nuevo nombre del cliente: ")
        primer_apellido = input("Ingrese el nuevo primer apellido del cliente: ")
        segundo_apellido = input("Ingrese el nuevo segundo apellido del cliente: ")
        telefono = int(input("Ingrese el nuevo teléfono del cliente: "))
        correo = input("Ingrese el nuevo correo del cliente: ")
        provincia = input("Ingrese la nueva provincia del cliente: ")
        otras_señas = input("Ingrese de nuevo otras señas actualizadas que indiquen su dirección completa:")

        cliente_actual[0] = identificacion
        cliente_actual[1] = nombre
        cliente_actual[2] = primer_apellido
        cliente_actual[3] = segundo_apellido
        cliente_actual[4] = telefono
        cliente_actual[5] = correo
        cliente_actual[6] = provincia
        cliente_actual[7] = otras_señas
        print("Cliente actualizado exitosamente.")
    else:
        print("El ID del cliente no existe en la lista.")

def registrar_cliente():
    identificacion = int(input("Ingrese la identificacion nacional del usuario: "))
    nombre = input("Ingrese el nombre del usuario: ")
    primer_apellido = input("Ingrese el primer apellido del usuario: ")
    segundo_apellido = input("Ingrese el segundo apellido del usuario: ")
    telefono = int(input("Ingrese el telefono del usuario: "))
    correo = input("Ingrese el correo del usuario: ")
    provincia = input("Ingrese la provincia del usuario: ")
    otras_señas = input("Ingrese otras señas que indiquen su dirección completa:")
    agregar_usuario(identificacion, nombre, primer_apellido, segundo_apellido, telefono, correo, provincia, otras_señas)
    id_usuario = len(arreglo) - 1
    print("El ID del Usuario es:", id_usuario)
    print("Por favor guarde el ID si desea consultar este usuario en el futuro.")

def agregar_producto(nombre, descripcion, precio, id_cliente, aprobacion_administrador):
    arreglo_producto.append([nombre, descripcion, precio, id_cliente, aprobacion_administrador])
    id_producto = len(arreglo_producto) - 1
    print("ID del Producto:", id_producto)
    print("Si el cliente listado abajo puede vender este producto oh no quedará a la espera de la aprobación de un administrador.")
    print(buscar_usuario(id_cliente))

def buscar_producto(id_producto):
    if id_producto >= len(arreglo_producto):
        return print("Eso no es ID de un producto existente.")
    else:
        if arreglo_producto[id_producto,4] == False:
            return print( "El producto no ha sido aprobado para venta por el administrador", arreglo_producto[id_producto])
        else:
            return print ("El producto a ha sido aprobado para venta por el administrador", arreglo_producto[id_producto])

#PENDING
def carrito_compra(): #PENDING
    print("PENDING")#PENDING
    #PENDING

def gestionar_productos():
    print("**** SISTEMA DE GESTION DE PRODUCTOS ****")
    print("1. Agregar un producto para venta")
    print("2. Consultar un producto agregado para venta")
    print("3. Crear un carrito de compras")
    print("4. Volver al menú principal")
    
    entrada_producto = input("Ingrese la opción: ")
    
    if entrada_producto == "1":
        nombre = input("Ingrese el nombre del producto: ")
        descripcion = input("Ingrese la descripción del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        id_cliente = input("Ingrese el id del cliente que desea vender este producto")
        aprobacion_administrador = False
        agregar_producto(nombre, descripcion, precio, id_cliente, aprobacion_administrador)
    elif entrada_producto == "2":
        id_producto = int(input("Ingrese un ID de producto para buscar información: "))
        print(buscar_producto(id_producto))
    elif entrada_producto == "3":
        carrito_compra()
    elif entrada_producto == "4":
        return
    else:
        print("Entrada no válida. Por favor ingrese una opción válida.")
        gestionar_productos()

condicion_menu = True
while condicion_menu:
    print("***MENU***")
    print("Elija una de las siguientes opciones para continuar:")
    print("1. Registrar un cliente")
    print("2. Consultar un cliente")
    print("3. Actualizar un cliente")
    print("4. Ingresar al Sistema de Gestion de Productos")
    print("5. Salir del Programa")
    entrada_usuario = input("Ingrese la opción:")

    if entrada_usuario == "1":
        registrar_cliente()
    elif entrada_usuario == "2":
        id_usuario = int(input("Ingrese un ID de usuario para buscar información: "))
        print(buscar_usuario(id_usuario))
    elif entrada_usuario == "3":
        id_usuario = int(input("Ingrese el ID del cliente que desea actualizar: "))
        actualizar_cliente(id_usuario)
    elif entrada_usuario == "4":
        gestionar_productos()
    elif entrada_usuario == "5":
        condicion_menu = False
    else:
        print("Entrada no válida. Por favor ingrese una opción válida.")

print("Programa finalizado.")


"""
Módulo 2: Módulo de Administrador

En este módulo se podrá activar los clientes, aceptar los productos de los clientes que desean vender, registrar 
los productos propios del local y visualizar las entregas de los transportistas.

La información para el registro de un producto del local debe contener como mínimo los siguientes datos (puede incluir más según se requiere en su análisis):

Identificación del producto.
Nombre del producto.
Descripción del producto.
Precio del producto.
Cantidad de existencia del producto.
Activo o Inactivo

Nota: Se debe validar que el producto no exista, en caso de existir debe permitir aumentar la cantidad de existencias o bien cambiar el estado activando o inactivando el producto.

Los productos deben ser persistentes, no se deben eliminar al cerrar el programa.

"""


