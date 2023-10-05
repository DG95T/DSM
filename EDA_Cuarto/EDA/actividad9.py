# Función para leer una matriz de tamaño 2x2
def leer_matriz():
    matriz = []
    for i in range(2):
        fila = []
        for j in range(2):
            valor = float(input(f"Ingrese el valor para la posición [{i+1}][{j+1}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

# Función para sumar dos matrices
def suma_matrices(matriz1, matriz2):
    resultado = []
    for i in range(2):
        fila = []
        for j in range(2):
            suma = matriz1[i][j] + matriz2[i][j]
            fila.append(suma)
        resultado.append(fila)
    return resultado

# Función para restar dos matrices
def resta_matrices(matriz1, matriz2):
    resultado = []
    for i in range(2):
        fila = []
        for j in range(2):
            resta = matriz1[i][j] - matriz2[i][j]
            fila.append(resta)
        resultado.append(fila)
    return resultado

# Función para multiplicar dos matrices
def multiplicacion_matrices(matriz1, matriz2):
    resultado = []
    for i in range(2):
        fila = []
        for j in range(2):
            producto = matriz1[i][j] * matriz2[i][j]
            fila.append(producto)
        resultado.append(fila)
    return resultado

# Función para dividir dos matrices
def division_matrices(matriz1, matriz2):
    resultado = []
    for i in range(2):
        fila = []
        for j in range(2):
            if matriz2[i][j] != 0:
                division = matriz1[i][j] / matriz2[i][j]
                fila.append(division)
            else:
                fila.append("Indefinido (división por cero)")
        resultado.append(fila)
    return resultado

# Main
print("Ingrese la primera matriz:")
matriz1 = leer_matriz()

print("\nIngrese la segunda matriz:")
matriz2 = leer_matriz()

# Realizamos las operaciones
resultado_suma = suma_matrices(matriz1, matriz2)
resultado_resta = resta_matrices(matriz1, matriz2)
resultado_multiplicacion = multiplicacion_matrices(matriz1, matriz2)
resultado_division = division_matrices(matriz1, matriz2)

# Mostramos los resultados
print("\nResultado de la suma de matrices:")
for fila in resultado_suma:
    print(fila)

print("\nResultado de la resta de matrices:")
for fila in resultado_resta:
    print(fila)

print("\nResultado de la multiplicación de matrices:")
for fila in resultado_multiplicacion:
    print(fila)

print("\nResultado de la división de matrices:")
for fila in resultado_division:
    print(fila)
