import tkinter as tk
from tkinter import ttk
import random
from tkinter import simpledialog

class VentasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventas por Mes y Día")

        # Matriz de ventas por mes y día
        self.ventas_por_mes = [
            [5, 16, 10, 12, 24],  # Enero
            [40, 55, 10, 11, 18],  # Febrero
            [15, 41, 78, 14, 51],  # Marzo
            [35, 22, 81, 15, 12],  # Abril
            [50, 12, 71, 10, 20],  # Mayo
            [70, 40, 60, 28, 22],  # Junio
            [50, 50, 50, 36, 25],  # Julio
            [40, 70, 40, 11, 20],  # Agosto
            [20, 20, 30, 12, 18],  # Septiembre
            [10, 40, 32, 13, 16],  # Octubre
            [50, 3, 24, 15, 82],  # Noviembre
            [40, 46, 15, 46, 22]  # Diciembre
        ]

        self.create_widgets()

    def create_widgets(self):
        # Botones para realizar acciones
        self.btn_show_min_max = ttk.Button(self.root, text="Mostrar Min/Max Venta", command=self.show_min_max)
        self.btn_show_min_max.pack()

        self.btn_show_total = ttk.Button(self.root, text="Mostrar Venta Total", command=self.show_total)
        self.btn_show_total.pack()

        self.btn_show_daily_sales = ttk.Button(self.root, text="Mostrar Ventas Diarias", command=self.show_daily_sales)
        self.btn_show_daily_sales.pack()

        # Área de texto para mostrar resultados
        self.result_text = tk.Text(self.root, height=10, width=40)
        self.result_text.pack()

    def show_min_max(self):
        # Solicitar al usuario el mes y el día
        mes, dia = self.get_user_month_and_day()

        if mes is not None and dia is not None:
            # Encontrar el mínimo y máximo valor de ventas
            min_max_info = self.find_min_max(mes, dia)

            # Mostrar resultados en el área de texto
            self.display_result(f"Menor Venta:\nMes: {mes + 1}, Día: {dia + 1}, Venta: ${min_max_info['minimo']}.00\n\n"
                                f"Mayor Venta:\nMes: {mes + 1}, Día: {dia + 1}, Venta: ${min_max_info['maximo']}.00")

    def show_total(self):
        # Calcular la venta total
        total = self.calculate_total()

        # Mostrar resultado en el área de texto
        self.display_result(f"Venta Total:\nTotal: ${total}.00")

    def show_daily_sales(self):
        # Calcular la venta por día de la semana
        daily_sales = self.calculate_daily_sales()

        # Mostrar resultado en el área de texto
        self.display_result("Venta por Día de la Semana:\n" + "\n".join(daily_sales))

    def find_min_max(self, mes, dia):
        minimo = self.ventas_por_mes[mes][dia]
        maximo = self.ventas_por_mes[mes][dia]
        mes_minimo, mes_maximo = mes, mes
        dia_minimo, dia_maximo = dia, dia

        # Encontrar el mínimo y máximo valor de ventas en la matriz
        for i, ventas_mes in enumerate(self.ventas_por_mes):
            for j, venta in enumerate(ventas_mes):
                if venta < minimo:
                    minimo = venta
                    mes_minimo, dia_minimo = i, j
                if venta > maximo:
                    maximo = venta
                    mes_maximo, dia_maximo = i, j

        return {"minimo": minimo, "mesMinimo": mes_minimo, "diaMinimo": dia_minimo,
                "maximo": maximo, "mesMaximo": mes_maximo, "diaMaximo": dia_maximo}

    def calculate_total(self):
        # Calcular la venta total sumando todos los valores en la matriz
        total = sum(sum(ventas_mes) for ventas_mes in self.ventas_por_mes)
        return total

    def calculate_daily_sales(self):
        # Calcular la venta por día de la semana
        dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        venta_por_dia = [0] * 5

        for ventas_mes in self.ventas_por_mes:
            for dia, venta in enumerate(ventas_mes):
                venta_por_dia[dia] += venta

        return [f"{dias_semana[i]}: ${venta}.00" for i, venta in enumerate(venta_por_dia)]

    def display_result(self, result):
        # Mostrar resultados en el área de texto
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)

    def get_user_month_and_day(self):
        # Solicitar al usuario el mes y el día usando simpledialog
        mes = simpledialog.askinteger("Ingresar Mes", "Ingrese el número de mes (1-12):", minvalue=1, maxvalue=12)
        dia = simpledialog.askinteger("Ingresar Día", "Ingrese el número de día (1-5):", minvalue=1, maxvalue=5)
        return mes - 1, dia - 1 if mes is not None and dia is not None else (None, None)

if __name__ == "__main__":
    root = tk.Tk()
    app = VentasApp(root)
    root.mainloop()
