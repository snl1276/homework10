with open('text.txt', 'w') as file:
    file.write('hello world')
with open('text.txt', 'r') as file:
    print(file.read())
