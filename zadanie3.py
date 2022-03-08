import json
import yaml
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
    des_data = json.load(read_file)
    print (des_data)
print()
print('Сериализация и десериализация с помощью yaml')
serial = yaml.dump(data, indent=4)
print(serial)
desserial = yaml.load(serial, Loader=yaml.FullLoader)
print(desserial)
