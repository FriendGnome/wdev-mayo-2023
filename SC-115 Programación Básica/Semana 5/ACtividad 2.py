#Actividad Evaluativa Grupo Seis (6) Nombre del Grupo: Grupo Los Erizos
#Integrantes: Corrales Sánchez Camilo, Luna Urbina David Guillermo, 
#Piñas Perez Julio Andres, Hernandez Urbina Eliecer Josue
#Profesor: Salas Sevilla Oscar Francisco

"""
Desarrolle un programa en Python para determinar el pago bruto de varios empleados de una 
empresa.  La empresa paga un “turno ordinario” por las primeras 40 horas trabajadas por cada 
empleado y paga un “turno y medio” por las demás horas extras trabajadas, después de las primeras 
40 horas. Su programa debe permitir solicitar la tarifa por hora del empleado, la cantidad de horas 
trabajadas y desplegar el pago bruto del empleado.  
"""
variable_empleado=int(input("Bienvenido!\n" 
          "Ingrese su número de empleado:\n"
          "1. Corrales Sánchez Camilo\n"
          "2. Luna Urbina David Guillermo\n"
          "3. Piñas Perez Julio Andres\n"
          "4. Hernandez Urbina Eliecer Josue\n"
          "5. Salas Sevilla Oscar Francisco\n"))

if variable_empleado == 1:
    print("Bienvenido: Corrales Sánchez Camilo.")
elif variable_empleado == 2:
    print("Bienvenido: Luna Urbina David Guillermo")
elif variable_empleado == 3:
    print("Bienvenido: Piñas Perez Julio Andres")
elif variable_empleado == 4:
    print("Bienvenido: Hernandez Urbina Eliecer Josue")
elif variable_empleado == 5:
    print("Bienvenido: Salas Sevilla Oscar Francisco")
else:
    print("No es una opción valida, el sistema continuara,\n"
          "contacte a su administrador para ingresar un nuevo empleado.")

  
opcion=int(input("Seleccione una opcion:\n"
        "1.Solicitar la tarifa por hora del empleado y salario Bruto ordinario.\n"
        "2.Solicitar la cantidad de horas trabajadas y salario Bruto personalizado.\n"))

if opcion == 1:
    print("Su tarifa por hora es",3500)
    print("Su pago bruto por jornada de 40 horas es:",140000)
elif opcion == 2:
    horas_trabajadas= int(input("Ingrese el número de horas trabajadas:"))
    if horas_trabajadas <= 40:
        print("Su salario bruto ordinario es igual a:",horas_trabajadas*3500)
    elif horas_trabajadas >= 41:
        horas_extras= horas_trabajadas-40
        print("Su salario bruto personalizado es igual a:",horas_trabajadas*3500+horas_extras*5250)

print("Gracias por usar el programa!")
