from infrastructure.config.conn import ConnectDB
from domain.repositories.product_repository import ProductRepository
from domain.entities.product import Product


class ProductRepositoryMySQL(ProductRepository):
    def __init__(self, connection: ConnectDB):
        self.connection = connection

    def add_product(self, product: Product):
        conn = self.connection.get_conn()
        with conn.cursor() as cursor:
            sql = 'INSERT INTO ' \
            'products (id, name, description, category, stock, price) ' \
            'VALUES (%s, %s, %s, %s, %s, %s)'
            cursor.execute(sql, 
                           (product.id,
                            product.name,
                            product.description,
                            product.category,
                            product.stock,
                            product.price)
                        )
        conn.commit()
        conn.close()

    def get_all_products(self):
        pass

    
    def get_product_by_id(self, product_id: int):
        pass
        
    
    def update_product(self, product_id: int, product_new: Product):
        pass
        
    
    def delete_product(self, product_id: int):
        pass