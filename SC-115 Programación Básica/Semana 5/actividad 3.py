#Actividad Evaluativa Grupo Seis (6) Nombre del Grupo: Grupo Los Erizos
#Integrantes: Corrales Sánchez Camilo, Luna Urbina David Guillermo, 
#Piñas Perez Julio Andres, Hernandez Urbina Eliecer Josue
#Profesor: Salas Sevilla Oscar Francisco
"""
Elabore un programa en Python que, solicite al usuario el precio de cuatro productos diferentes y 
tras sumarlos, si el monto es mayor a 15 mil colones, le aplique un descuento del 10%, mostrando 
por pantalla el resultado final al cliente.
"""

print("10% de descuento por compras mayores a 15000 colones")
art1= float(input("ingrese el precio de su articulo:"))
art2= float(input("ingrese el precio de su articulo:"))
art3= float(input("ingrese el precio de su articulo:"))
art4= float(input("ingrese el precio de su articulo:"))
subtotal= art1+art2+art3+art4
if subtotal<=15000:
            print("Su total a pagar es:", subtotal)
else:
    print("Su total a pagar es:", subtotal-(subtotal*0.10))
