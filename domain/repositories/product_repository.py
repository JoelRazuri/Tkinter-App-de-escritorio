from abc import ABC, abstractmethod
from typing import List
from domain.entities.product import Product


class ProductRepository(ABC):
    @abstractmethod
    def add_product(self, product: Product) -> Product:
        """  Crea un producto y devuelve su entidad. """
        ...
    
    @abstractmethod
    def get_all_products(self) -> List[Product]:
        """  Devuelve todos los productos existentes. """
        ...

    @abstractmethod
    def get_product_by_id(self, product_id: int) -> Product:
        """  Busca y devuelve un producto según su ID. """
        ...

    @abstractmethod
    def update_product(self, product_id: int, product_new: Product) -> Product:
        """  Actualiza un producto según su ID y devuelve la versión actualizada. """
        ...

    @abstractmethod
    def delete_product(self, product_id: int) -> None:
        """  Elimina un producto según su ID. """
        ...