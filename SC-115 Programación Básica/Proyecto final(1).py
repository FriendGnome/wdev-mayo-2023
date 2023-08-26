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
        return "Eso no es ID de un usuario existente."
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

def agregar_producto(nombre, descripcion, precio):
    arreglo_producto.append([nombre, descripcion, precio])
    id_producto = len(arreglo_producto) - 1
    print("ID del Producto:", id_producto)

def buscar_producto(id_producto):
    if id_producto >= len(arreglo_producto):
        return "Eso no es ID de un producto existente."
    else:
        return arreglo_producto[id_producto]

def gestionar_productos():
    print("**** SISTEMA DE GESTION DE PRODUCTOS ****")
    print("1. Agregar un producto")
    print("2. Consultar un producto")
    print("3. Volver al menú principal")

    entrada_producto = input("Ingrese la opción: ")

    if entrada_producto == "1":
        nombre = input("Ingrese el nombre del producto: ")
        descripcion = input("Ingrese la descripción del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        agregar_producto(nombre, descripcion, precio)
    elif entrada_producto == "2":
        id_producto = int(input("Ingrese un ID de producto para buscar información: "))
        print(buscar_producto(id_producto))
    elif entrada_producto == "3":
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
