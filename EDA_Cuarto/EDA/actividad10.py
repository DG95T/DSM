#Practica 10

class EliminacionGaussiana:
    def __init__(self, matriz):
        self.matriz = matriz

    def intercambiar_filas(self, fila1, fila2):
        self.matriz[fila1], self.matriz[fila2] = self.matriz[fila2], self.matriz[fila1]

    def multiplicar_fila(self, fila, constante):
        self.matriz[fila] = [elemento * constante for elemento in self.matriz[fila]]

    def restar_filas(self, fila1, fila2, factor):
        self.matriz[fila1] = [elem1 - elem2 * factor for elem1, elem2 in zip(self.matriz[fila1], self.matriz[fila2])]

    def imprimir_matriz(self):
        for fila in self.matriz:
            print(fila)

    def gauss(self):
        filas, columnas = len(self.matriz), len(self.matriz[0])

        for i in range(min(filas, columnas - 1)):
            # Hacer ceros debajo del elemento diagonal
            for j in range(i + 1, filas):
                factor = self.matriz[j][i] / self.matriz[i][i]
                self.restar_filas(j, i, factor)

        # Hacer ceros por encima del elemento diagonal
        for i in range(filas - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                factor = self.matriz[j][i] / self.matriz[i][i]
                self.restar_filas(j, i, factor)

        # Normalizar filas
        for i in range(filas):
            factor = 1 / self.matriz[i][i]
            self.multiplicar_fila(i, factor)

        self.imprimir_matriz()


# Ejemplo de uso
matriz_ejemplo = [
    [2, -1, 1],
    [-3, 0, 1],
    [-1, 3, -2]
]

gauss_solver = EliminacionGaussiana(matriz_ejemplo)
print("Matriz original:")
gauss_solver.imprimir_matriz()

print("\nAplicando eliminación de Gauss:")
gauss_solver.gauss()

print("\nMatriz después de Gauss:")
gauss_solver.imprimir_matriz()