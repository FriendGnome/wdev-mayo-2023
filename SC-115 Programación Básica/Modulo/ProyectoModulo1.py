#Proyecto de SC-115 Programación Básica Modulo 1
#Integrantes: Corrales Sánchez Camilo, Luna Urbina David Guillermo, 
#Piñas Perez Julio Andres, Hernandez Urbina Eliecer Josue
#Profesor: Salas Sevilla Oscar Francisco

#Modulo 1:⦁	
"""
El programa debe tener un menú con las siguientes opciones:
⦁	Módulo de Clientes: En este módulo se podrá realizar lo siguiente:

⦁	Registrar un nuevo cliente, solicitando la siguiente información:

⦁	Identificación.
⦁	Nombre
⦁	Primer Apellido
⦁	Segundo Apellido.
⦁	Teléfono
⦁	Correo
⦁	Provincia de residencia
⦁	Otras señas de ubicación.

Nota: Al registrar un nuevo cliente, se debe validar que este no exista previamente; además los clientes deben ser persistentes, no se deben perder al cerrar el programa.
⦁	Actualizar un cliente existente: Permitiendo modificar toda la información del cliente, únicamente dejando intacto la Identificación.
⦁	Consultar un cliente: Solicitando la identificación, desplegará la información básica del cliente.
⦁	Venta de productos: el cliente pude vender un producto, incluyendo la información del producto, descripción y precio y quedará a la espera de la aprobación del administrador.
⦁	Listado de productos comprados, mediante la orden de compra, visualizará los productos adquiridos recientemente y el precio pagado.


class Cliente:
    def __init__(self, identificacion, nombre, primer_apellido, segundo_apellido, telefono, correo, provincia, otras_senas):
        self.identificacion = identificacion
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.telefono = telefono
        self.correo = correo
        self.provincia = provincia
        self.otras_senas = otras_senas

class Producto:
    def __init__(self, nombre, descripcion, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

class Programa:
    def __init__(self):
        self.clientes = []
        self.productos_comprados = []

    def menu_principal(self):
        while True:
            print("\n-- Menú Principal --")
            print("1. Módulo de Clientes")
            print("2. Venta de Productos")
            print("3. Listado de Productos Comprados")
            print("4. Salir")

            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                self.menu_clientes()
            elif opcion == "2":
                self.venta_productos()
            elif opcion == "3":
                self.listado_productos_comprados()
            elif opcion == "4":
                break
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.")

    def menu_clientes(self):
        while True:
            print("\n-- Módulo de Clientes --")
            print("1. Registrar un nuevo cliente")
            print("2. Actualizar un cliente existente")
            print("3. Consultar un cliente")
            print("4. Volver al Menú Principal")

            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                self.registrar_cliente()
            elif opcion == "2":
                self.actualizar_cliente()
            elif opcion == "3":
                self.consultar_cliente()
            elif opcion == "4":
                break
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.")

    def registrar_cliente(self):
        print("\n-- Registrar un nuevo cliente --")
        identificacion = input("Identificación: ")

        # Verificar si el cliente ya existe
        if self.buscar_cliente(identificacion) is not None:
            print("El cliente ya existe.")
            return

        nombre = input("Nombre: ")
        primer_apellido = input("Primer Apellido: ")
        segundo_apellido = input("Segundo Apellido: ")
        telefono = input("Teléfono: ")
        correo = input("Correo: ")
        provincia = input("Provincia de residencia: ")
        otras_senas = input("Otras señas de ubicación: ")

        cliente = Cliente(identificacion, nombre, primer_apellido, segundo_apellido, telefono, correo, provincia, otras_senas)
        self.clientes.append(cliente)

        print("Cliente registrado exitosamente.")

    def buscar_cliente(self, identificacion):
        for cliente in self.clientes:
            if cliente.identificacion == identificacion:
                return cliente
        return None

    def actualizar_cliente(self):
        print("\n-- Actualizar un cliente existente --")
        identificacion = input("Identificación del cliente a actualizar: ")
        cliente = self.buscar_cliente(identificacion)

        if cliente is None:
            print("El cliente no existe.")
            return

        print("Información actual del cliente:")
        print("Identificación:", cliente.identificacion)
        print("Nombre:", cliente.nombre)
        print("Primer Apellido:", cliente.primer_apellido)
        print("Segundo Apellido:", cliente.segundo_apellido)
        print("Teléfono:", cliente.telefono)
        print("Correo:", cliente.correo)
        print("Provincia de residencia:", cliente.provincia)
        print("Otras señas de ubicación:", cliente.otras_senas)

        print("\nIngrese la nueva información del cliente:")
        nombre = input("Nombre: ")
        primer_apellido = input("Primer Apellido: ")
        segundo_apellido = input("Segundo Apellido: ")
        telefono = input("Teléfono: ")
        correo = input("Correo: ")
        provincia = input("Provincia de residencia: ")
        otras_senas = input("Otras señas de ubicación: ")

        # Actualizar la información del cliente
        cliente.nombre = nombre
        cliente.primer_apellido = primer_apellido
        cliente.segundo_apellido = segundo_apellido
        cliente.telefono = telefono
        cliente.correo = correo
        cliente.provincia = provincia
        cliente.otras_senas = otras_senas

        print("Cliente actualizado exitosamente.")

    def consultar_cliente(self):
        print("\n-- Consultar un cliente --")
        identificacion = input("Identificación del cliente a consultar: ")
        cliente = self.buscar_cliente(identificacion)

        if cliente is None:
            print("El cliente no existe.")
            return

        print("Información del cliente:")
        print("Identificación:", cliente.identificacion)
        print("Nombre:", cliente.nombre)
        print("Primer Apellido:", cliente.primer_apellido)
        print("Segundo Apellido:", cliente.segundo_apellido)
        print("Teléfono:", cliente.telefono)
        print("Correo:", cliente.correo)
        print("Provincia de residencia:", cliente.provincia)
        print("Otras señas de ubicación:", cliente.otras_senas)

    def venta_productos(self):
        print("\n-- Venta de Productos --")
        identificacion = input("Identificación del cliente: ")
        cliente = self.buscar_cliente(identificacion)

        if cliente is None:
            print("El cliente no existe.")
            return

        nombre_producto = input("Nombre del producto: ")
        descripcion_producto = input("Descripción del producto: ")
        precio_producto = float(input("Precio del producto: "))

        producto = Producto(nombre_producto, descripcion_producto, precio_producto)
        self.productos_comprados.append((cliente, producto))

        print("Venta de producto registrada exitosamente.")

    def listado_productos_comprados(self):
        print("\n-- Listado de Productos Comprados --")

        if len(self.productos_comprados) == 0:
            print("No se han registrado compras de productos.")
            return

        for cliente, producto in self.productos_comprados:
            print("Cliente:", cliente.nombre, cliente.primer_apellido)
            print("Producto:", producto.nombre)
            print("Descripción:", producto.descripcion)
            print("Precio:", producto.precio)
            print("------------------------------------")

programa = Programa()
programa.menu_principal()
"""