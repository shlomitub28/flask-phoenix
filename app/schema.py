import phoenixdb
from config import *
class Schema:
    def __init__(self):
        opts = {}
        opts['authentication'] = 'BASIC'
        opts['avatica_user'] = '<cod workload username>'
        opts['avatica_password'] = '<cod workload pw>'
        database_url = "<cod thin jdbc url>"
        self.TABLENAME = "users"
        self.conn = phoenixdb.connect(database_url, autocommit=True,**opts)
        self.curs = self.conn.cursor()

    def create_users_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS """+self.TABLENAME+""" (
        username VARCHAR NOT NULL,
        firstname VARCHAR,
        lastname  VARCHAR,
        telephone VARCHAR,
        message VARCHAR,
        email VARCHAR,
        photo VARBINARY,
        photo_name VARCHAR,
        photo_type VARCHAR,
        photo_chars VARCHAR
        CONSTRAINT my_pk PRIMARY KEY (username))
        """
        self.curs.execute(query)

    def drop_users_table(self):
        query = "DROP TABLE "+self.TABLENAME
        self.curs.execute(query)
