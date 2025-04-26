# Clase Producto
class Product:
    def __init__(self, id: int, name: str, description: str, category: str, stock: int, price: float):
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.stock = stock
        self.price = price

    def __str__(self):
        return f""""
                ID: {self.id}
                Nombre: {self.name}
                Descripción: {self.description}
                Categoría: {self.category}
                Stock: {self.stock}
                Precio: ${self.price}
             """
    
    def _validate_not_value(self, value: str, field_name: str) -> str:
        if not value:
            raise ValueError(f'El campo {field_name} no puede estar vacío.')
        return value

    def _validate_positive(self, value: int, field_name: str, allow_zero: bool = False) -> int:
        if allow_zero:
            if value<0:
                raise ValueError(f'El campo {field_name} no puede ser menor a cero.')
        if value<=0:
            raise ValueError(f'El campo {field_name} no puede ser menor o igual a cero.')
        return value

    # Nombre
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        self._name = self._validate_not_value(value, 'nombre')

    # Categoría
    @property
    def category(self) -> str:
        return self._category
    
    @category.setter
    def category(self, value: str):
        self._category = self._validate_not_value(value, 'categoría')

    # Stock
    @property
    def stock(self) -> int:
        return self._stock
    
    @stock.setter
    def stock(self, value: int):
        self._stock = self._validate_positive(value, 'stock', True)

    # Precio
    @property
    def price(self) -> float:
        return self._price
    
    @price.setter
    def price(self, value: float):
        self._price = self._validate_positive(value, 'precio')
