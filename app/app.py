from flask import Flask, request, send_file ,jsonify,render_template
import phoenixdb
import io
from users import UsersModel
from schema import Schema
import json

app = Flask(__name__)


@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] =  \
        "Content-Type, Access-Control-Allow-Headers, Authorization, \
        X-Requested-With"
    response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, \
    DELETE, OPTIONS"
    response.headers['Allow']=  "POST, GET, PUT, OPTIONS"
    return response


@app.route("/users")
def return_form():
    return render_template("users.html")

@app.route("/handle_data",methods=['POST'])
def handle_data():
    if request.method == 'POST':
        username = request.form['username']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        telephone = request.form['telephone']
        message = request.form['message']
        photo = request.files['photo']
        photo_bytes = photo.read()
        model=Schema()
        usersmodel=UsersModel()
        data = {'username':f"{username}",'firstname':f"{firstname}",\
            'lastname':f"{lastname}",'telephone':f"{telephone}",\
            'message':f"{message}"}
        photo_data = {'username':f"{username}",\
            'photo':photo_bytes,\
            'photo_name':f"{photo.filename}"}
        usersmodel.upsert(data)
        usersmodel.upsert_photo(photo_data)
        return render_template('users.html')
    else:
        return render_template('users.html')

@app.route("/get_users",methods=['GET'])
def get_users():
    if request.method == 'GET':
        usersmodel=UsersModel()
        users = usersmodel.list_items("1=1")
        return users

@app.route("/get_image",methods=['GET'])
def get_image():
    if request.method == 'GET':
        username = request.args.get('username')
        usersmodel=UsersModel()
        imagedb = usersmodel.get_image(username)
        return send_file(io.BytesIO(imagedb[0]),mimetype='image/png', \
            attachment_filename=imagedb[1])


if __name__ == "__main__":
    Schema()
    app.run(debug=True, port=8888)
