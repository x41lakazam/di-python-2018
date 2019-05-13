import json

db = {

    'users':[
        {'name':'Eyal', 'email':'eyal@gmail.com', 'posts':['I love python', 'Hello world']},
        {'name':'sean', 'email':'sean@gmail.com', 'posts':['sean love python', 'Hello world']},
        {'name':'yossi', 'email':'yossi@gmail.com', 'posts':['yossi love python', 'Hello world']},
    ]
}

filename = "app_db.json"
file_obj = open(filename, 'w')
json.dump(db, file_obj)