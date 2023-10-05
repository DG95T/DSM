import flet as ft
import random

class MatrizOperaciones:
    def __init__(self, filas, columnas, min_valor=1, max_valor=100):
        self.filas = filas
        self.columnas = columnas
        self.min_valor = min_valor
        self.max_valor = max_valor
        self.matriz = self.crear_matriz_aleatoria()

    def crear_matriz_aleatoria(self):
        # Crea una matriz de números aleatorios entre min_valor y max_valor
        matriz = []
        for i in range(self.filas):
            fila = [random.randint(self.min_valor, self.max_valor) for _ in range(self.columnas)]
            matriz.append(fila)
        return matriz

    def sumar_filas(self):
        # Calcula la suma de cada fila de la matriz
        return [sum(fila) for fila in self.matriz]

    def promedio_filas(self):
        # Calcula el promedio de cada fila de la matriz
        return [sum(fila) / self.columnas for fila in self.matriz]

    def sumar_columnas(self):
        # Calcula la suma de cada columna de la matriz
        return [sum(self.matriz[i][j] for i in range(self.filas)) for j in range(self.columnas)]

    def promedio_columnas(self):
        # Calcula el promedio de cada columna de la matriz
        return [sum(self.matriz[i][j] for i in range(self.filas)) / self.filas for j in range(self.columnas)]


def main(page: ft.page):
    def EventoClickMatriz(e):
        page.controls.pop(2)

        def mostrar_matriz(self):
            # Muestra la matriz en la consola
            print("Matriz:")
            for fila in self.matriz:
                print(" ".join(map(str, fila)))


    def EventoClickResult(e):
        page.controls.pop(2)
        def mostrar_resultados(self):
            # Muestra los resultados en la consola
            print("\nResultados:")
            suma_filas = self.sumar_filas()
            promedio_filas = self.promedio_filas()
            suma_columnas = self.sumar_columnas()
            promedio_columnas = self.promedio_columnas()

            for i in range(self.filas):
                print(f"Fila {i + 1}: Suma = {suma_filas[i]}, Promedio = {promedio_filas[i]}")

            for j in range(self.columnas):
                print(f"Columna {j + 1}: Suma = {suma_columnas[j]}, Promedio = {promedio_columnas[j]}")


# Uso de la clase MatrizOperaciones
matriz_operaciones = MatrizOperaciones(5, 10)
matriz_operaciones.mostrar_matriz()
matriz_operaciones.mostrar_resultados()
