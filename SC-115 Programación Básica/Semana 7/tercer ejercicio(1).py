Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def calcular_costo_paquete(destino, cantidad_personas, mes_viaje):
    # Definir los precios de los paquetes por persona
    precios = {
        "España": 800,
        "Inglaterra": 1200,
        "Brazil": 600,
        "Argentina": 800
    }
    
    # Definir los meses de temporada alta
    meses_temporada_alta = ["Enero", "Julio", "Diciembre"]
    
    # Obtener el precio base del paquete seleccionado
    precio_base = precios[destino]
    
    # Verificar si es temporada alta y aplicar el aumento del 10%
    if mes_viaje in meses_temporada_alta:
        precio_base *= 1.1
    
    # Calcular el costo total por la cantidad de personas
    costo_total = precio_base * cantidad_personas
    
    return costo_total

# Función para mostrar el menú y obtener la selección del usuario
def mostrar_menu():
    print("Bienvenido(a) a la agencia de viajes")
    print("Destinos disponibles:")
    print("1. España")
    print("2. Inglaterra")
    print("3. Brazil")
    print("4. Argentina")
    
    while True:
        opcion = input("Seleccione el número del destino deseado: ")
        
        if opcion in ["1", "2", "3", "4"]:
            return opcion
        else:
            print("Selección inválida. Por favor, ingrese un número válido.")

# Función para obtener la cantidad de personas que van a viajar
def obtener_cantidad_personas():
    while True:
        cantidad = input("Ingrese la cantidad de personas que van a viajar: ")
        
        if cantidad.isdigit():
            return int(cantidad)
        else:
            print("Cantidad inválida. Por favor, ingrese un número válido.")
... 
... # Función para obtener el mes del viaje
... def obtener_mes_viaje():
...     while True:
...         mes = input("Ingrese el mes del viaje (por ejemplo, 'Enero', 'Febrero', etc.): ")
...         
...         if mes in ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]:
...             return mes
...         else:
...             print("Mes inválido. Por favor, ingrese un mes válido.")
... 
... # Función principal
... def main():
...     destino = mostrar_menu()
...     cantidad_personas = obtener_cantidad_personas()
...     mes_viaje = obtener_mes_viaje()
...     
...     # Obtener el nombre del destino seleccionado
...     destinos = {
...         "1": "España",
...         "2": "Inglaterra",
...         "3": "Brazil",
...         "4": "Argentina"
...     }
...     nombre_destino = destinos[destino]
...     
...     # Calcular el costo del paquete seleccionado
...     costo_paquete = calcular_costo_paquete(nombre_destino, cantidad_personas, mes_viaje)
...     
...     print(f"\nDestino seleccionado: {nombre_destino}")
...     print(f"Cantidad de personas: {cantidad_personas}")
...     print(f"Mes del viaje: {mes_viaje}")
...     print(f"Monto a pagar por el paquete seleccionado: ${costo_paquete:.2f}")
... 
... # Ejecutar el programa principal
... main()
