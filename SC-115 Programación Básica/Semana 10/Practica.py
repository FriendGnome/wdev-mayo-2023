# Función para sumar dos matrices de 2x2
def sumar_matrices(matriz1, matriz2):
    suma_matriz = []
    for i in range(2):
        fila = []
        for j in range(2):
            suma = matriz1[i][j] + matriz2[i][j]
            fila.append(suma)
        suma_matriz.append(fila)
    return suma_matriz

# Matriz 1
matriz1 = [[1, 2],
           [3, 4]]

# Matriz 2
matriz2 = [[5, 6],
           [7, 8]]

# Calculamos la suma de las matrices
matriz_suma = sumar_matrices(matriz1, matriz2)

# Mostramos las matrices originales y la suma resultante
print("Matriz 1:")
for fila in matriz1:
    print(fila)

print("\nMatriz 2:")
for fila in matriz2:
    print(fila)

print("\nMatriz Suma:")
for fila in matriz_suma:
    print(fila)