import requests
import json

url = 'http://127.0.0.1:8000/stu/'

def get_data(id = None):
     data = {}
     if id is not None:
         data = {'id':id}
     headers = {'content-type':'application/json'}    
     json_data = json.dumps(data)
     r = requests.get(url = url,headers=headers, data=json_data)
     data = r.json()
     print(data)

#get_data() 

def post_data():
    data = {
        'name': 'rohit',
        'roll': '5',
        'city': 'surat'
    }
    headers = {'content-type':'application/json'}
    json_data =  json.dumps(data)
    r = requests.post(url = url,headers=headers, data=json_data)
    data = r.json()
    print(data)   

#post_data()   


def update_data():
    data = {
        'id': 2,
        'name': 'kiran',
        'city': 'Churu'
        
    }
    headers = {'content-type':'application/json'}
    json_data =  json.dumps(data)
    r = requests.put(url = url, headers=headers, data=json_data)
    data = r.json()
    print(data)   

#update_data()   



def delete_data():
    data = {'id': 4}
    headers = {'content-type':'application/json'}
    json_data =  json.dumps(data)
    r = requests.delete(url = url, headers=headers ,data=json_data)
    data = r.json()
    print(data)   

delete_data()   


