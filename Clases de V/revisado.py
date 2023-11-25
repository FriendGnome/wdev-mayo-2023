import csv
import os

arreglo = []
arreglo_producto = []
compras = []
ventas = []
ordenes_compra = []


def agregar_usuario(identificacion, nombre, primer_apellido, segundo_apellido, telefono, correo, provincia, otras_señas):
    for cliente in arreglo:
        if cliente[0] == identificacion:
            print("Este cliente ya existe previamente y no puede ser ingresado de nuevo.")
            return
    arreglo.append([identificacion, nombre, primer_apellido, segundo_apellido, telefono, correo, provincia, otras_señas])

def buscar_usuario(id_usuario):
    if id_usuario >= len(arreglo):
        return "Eso no es ID de un usuario existente."
    else:
        return arreglo[id_usuario]

def actualizar_cliente(id_usuario):
    if id_usuario < len(arreglo):
        cliente_actual = arreglo[id_usuario]
        print("Actualizando información del cliente con ID", id_usuario)

        try:
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
        except ValueError:
            print("Ingrese un valor numérico válido para la identificación y el teléfono.")
    else:
        print("El ID del cliente no existe en la lista.")

def registrar_cliente():
    try:
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
    except ValueError:
        print("Ingrese un valor numérico válido para la identificación y el teléfono.")

def vender_producto(id_cliente):
    productos = input("Ingrese los productos vendidos separados por comas: ").split(",")
    fecha_venta = input("Ingrese la fecha de la venta (dd/mm/aaaa): ")

    ventas_cliente = {
        "id_cliente": id_cliente,
        "productos": productos,
        "fecha_venta": fecha_venta
    }
    ventas.append(ventas_cliente)

    print("Venta registrada exitosamente.")

def listar_productos_comprados(id_cliente):
    productos_comprados = []

    for compra in compras:
        if compra[0] == str(id_cliente):
            productos = compra[1].split(",")
            for producto_id in productos:
                productos_comprados.append(producto_id)

    if productos_comprados:
        print("Productos comprados por el cliente:")
        for producto_id in productos_comprados:
            producto = buscar_producto(int(producto_id))
            if producto:
                print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[3]}")
            else:
                print(f"Producto con ID {producto_id} no encontrado.")
    else:
        print("El cliente no ha realizado ninguna compra.")


def menu_modulo_clientes():
    while True:
        print("*** Módulo de Clientes ***")
        print("1. Registrar un nuevo cliente")
        print("2. Actualizar un cliente existente")
        print("3. Consultar un cliente")
        print("4. Venta de productos")
        print("5. Listado de productos comprados")
        print("6. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            id_cliente = int(input("Ingrese la identificación del cliente que desea actualizar: "))
            actualizar_cliente(id_cliente)
        elif opcion == "3":
            id_cliente = int(input("Ingrese la identificación del cliente que desea consultar: "))
            print(buscar_usuario(id_cliente))
        elif opcion == "4":
            id_cliente = int(input("Ingrese la identificación del cliente que va a realizar la venta: "))
            vender_producto(id_cliente)
        elif opcion == "5":
            id_cliente = int(input("Ingrese la identificación del cliente para listar los productos comprados: "))
            listar_productos_comprados(id_cliente)
        elif opcion == "6":
            return
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def agregar_producto(identificacion, nombre, descripcion, precio, cantidad_existencia, activo):
    for producto in arreglo_producto:
        if producto[0] == identificacion:
            producto[4] += cantidad_existencia
            producto[5] = activo
            print("Producto actualizado exitosamente.")
            return

    arreglo_producto.append([identificacion, nombre, descripcion, precio, cantidad_existencia, activo])
    print("Producto agregado exitosamente.")

def buscar_producto(identificacion):
    for producto in arreglo_producto:
        if producto[0] == identificacion:
            return producto
    return None

def gestionar_productos():
    while True:
        print("**** SISTEMA DE GESTION DE PRODUCTOS ****")
        print("1. Agregar un producto")
        print("2. Consultar un producto")
        print("3. Volver al menú principal")

        entrada_producto = input("Ingrese la opción: ")

        if entrada_producto == "1":
            pass
        elif entrada_producto == "2":
            identificacion = int(input("Ingrese la identificación del producto para buscar información: "))
            producto_encontrado = buscar_producto(identificacion)
            if producto_encontrado:
                print("Información del producto:")
                print("Identificación:", producto_encontrado[0])
                print("Nombre:", producto_encontrado[1])
                print("Descripción:", producto_encontrado[2])
                print("Precio:", producto_encontrado[3])
                print("Cantidad en existencia:", producto_encontrado[4])
                print("Activo:", "Sí" if producto_encontrado[5] else "No")
            else:
                print("Producto no encontrado.")
        elif entrada_producto == "3":
            return
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def aprobar_venta(id_cliente):
    venta_encontrada = False
    for venta in ventas:
        if venta["id_cliente"] == id_cliente:
            venta_encontrada = True

    if venta_encontrada:
        print(f"Venta del cliente {id_cliente} aprobada.")
    else:
        print("Venta no encontrada para el cliente especificado.")

def generar_orden_compra(id_cliente, productos):
    fecha_orden = input("Ingrese la fecha de la orden de compra (dd/mm/aaaa): ")

    orden_compra = {
        "id_cliente": id_cliente,
        "productos": productos,
        "fecha_orden": fecha_orden
    }
    ordenes_compra.append(orden_compra)

    print("Orden de compra generada exitosamente.")

def menu_modulo_administrador():
    condicion3 = True
    while condicion3:
        print("*** Módulo de Administrador ***")
        print("1. Aprobar venta de productos")
        print("2. Generar orden de compra")
        print("3. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_cliente = int(input("Ingrese la identificación del cliente para aprobar su venta: "))
            aprobar_venta(id_cliente)
        elif opcion == "2":
            id_cliente = int(input("Ingrese la identificación del cliente para generar la orden de compra: "))
            productos = input("Ingrese los productos separados por comas: ").split(",")
            generar_orden_compra(id_cliente, productos)
        elif opcion == "3":
            return
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def leer_compras():
    compras = []
    archivo = None
    try:
        archivo = open("compras.csv", "r")
        contenido = archivo.read()
        filas = contenido.split("\n")
        for fila in filas:
            if fila:
                valores = fila.split(",")
                compras.append(valores)
    except FileNotFoundError:
        archivo = None
    except Exception:
        print("Error al leer las compras.")
    if archivo:
        archivo.close()
    return compras

def guardar_compra(id_cliente, productos, fecha):
    archivo = None
    try:
        archivo = open("compras.csv", "a")
        linea = str(id_cliente) + "," + str(productos) + "," + str(fecha) + ";"
        archivo.write(linea)
        archivo.write("\n")  
        archivo.close()
        print("Compra registrada exitosamente.")
    except Exception:
        print("Error al guardar la compra.")

def menu_modulo_compras():
    condicion2 = True
    while condicion2:
        print("*** Módulo de Compras ***")
        print("1. Realizar una compra")
        print("2. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_cliente = int(input("Ingrese la identificación del cliente que realiza la compra: "))
            productos = input("Ingrese los productos separados por comas: ")
            fecha = input("Ingrese la fecha de la compra (dd/mm/aaaa): ")
            guardar_compra(id_cliente, productos, fecha)
        elif opcion == "2":
            return
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            
def guardar_clientes(arreglo):
    with open("clientes.csv", "w") as archivo:
        for cliente in arreglo:
            for i in range(len(cliente)):
                archivo.write(str(cliente[i]))
                if i < len(cliente) - 1:
                    archivo.write(",")
            archivo.write("\n")


def cargar_clientes():
    try:
        with open("clientes.csv", "r") as archivo:
            contenido = archivo.read()
            filas = contenido.split("\n")
            for fila in filas:
                if fila:
                    valores = fila.split(",")
                    arreglo.append(valores)
    except FileNotFoundError:
        pass
    

def menu_principal():
    condicion = True
    cargar_clientes()  
    while condicion == True:
        print("*** Menú Principal ***")
        print("1. Módulo de Clientes")
        print("2. Módulo de Productos")
        print("3. Módulo de Administrador")
        print("4. Módulo de Compras")
        print("5. Guardar datos del cliente y salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_modulo_clientes()
        elif opcion == "2":
            gestionar_productos()
        elif opcion == "3":
            menu_modulo_administrador()
        elif opcion == "4":
            menu_modulo_compras()
        elif opcion == "5":
            guardar_clientes()  
            condicion = False
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


menu_principal()

"""
MODULO CLIENTES

En este módulo se podrá realizar lo siguiente:

El programa debe tener un menú con las siguientes opciones:
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

Nota: Al registrar un nuevo cliente, se debe validar que este no exista previamente; además los clientes deben ser persistentes, 
no se deben perder al cerrar el programa.
Actualizar un cliente existente: Permitiendo modificar toda la información del cliente, únicamente dejando intacto la 
Identificación.
Consultar un cliente: Solicitando la identificación, desplegará la información básica del cliente.
Venta de productos: el cliente pude vender un producto, incluyendo la información del producto, descripción y precio y quedará 
a la espera de la aprobación del administrador.
Listado de productos comprados, mediante la orden de compra, visualizará los productos adquiridos recientemente y el precio 
pagado.
"""


"""
MODULO ADMINISTRADOR

En este módulo se podrá activar los clientes, aceptar los productos de los clientes que desean vender, registrar los productos 
propios del local y visualizar las entregas de los transportistas.

La información para el registro de un producto del local debe contener como mínimo los siguientes datos (puede incluir más 
según se requiere en su análisis):

Identificación del producto.
Nombre del producto.
Descripción del producto.
Precio del producto.
Cantidad de existencia del producto.
Activo o Inactivo

Nota: Se debe validar que el producto no exista, en caso de existir debe permitir aumentar la cantidad de existencias o 
bien cambiar el estado activando o inactivando el producto.

Los productos deben ser persistentes, no se deben eliminar al cerrar el programa
"""


"""
MODULO DE COMPRA

En este módulo el cliente puede realizar una compra; el sistema presentará un listado de los productos habilitados para la 
compra, incluyendo los productos de otros clientes.

El cliente seleccionará el producto deseado y podrá elegir entre agregar otro producto al carrito o finalizar con la compra.

Al finalizar la compra, el sistema imprimirá un número de orden, el monto a pagar según los gastos administrativos, la 
localización de la entrega, el precio de los productos y el 13% de impuesto. Adicionalmente informará al usuario la fecha 
estimada de entrega.

Nota: La fecha estimada de entrega se basa en la fecha del pedido y la próxima disponibilidad de entrega del transportista 
asignado a esa provincia.

Las órdenes de compra deben ser persistentes, no se deben perder al cerrar el programa.
"""


"""
MODULO DE INFORMES

Generará los siguientes informes, para los cuales debe obtener la información de los archivos planos que se grabaron para cada 
uno de los módulos anteriores:

Compras: mostrando la información completa de las compras realizadas y su fecha de registro. Para realizar la búsqueda, se debe 
solicitar la fecha de consulta.

Clientes: mostrando la información de los clientes y su fecha de registro. Para realizar la búsqueda, se debe solicitar 
la fecha de consulta.

"""