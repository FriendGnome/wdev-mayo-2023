temperatura = float(input("Ingrese la temperatura: "))
medida = input("Ingrese la unidad de medida (celsius o fahrenheit): ")

if medida == "celsius":
    conversion = (temperatura * 9/5) + 32
    medida = "fahrenheit"
    print(f"La temperatura convertida es: "+ str(conversion) + " " + medida)
elif medida == "fahrenheit":
    conversion = (temperatura - 32) * 5/9
    medida = "celsius"
    print(f"La temperatura convertida es: "+ str(conversion) + " " + medida)
else:
    print("Unidad de medida no válida. Debe escribir celsius o fahrenheit en minuscula")

