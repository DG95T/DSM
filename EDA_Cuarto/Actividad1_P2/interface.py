import tkinter as tk
from tkinter import messagebox
from producto import agregar_producto
import random
from producto import mostrar_inventario

def generar_productos_aleatorios():
    for i in range(1, 11):
        nombre = f"producto{i}"
        cantidad = random.randint(1, 100)
        precio = round(random.uniform(1.0, 100.0), 2)
        agregar_producto(nombre, cantidad, precio)

def agregar_producto_gui():
    nombre = nombre_entry.get()
    cantidad = cantidad_entry.get()
    precio = precio_entry.get()
    if nombre and cantidad and precio:
        agregar_producto(nombre, int(cantidad), float(precio))
        update_inventario()
        messagebox.showinfo("Éxito", f"{cantidad} unidades de {nombre} han sido agregadas al almacén.")
        nombre_entry.delete(0, tk.END)
        cantidad_entry.delete(0, tk.END)
        precio_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")

# Crear una ventana principal
root = tk.Tk()
root.title("Gestión de Inventario")

# Agregar productos aleatorios al inicio
generar_productos_aleatorios()

# Widgets y etiquetas para agregar productos
nombre_label = tk.Label(root, text="Nombre del producto:")
nombre_label.pack()
nombre_entry = tk.Entry(root)
nombre_entry.pack()

cantidad_label = tk.Label(root, text="Cantidad:")
cantidad_label.pack()
cantidad_entry = tk.Entry(root)
cantidad_entry.pack()

precio_label = tk.Label(root, text="Precio por unidad:")
precio_label.pack()
precio_entry = tk.Entry(root)
precio_entry.pack()

agregar_button = tk.Button(root, text="Agregar Producto", command=agregar_producto_gui)
agregar_button.pack()

# Continuación de la interfaz gráfica
# (Agregar aquí los elementos para retirar productos y mostrar el inventario)

# Función para actualizar el inventario en la interfaz
def update_inventario():
    inventario_text.delete(1.0, tk.END)
    inventario_text.insert(tk.END, mostrar_inventario())

# Continuación de la interfaz gráfica
# (Agregar aquí los elementos para retirar productos y mostrar el inventario)

# Widget para mostrar el inventario
inventario_label = tk.Label(root, text="Inventario:")
inventario_label.pack()
inventario_text = tk.Text(root, width=40, height=10)
inventario_text.pack()

# Actualizar el inventario inicial
update_inventario()

# Bucle principal
root.mainloop()
