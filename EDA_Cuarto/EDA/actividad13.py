import tkinter as tk
from tkinter import ttk

class CalificacionesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calificaciones")

        # Matriz de calificaciones
        self.calificaciones = [
            [5.5, 8.6, 10],
            [8.0, 5.5, 10],
            [9.0, 4.1, 7.8],
            [10, 2.2, 8.1],
            [7.0, 9.2, 7.1],
            [9.0, 4.0, 6.0],
            [6.5, 5.0, 5.0],
            [4.0, 7.0, 4.0],
            [8.0, 8.0, 9.0],
            [10, 9.0, 9.2],
            [5.0, 10, 8.4],
            [9.0, 4.6, 7.5]
        ]

        self.create_widgets()

    def create_widgets(self):
        # Botón para calcular resultados
        self.btn_calculate = ttk.Button(self.root, text="Calcular Resultados", command=self.calculate_results)
        self.btn_calculate.pack()

        # Área de texto para mostrar resultados
        self.result_text = tk.Text(self.root, height=20, width=40)
        self.result_text.pack()

    def calculate_results(self):
        # Cálculo de resultados
        promedios_alumnos = [self.calcular_promedio(alumno) for alumno in self.calificaciones]
        promedio_mas_alto = self.calcular_promedio_mas_alto(self.calificaciones)
        promedio_mas_bajo = self.calcular_promedio_mas_bajo(self.calificaciones)
        parciales_reprobados = self.contar_parciales_reprobados(self.calificaciones)
        distribucion_calificaciones = self.generar_distribucion(self.calificaciones)

        # Formatear resultados en un texto
        result = "Matriz de Calificaciones:\n\n"
        for fila in self.calificaciones:
            result += "  ".join(map(str, fila)) + "\n"

        result += "\nResultados:\n\n"
        result += f"Promedio de cada alumno:\n{promedios_alumnos}\n\n"
        result += f"Promedio más alto: {promedio_mas_alto}\n"
        result += f"Promedio más bajo: {promedio_mas_bajo}\n"
        result += f"Parciales reprobados: {parciales_reprobados}\n"
        result += f"Distribución de calificaciones finales: {distribucion_calificaciones}"

        # Mostrar resultados en el área de texto
        self.display_result(result)

    def calcular_promedio(self, calificaciones):
        # Calcular el promedio de un alumno
        return sum(calificaciones) / len(calificaciones)

    def calcular_promedio_mas_alto(self, calificaciones):
        # Encontrar el promedio más alto
        return max([self.calcular_promedio(alumno) for alumno in calificaciones])

    def calcular_promedio_mas_bajo(self, calificaciones):
        # Encontrar el promedio más bajo
        return min([self.calcular_promedio(alumno) for alumno in calificaciones])

    def contar_parciales_reprobados(self, calificaciones):
        # Contar parciales reprobados
        reprobados = 0
        for alumno in calificaciones:
            for calificacion in alumno:
                if calificacion < 6:
                    reprobados += 1
        return reprobados

    def generar_distribucion(self, calificaciones):
        # Generar la distribución de calificaciones finales
        distribucion = [0, 0, 0, 0, 0]  # Inicializamos la distribución con 5 elementos

        for alumno in calificaciones:
            promedio = self.calcular_promedio(alumno)
            if promedio >= 9:
                distribucion[4] += 1
            elif promedio >= 7:
                distribucion[3] += 1
            elif promedio >= 5:
                distribucion[2] += 1
            elif promedio >= 3:
                distribucion[1] += 1
            else:
                distribucion[0] += 1

        return distribucion

    def display_result(self, result):
        # Mostrar resultados en el área de texto
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalificacionesApp(root)
    root.mainloop()
