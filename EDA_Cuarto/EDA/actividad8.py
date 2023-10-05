#se le pide al usuario hacer el cuadro magico
def solicitar_matriz():
    matriz = []
    print("Ingresa los valores de la matriz (fila por fila):")
    for i in range(3):  # Solicitamos una matriz 3x3 
        fila = input(f"Ingresa los valores de la fila {i + 1} separados por espacios: ")
        #se crea una matriz donde hay un numero entero de la variable fila y estos se dividen por columnas 
        valores = [int(x) for x in fila.split()]
        #luego se agregan a la variable matriz, que es el cuadro magico
        matriz.append(valores)
    return matriz

def cuadroM(matriz):
    #se suman la primera fila de la matriz y se encierra en una variable llamada "suma"
    suma = sum(matriz[0])
    
    constante = suma

    for i in range(len(matriz)):
        if sum(matriz[i]) != constante:
            return False

    sumaFila = 0
    # itera a través de las columnas de la matriz. `i` representa el índice de la columna actual.
    for i in range(len(matriz)):
        #itera a través de las filas de la matriz dentro de la columna actual. `j` representa el índice de la fila actual dentro de la columna `i`.
        for j in range(len(matriz[i])):
            #suma el valor del elemento actual al valor acumulado en la variable `sumaFila`. Esto se hace para calcular la suma de la columna actual.
            sumaFila = sumaFila + matriz[j][i]
        if sumaFila != constante:
            return False
        sumaFila = 0
      #inicializamos 2 variables       
    sumaDiagonal1 = 0
    sumaDiagonal2 = 0
    #este for se usa para que del primer lugar que agarre de la primera fila, se le reste un lugar a la segunda fila, formando la diagonal
    for i in range(len(matriz)):
        sumaDiagonal1 += matriz[i][i]
        sumaDiagonal2 += matriz[i][len(matriz) - i - 1]
    if sumaDiagonal1 != constante:
        return False
    if sumaDiagonal2 != constante:
         return False
    return constante

matriz = solicitar_matriz()
resultado = cuadroM(matriz)
if resultado:
    print(f"La constante del cuadro mágico es: {resultado}")
else:
    print("Falso")
