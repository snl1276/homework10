import pickle


class Person:
    name = "Tom"
    def display_info(name):
        print(f"Name: {name}")


object = Person()
serial = pickle.dumps(object)
print(serial)
deserial = pickle.loads(serial)
print(deserial.name)
Person.display_info('Dina')
