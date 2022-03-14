from pydantic import BaseModel
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


class Results(BaseModel):
    age: int
    name: str
    children: list[dict]
    married: bool
    city: None


print(Results(**data))  
