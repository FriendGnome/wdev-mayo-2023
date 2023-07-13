"""
Desarrolle un programa en python que convierta un número a su respectivo valor en base binaria, 
octal y hexadecimal. Cada una de las conversiones debe ser un proceso independiente. El proceso binario 
debe mostrar el resultado los otros dos procesos deben retornar el resultado para ser mostrado desde el 
proceso inicial. Adicionalmente, programe un proceso que reciba dos parámetros (el valor y la base) y que 
muestre el número correspondiente. 
"""

def convertir_binario(numero):
    if numero == 0:
        return '0'

    binario = ''
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero = (numero - residuo) / 2

    return binario

def convertir_octal(numero):
    if numero == 0:
        return '0'

    octal = ''
    while numero > 0:
        residuo = numero % 8
        numero = numero - residuo
        octal = str(residuo) + octal
        numero = numero / 8

    return octal

def convertir_hexadecimal(numero):
    if numero == 0:
        return '0'

    hexadecimal = ''
    while numero > 0:
        residuo = numero % 16
        if residuo < 10:
            hexadecimal = str(residuo) + hexadecimal
        else:
            if residuo == 10:
                hexadecimal = 'A' + hexadecimal
            elif residuo == 11:
                hexadecimal = 'B' + hexadecimal
            elif residuo == 12:
                hexadecimal = 'C' + hexadecimal
            elif residuo == 13:
                hexadecimal = 'D' + hexadecimal
            elif residuo == 14:
                hexadecimal = 'E' + hexadecimal
            elif residuo == 15:
                hexadecimal = 'F' + hexadecimal
        numero = (numero - residuo) // 16

    return hexadecimal

def mostrar_numero(valor, base):
    if base == 2:
        resultado = convertir_binario(valor)
        print("El número en binario es:", resultado)
    elif base == 8:
        resultado = convertir_octal(valor)
        print("El número en octal es:", resultado)
    elif base == 16:
        resultado = convertir_hexadecimal(valor)
        print("El número en hexadecimal es:", resultado)
    else:
        print("Base inválida. Solo se admiten bases 2, 8 y 16.")


numero = int(input("Ingrese un número: "))
mostrar_numero(numero, 2)  
resultado_octal = mostrar_numero(numero, 8)  
resultado_hexadecimal = mostrar_numero(numero, 16)  

