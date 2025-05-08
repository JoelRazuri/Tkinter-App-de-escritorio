import pymysql.cursors


class ConnectDB():
    def __init__(self,host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.cursor = pymysql.cursors.DictCursor

    def get_conn(self):
        try:
            connect = pymysql.connect(self.host, self.user, self.password, self.db, cursorclass=self.cursor)
        except pymysql.MySQLError as err:
            raise pymysql.MySQLError("Error al conectar a la base de datos: " + str(err))
        return connect