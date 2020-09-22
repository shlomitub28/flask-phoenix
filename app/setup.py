from users import UsersModel
from schema import Schema
import os
import phoenixdb

# __file__ refers to the file settings.py
APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')

model=Schema()
model.create_users_table()
usersmodel=UsersModel()
data = {'username':'user1','firstname':'user','lastname':'one'\
    ,'telephone':'0544533856','message':'hi wassap','email':'yk@hotmail.com'}
results = usersmodel.upsert(data)
data = {'username':'user2','firstname':'user','lastname':'two',\
    'telephone':'0542733863','message':'hi wassap2','email':'yk2@hotmail.com'}
results = usersmodel.upsert(data)
data = {'username':'user3','firstname':'user','lastname':'three',\
    'telephone':'0524340980','message':'hi wassap3','email':'yk3@hotmail.com'}
results = usersmodel.upsert(data)
i=1
for file in os.listdir(APP_STATIC+'/images'):
    
    f=open(APP_STATIC+'/images/'+file,'rb')
    img=f.read()
    photo_data = {'username':f"user{i}",\
        'photo':img,\
        'photo_name':f"{file}"}
    usersmodel.upsert_photo(photo_data)
    i+=1
