import random

class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

almacen_productos = []

def agregar_producto(nombre, cantidad, precio):
    producto = Producto(nombre, cantidad, precio)
    almacen_productos.append(producto)

def retirar_producto(nombre, cantidad):
    for producto in almacen_productos:
        if producto.nombre == nombre:
            if producto.cantidad >= cantidad:
                producto.cantidad -= cantidad
                return f"Se retiraron {cantidad} unidades de {nombre}."
            else:
                return f"No hay suficiente cantidad de {nombre} en el almacén."
    return f"{nombre} no se encontró en el almacén."

def mostrar_inventario():
    inventario = []
    for producto in almacen_productos:
        inventario.append(f"{producto.nombre} - Cantidad: {producto.cantidad}, Precio: ${producto.precio:.2f}")
    return "\n".join(inventario)
