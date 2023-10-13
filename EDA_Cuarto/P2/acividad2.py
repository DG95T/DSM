import random
import tkinter as tk

def generar_y_mostrar_numeros():
    cantidad_numeros = int(cantidad_entry.get())
    minimo = int(minimo_entry.get())
    maximo = int(maximo_entry.get())
    
    numeros_aleatorios = [random.randint(minimo, maximo) for _ in range(cantidad_numeros)]
    
    resultado_label.config(text="Números aleatorios: " + str(numeros_aleatorios))

# Crear una ventana
ventana = tk.Tk()
ventana.title("Generador de Números Aleatorios")

# Etiqueta y entrada para la cantidad de números
cantidad_label = tk.Label(ventana, text="Cantidad de números:")
cantidad_label.pack()
cantidad_entry = tk.Entry(ventana)
cantidad_entry.pack()

# Etiqueta y entrada para el valor mínimo
minimo_label = tk.Label(ventana, text="Valor mínimo:")
minimo_label.pack()
minimo_entry = tk.Entry(ventana)
minimo_entry.pack()

# Etiqueta y entrada para el valor máximo
maximo_label = tk.Label(ventana, text="Valor máximo:")
maximo_label.pack()
maximo_entry = tk.Entry(ventana)
maximo_entry.pack()

# Botón para generar y mostrar los números
generar_button = tk.Button(ventana, text="Generar y Mostrar", command=generar_y_mostrar_numeros)
generar_button.pack()

# Etiqueta para mostrar los números generados
resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

ventana.mainloop()