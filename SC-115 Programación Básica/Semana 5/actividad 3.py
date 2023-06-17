#Actividad Evaluativa 
#Integrante: Corrales Sánchez Camilo,
#Profesor: Salas Sevilla Oscar Francisco
#Nota(los miembros de mi grupo usaron el punto dos de mi entrega para su grupo
#con mi permiso pero igual quería entregar el que hize por aparte)
"""
3.Elabore un programa en Python que, solicite al usuario el precio de cuatro productos diferentes y 
tras sumarlos, si el monto es mayor a 15 mil colones, le aplique un descuento del 10%, mostrando 
por pantalla el resultado final al cliente.
"""
precio1 = float(input("Ingrese el precio del primer producto: "))
precio2 = float(input("Ingrese el precio del segundo producto: "))
precio3 = float(input("Ingrese el precio del tercer producto: "))
precio4 = float(input("Ingrese el precio del cuarto producto: "))

subtotal = precio1 + precio2 + precio3 + precio4

if subtotal > 15000:
    descuento = subtotal * 0.1
    total = subtotal - descuento
    print("El monto total con descuento es de:", total, "colones.")
else:
    print("El monto total es de:", subtotal, "colones.")

print("Gracias por usar el programa!")
