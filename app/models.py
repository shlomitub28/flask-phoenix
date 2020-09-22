import jaydebeapi
import pdb
import json
class Schema:
    def __init__(self):
        self.conn = jaydebeapi.connect("org.apache.phoenix.jdbc.PhoenixDriver",
                               "jdbc:phoenix:nightly7x-unsecure-2.nightly7x-unsecure.root.hwx.site:2181;autocommit=true",
                               ["SA", ""],
                               "../drivers/phoenix-5.0.0-HBase-2.0-client.jar",)

        self.curs = self.conn.cursor()

#    def __del__(self):
#        # body of destructor
#        self.conn.commit()
#        self.conn.close()

    def create_users_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS users (

        username VARCHAR NOT NULL,
        firstname VARCHAR,
        lastname  VARCHAR,
        telephone VARCHAR,
        message VARCHAR,
        email VARCHAR,
        photo VARBINARY,
        photo_name VARCHAR,
        photo_type VARCHAR
        CONSTRAINT my_pk PRIMARY KEY (username))
        """

        self.curs.execute(query)

    def create_user_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "User" (
        _id INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Email TEXT,
        CreatedOn Date default CURRENT_DATE
        );
        """
        self.conn.execute(query)
def drop_users_table(self):

    query = """
    CREATE TABLE USERS
    """

    self.curs.execute(query)

class UsersModel:
    TABLENAME = "users"

    def __init__(self):
        db = Schema()
        self.conn=db.conn
        self.curs=db.curs

#    def __del__(self):
#        self.conn.close()

    def upsert(self, params):
        query = f"upsert into {self.TABLENAME} "\
        f"(username ,message,telephone,firstname,lastname,email,photo,photo_name,photo_chars) "\
        f"values (\'{params.get('username')}\',\'{params.get('message')}\',\'{params.get('telephone')}\', "\
        f"\'{params.get('firstname')}\','{params.get('lastname')}\',\'{params.get('email')}\', "\
        f"\'{params.get('photo')}\','{params.get('photo_name')}\','{params.get('photo')}\')"
        print (query)
        sql = "upsert into " + self.TABLENAME + "(username ,message,telephone,firstname,lastname,email,photo,photo_name,photo_chars) values (?,?,?,?,?,?,?,?,?)"
        data = (params.get('username'),params.get('message'),params.get('telephone')
                ,params.get('firstname'),params.get('lastname'),params.get('email')
                ,params.get('photo'), params.get('photo_name'), params.get('photo'))
        results = self.curs.execute(sql,data)
#        return self.get_by_id(result.lastrowid)
        return results

    def delete(self, username):
        query = f"DELETE from {self.TABLENAME} " \
                f"WHERE username = {username}"
        print (query)
        self.curs.execute(query)
    def list_items(self, where_clause="",format="json"):
        query = f"SELECT username ,email,message,telephone,firstname,lastname,photo_name " \
                f"from {self.TABLENAME} WHERE  " + where_clause
        print (query)
        self.curs.execute(query)
        if format=="json":
            r = [dict((self.curs.description[i][0].lower(), value) \
                   for i, value in enumerate(row)) for row in self.curs.fetchall()]
            self.conn.close()
            data={'data': r }
            #return (json.dumps(r[0]) if r else None) if None else json.dumps(r)
            return json.dumps(data)

        result_set=self.curs.fetchall()
        result = [{column: row[i]
            for i, column in enumerate(result_set[0].keys())}
                for row in result_set]
        return result
    def get_image(self, username):
        query = f"SELECT photo,photo_name " \
                f"from {self.TABLENAME} WHERE  username='"+username+"'"
        print (query)
        self.curs.execute(query)
        row = self.curs.fetchone()
        print(row)
        #for i , value in enumerate(row):
        #    print(value)
        return row
