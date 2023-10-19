import tkinter as tk
from product_manager import ProductManager
from product import Product

class ProductApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Productos")

        self.product_manager = ProductManager()

        self.add_product_button = tk.Button(root, text="Agregar Producto", command=self.add_product)
        self.add_product_button.pack()

        self.delete_product_button = tk.Button(root, text="Eliminar Producto", command=self.delete_product)
        self.delete_product_button.pack()

        self.show_products_button = tk.Button(root, text="Mostrar Productos", command=self.show_products)
        self.show_products_button.pack()

        self.total_cost_label = tk.Label(root, text="Costo Total de Compra: $0.00")
        self.total_cost_label.pack()

    def add_product(self):
        # Ventana emergente para agregar un producto
        add_product_window = tk.Toplevel(self.root)

        product_id_label = tk.Label(add_product_window, text="ID del Producto:")
        product_id_label.pack()
        product_id_entry = tk.Entry(add_product_window)
        product_id_entry.pack()

        product_name_label = tk.Label(add_product_window, text="Nombre del Producto:")
        product_name_label.pack()
        product_name_entry = tk.Entry(add_product_window)
        product_name_entry.pack()

        product_price_label = tk.Label(add_product_window, text="Precio del Producto:")
        product_price_label.pack()
        product_price_entry = tk.Entry(add_product_window)
        product_price_entry.pack()

        def add_product_to_list():
            product_id = product_id_entry.get()
            product_name = product_name_entry.get()
            product_price = float(product_price_entry.get())
            new_product = Product(product_id, product_name, product_price)
            self.product_manager.add_product(new_product)
            add_product_window.destroy()

        add_product_button = tk.Button(add_product_window, text="Agregar", command=add_product_to_list)
        add_product_button.pack()

    def delete_product(self):
        # Ventana emergente para eliminar un producto por clave
        delete_product_window = tk.Toplevel(self.root)

        product_id_label = tk.Label(delete_product_window, text="ID del Producto a Eliminar:")
        product_id_label.pack()
        product_id_entry = tk.Entry(delete_product_window)
        product_id_entry.pack()

        def delete_product_from_list():
            product_id = product_id_entry.get()
            self.product_manager.delete_product(product_id)
            delete_product_window.destroy()

        delete_button = tk.Button(delete_product_window, text="Eliminar", command=delete_product_from_list)
        delete_button.pack()

    def show_products(self):
        products = self.product_manager.get_sorted_products()
        product_list_text = "\n".join([f"{product.name}: ${product.price:.2f}" for product in products])

        # Crear una ventana emergente para mostrar la lista de productos
        show_products_window = tk.Toplevel(self.root)
        products_label = tk.Label(show_products_window, text=product_list_text)
        products_label.pack()

        total_cost = self.product_manager.get_total_cost()
        self.total_cost_label.config(text=f"Costo Total de Compra: ${total_cost:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ProductApp(root)
    root.mainloop()
