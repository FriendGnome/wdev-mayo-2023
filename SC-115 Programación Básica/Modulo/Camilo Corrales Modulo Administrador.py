
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

-Listado de productos comprados, mediante la orden de compra, visualizará los productos

"""
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

matriz = []

def agregar_usuario(nombre, pais, edad):
    matriz.append([nombre, pais, edad])

def buscar_usuario(id_usuario):
    if id_usuario >= len(matriz):
        return print("Eso no es un usuario valido.")
    return matriz[id_usuario]

condicion = True
while condicion:
    print("***MENU***")
    print("Elija una de las siguientes opciones para continuar:")
    print("1. Registrar un cliente")
    print("2. Consultar un cliente")
    print("3. Salir")
    entrada_usuario = int(input("Ingrese la opción:"))
    
    if entrada_usuario == 3:
        condicion = False
    elif entrada_usuario == 1:
        nombre = input("Ingrese el nombre del usuario: ")
        pais = input("Ingrese el país del usuario: ")
        edad = int(input("Ingrese la edad del usuario: "))
        agregar_usuario(nombre, pais, edad)
        id_usuario = len(matriz) - 1
        print("El ID del Usuario es:", id_usuario)
        print("Por favor guarde el ID si desea consultar este usuario en el futuro.")
    elif entrada_usuario == 2:
        id_usuario = int(input("Ingrese un ID de usuario para buscar información: "))
        print(buscar_usuario(id_usuario))
    else:
        print("Entrada no válida. Por favor ingrese una opción válida.")
        print()

print("Programa finalizado.")