import phoenixdb
from schema import Schema
import json
class UsersModel:
    TABLENAME = "users"

    def __init__(self):
        db = Schema()
        self.conn=db.conn
        self.curs=db.curs

    def upsert(self, params):

        sql = "upsert into " + self.TABLENAME + \
            " (username ,message,telephone,firstname,lastname,email) \
             values (?,?,?,?,?,?)"
        data = (params.get('username'),params.get('message'),\
            params.get('telephone'),params.get('firstname'),\
            params.get('lastname'),params.get('email'))
        results = self.curs.execute(sql,data)
        return results

    def upsert_photo(self, params):

        if params.get('photo') is None:
            photo = bytes('','utf-8')
        else:
            photo = params.get('photo')


        sql = "upsert into " + self.TABLENAME + \
            " (username, photo,photo_name) values (?,?,?)"

        data = (params.get('username'),photo, params.get('photo_name'))
        results = self.curs.execute(sql,data)
        return results

    def delete(self, username):
        query = f"DELETE from {self.TABLENAME} " \
                f"WHERE username = {username}"

        self.curs.execute(query)

    def list_items(self, where_clause="",format="json"):
        query = f"SELECT username ,email,message,telephone,firstname,\
            lastname,photo_name " \
            f"from {self.TABLENAME} WHERE  " + where_clause

        self.curs.execute(query)
        if format=="json":
            r = [dict((self.curs.description[i][0].lower(), value) \
                   for i, value in enumerate(row)) for row in \
                   self.curs.fetchall()]
            self.conn.close()
            data={'data': r }
            return json.dumps(data)

        result_set=self.curs.fetchall()
        result = [{column: row[i]
            for i, column in enumerate(result_set[0].keys())}
                for row in result_set]
        return result
    def get_image(self, username):
        query = f"SELECT photo,photo_name " \
                f"from {self.TABLENAME} WHERE  username='"+username+"'"

        self.curs.execute(query)
        row = self.curs.fetchone()
        return row
