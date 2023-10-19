class ProductManager:
    def __init__(self):
        self.product_list = []

    def add_product(self, product):
        self.product_list.append(product)

    def delete_product(self, product_id):
        for product in self.product_list:
            if product.product_id == product_id:
                self.product_list.remove(product)
                break

    def get_total_cost(self):
        total_cost = sum(product.price for product in self.product_list)
        return total_cost

    def get_sorted_products(self):
        sorted_products = sorted(self.product_list, key=lambda x: x.name)
        return sorted_products
