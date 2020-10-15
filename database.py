from flask_db2 import DB2


class database:

    def __init__(self, app):
        self.db = DB2(app)

    def get_db(self):
        return self.db

    def init_db(self):
        cur = self.db.connection.cursor()
        cur.execute('SELECT * FROM tblUser')
