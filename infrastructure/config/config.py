import os

DB_CONFIG = {
    'host': os.getenv('HOST'),
    'user': os.getenv('USER'),
    'password': os.getenv('PASSWORD'),
    'db': os.getenv('DB_NAME'),
}