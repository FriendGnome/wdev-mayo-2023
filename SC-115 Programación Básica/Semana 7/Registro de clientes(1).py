print("Bienvenido a hotel El Canalito")

clientes = []  

while True:
    print("Bienvenido al registro de clientes!")
    opcion = input("¿Desea registrar un nuevo cliente? (s/n): ")

    if opcion.lower() == 'n':
        break

    
    nombre = input("Ingrese el nombre del cliente: ")
    identificacion = input("Ingrese el número de identificación: ")
    pais = input("Ingrese el país: ")
    provincia = input("Ingrese la provincia: ")
    canton = input("Ingrese el cantón: ")
    distrito = input("Ingrese el distrito: ")
    direccion = input("Ingrese la dirección: ")
    edad = int(input("Ingrese la edad: "))
    forma_pago = input("Ingrese la forma de pago (efectivo, transferencia, tarjeta de crédito): ")

    
    personas_acompanantes = int(input("¿Cuántas personas lo acompañan?: "))
    acompanantes = []
    for i in range(personas_acompanantes):
        print(f"\nDatos de la persona {i+1}:")
        nombre_acompanante = input("Ingrese el nombre: ")
        identificacion_acompanante = input("Ingrese el número de identificación: ")
        edad_acompanante = int(input("Ingrese la edad: "))
        acompanante = {
            'nombre': nombre_acompanante,
            'identificacion': identificacion_acompanante,
            'edad': edad_acompanante
        }
        acompanantes.append(acompanante)

    
    cliente = {
        'nombre': nombre,
        'identificacion': identificacion,
        'pais': pais,
        'provincia': provincia,
        'canton': canton,
        'distrito': distrito,
        'direccion': direccion,
        'edad': edad,
        'forma_pago': forma_pago,
        'acompanantes': acompanantes
    }

    
    clientes.append(cliente)
    print("¡Cliente registrado exitosamente!")


print("\n--- Clientes registrados ---")
for cliente in clientes:
    print("\nNombre:", cliente['nombre'])
    print("Identificación:", cliente['identificacion'])
    print("País:", cliente['pais'])
    print("Provincia:", cliente['provincia'])
    print("Cantón:", cliente['canton'])
    print("Distrito:", cliente['distrito'])
    print("Dirección:", cliente['direccion'])
    print("Edad:", cliente['edad'])
    print("Forma de pago:", cliente['forma_pago'])
    print("Acompañantes:")
    for acompanante in cliente['acompanantes']:
        print("- Nombre:", acompanante['nombre'])
        print("  Identificación:", acompanante['identificacion'])
        print("  Edad:", acompanante['edad'])
