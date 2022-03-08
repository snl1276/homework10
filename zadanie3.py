import json
data = { 
    'age': 45, 
    'name': 'Peter', 
    'children': [
        {
            'age': 3,   
            'name': 'Alice'  
        }
    ],
    'married': True, 
    'city': None
}
with open('file.txt', 'w') as fd:
    json.dump(data, fd, indent=4)
with open('file.txt', 'r') as read_file:
    data = json.load(read_file)
    print (data)