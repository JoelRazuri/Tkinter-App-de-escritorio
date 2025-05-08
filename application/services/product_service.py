from domain.repositories.product_repository import ProductRepository
from domain.entities.product import Product
from typing import List


class ProductService():
    def __init__(self, repository: ProductRepository):
        self.repository = repository
    
    def create_product(self, product: Product) -> Product:
        return self.repository.add_product(product)
    
    def list_products(self) -> List[Product] | None:
        return self.repository.get_all_products()

    def update_product(self, product_id: int, product_update: Product) -> Product:
        product = self.repository.get_product_by_id(product_id)
        if not product:
            raise ValueError(f'El producto con ID: {product_id}, no fue encontrado.')
        return self.repository.update_product(product_id, product_update)
    
    def remove_product(self, product_id: int) -> None:
        product = self.repository.get_product_by_id(product_id)
        if not product:
            raise ValueError(f'El producto con ID: {product_id}, no fue encontrado.')
        self.repository.delete_product(product_id)
        return None