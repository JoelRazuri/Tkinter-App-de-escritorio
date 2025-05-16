from infrastructure.config.config import DB_CONFIG
from infrastructure.config.conn import ConnectDB
from infrastructure.db.product_repository_db import ProductRepositoryMySQL
from domain.entities.product import Product


# Pruebas
product = Product(2, 'Lapicera', 'Lapicera bic color negro', 'Colegio', 50, 200)

conn = ConnectDB(**DB_CONFIG)

repo = ProductRepositoryMySQL(conn)

repo.add_product(product)