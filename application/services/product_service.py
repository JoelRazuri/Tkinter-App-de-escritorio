from domain.repositories.product_repository import ProductRepository
from domain.entities.product import Product
from typing import List



class ProductService():
    def __init__(self, repository: ProductRepository):
        self.repository = repository
    
    def add_product(self, product: Product) -> Product:
        try:
            new_product = self.repository.add_product(product)
        except ValueError as err:
            raise err
        return new_product
    
    def get_all_products(self) -> List[Product]:
        try:
            all_products = self.repository.get_all_products()
        except Exception as err:
            raise err
        return all_products

    def get_product_by_id(self, product_id) -> Product:
        try:
            product = self.repository.get_product_by_id(product_id)
        except Exception as err:
            raise err
        return product
    
    def update_product(self, product_id, product_update) -> Product:
        try:
            product = self.repository.get_product_by_id(product_id, product_update)
        except Exception as err:
            raise err
        return product
    
    def delete_product(self, product_id) -> None:
        try:
            self.repository.get_product_by_id(product_id)
        except Exception as err:
            raise err
        return None