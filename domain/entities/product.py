# Clase Producto
class Product():
    def __init__(self, id:int, name:str, description:str, category:str, stock:int, price:float):
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.stock = stock
        self.price = price

    def __str__(self):
        return f""""
                Producto: {self.name}
                Descripción: {self.description}
                Categoría: {self.category}
                Stock: {self.stock}
                Precio: ${self.price}
                """
