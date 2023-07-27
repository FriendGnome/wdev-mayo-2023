def buscar_producto(productos, id_producto):
    for producto in productos:
        if producto[0] == id_producto:
            return producto
    return None

def agregar_producto():
    id_producto = input("Ingrese el ID del producto: ")
    producto_existente = buscar_producto(productos, id_producto)

    if producto_existente:
        print("El producto ya existe:")
        print("Nombre:", producto_existente[1])
        print("Descripción:", producto_existente[2])
        print("Precio:", producto_existente[3])
        print("Cantidad de existencia:", producto_existente[4])
        print("Estado:", "Activo" if producto_existente[5] else "Inactivo")
        opcion = input("¿Desea aumentar la cantidad de existencia o cambiar el estado? (cantidad/estado/nada): ")

        if opcion.lower() == 'cantidad':
            cantidad_aumentar = int(input("Ingrese la cantidad a aumentar: "))
            producto_existente[4] += cantidad_aumentar
        elif opcion.lower() == 'estado':
            nuevo_estado = input("Ingrese el nuevo estado (activo/inactivo): ")
            producto_existente[5] = True if nuevo_estado.lower() == 'activo' else False
    else:
        nombre_producto = input("Ingrese el nombre del producto: ")
        descripcion_producto = input("Ingrese la descripción del producto: ")
        precio_producto = float(input("Ingrese el precio del producto: "))
        cantidad_producto = int(input("Ingrese la cantidad de existencia del producto: "))
        estado_producto = True  
        productos.append([id_producto, nombre_producto, descripcion_producto, precio_producto, cantidad_producto, estado_producto])

    print("Producto agregado o actualizado exitosamente.")

def mostrar_productos():
    if not productos:
        print("No hay productos registrados.")
    else:
        print("Productos registrados:")
        for producto in productos:
            print("ID:", producto[0])
            print("Nombre:", producto[1])
            print("Descripción:", producto[2])
            print("Precio:", producto[3])
            print("Cantidad de existencia:", producto[4])
            print("Estado:", "Activo" if producto[5] else "Inactivo")
            print("-" * 20)

if __name__ == "__main__":
    productos = []  
    while True:
        print("\n--- Sistema de Gestión de Productos ---")
        print("1. Agregar o actualizar producto")
        print("2. Mostrar productos")
        print("3. Salir")
        opcion = input("Seleccione una opción (1/2/3): ")

        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            mostrar_productos()
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
