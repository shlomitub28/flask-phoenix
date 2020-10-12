# Flask web application with Apache Phoenix

Creating a simple CRUD web Application that store images with Flask & Apache Phoenix

In this example i'm using Cloudera COD in aws. for dev purposes, you can use [phoenix query server](https://github.com/apache/phoenix-queryserver/tree/master/python-phoenixdb#setting-up-a-development-environment)

Instructions
```
$ pip install -r requirements.txt
```
Change to the app directory and edit config.py to add your parameters of workload user, password, and the Phoenix Query Server Endpoint
```
$  cd app
$  vi config.py

WORKLOAD_USER = 'bobjones'
WORKLOAD_PASSWORD = 'verysecretpassword'
OPDB_ENDPOINT = 'https://cod-datahubname-gateway1.kerb1.kerb2.cloudera.site/cod-datahubname/cdp-proxy-api/avatica'

```
 Now run setup
```
$  python setup.py
```
This will create a table with some data and images in COD
Now you can run the flask web server::
```
$  python -m flask run --port=12345 --host=$(hostname -i) --reload --with-threads
```
Now log in to http://localhost/users to view and use the web application
