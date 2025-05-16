import pymysql.cursors


class ConnectDB():
    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.cursor = pymysql.cursors.DictCursor

    def get_conn(self):
        try:
            connect = pymysql.connect(
                host=self.host, 
                user=self.user, 
                password=self.password, 
                db=self.db, 
                cursorclass=self.cursor)
            # print('Conexión a la base de datos exitosa :D !!!')
        except pymysql.MySQLError as err:
            raise pymysql.MySQLError(f'Error al conectar a la base de datos: {err}')
        return connect