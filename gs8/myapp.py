import requests
import json

url = 'http://127.0.0.1:8000/stu/'

def get_data(id = None):
     data = {}
     if id is not None:
         data = {'id':id}
     json_data = json.dumps(data)
     r = requests.get(url = url, data=json_data)
     data = r.json()
     print(data)

#get_data() 

def post_data():
    data = {
        'name': 'mohit',
        'roll': '201',
        'city': 'bilaspur'
    }
    json_data =  json.dumps(data)
    r = requests.post(url = url, data=json_data)
    data = r.json()
    print(data)   

post_data()   


def update_data():
    data = {
        'id': 3,
        'name': 'kiran',
        'city': 'Churu',
        'roll': 6
    }
    json_data =  json.dumps(data)
    r = requests.put(url = url, data=json_data)
    data = r.json()
    print(data)   

#update_data()   



def delete_data():
    data = {'id': 8}
    json_data =  json.dumps(data)
    r = requests.delete(url = url, data=json_data)
    data = r.json()
    print(data)   

#delete_data()   


