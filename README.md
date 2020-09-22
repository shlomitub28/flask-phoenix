# Flask web application with Apache Phoenix

Creating a simple CRUD web Application that store images with Flask & Apache Phoenix

In this example i'm using Cloudera COD in aws. for dev purposes, you can use [phoenix query server](https://github.com/apache/phoenix-queryserver/tree/master/python-phoenixdb#setting-up-a-development-environment)

before using this repo , install the [phoenix driver](https://github.com/apache/phoenix-queryserver/tree/master/python-phoenixdb)

Instructions
```
$ pip install -r requirements.txt
```
Change to the app directory and run setup::
```
$  cd app
$  python seteup.py
```
This will create a table with some data and images in COD
Now you can run the flask web server::
```
$  FLASK_APP=app.py python -m flask run --port=8888 --host=127.0.0.1  --reload --with-threads --debugger
```
Now log in to http://localhost/users to view and use the web application
