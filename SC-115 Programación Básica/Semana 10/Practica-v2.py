def sumar_matrices(matriz1, matriz2):
    suma_matriz = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            suma_matriz[i][j] = matriz1[i][j] + matriz2[i][j]
    return suma_matriz

def imprimir_matriz(matriz):
    for i in range(2):
        for j in range(2):
            print(matriz[i][j], end=" ")
        print()


matriz1 = [[1, 2],
           [3, 4]]


matriz2 = [[5, 6],
           [7, 8]]

matriz_suma = sumar_matrices(matriz1, matriz2)

print("Matriz 1:")
imprimir_matriz(matriz1)

print("\nMatriz 2:")
imprimir_matriz(matriz2)

print("\nMatriz Suma:")
imprimir_matriz(matriz_suma)