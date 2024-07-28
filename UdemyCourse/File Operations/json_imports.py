import json

with open('friends_json.txt', 'r') as file: #using context manager
    file_contents = json.load(file) # reads the file and converts into dict

print(file_contents['friends'][0])

cars = [
    {'make':'Ford', 'mode1':'Fiesta'},
    {'make':'Ford', 'model': 'Focus'}
]

# Go and investigate how to use json.dump
with open('cars_json.txt','w') as file:
    json.dump(cars,file)
    

my_json_string = '[{"name": "Innova", "released":2004}, {"name": "Ford", "released":2008}]'
incorrect_car = json.loads(my_json_string)
print(incorrect_car[1]['name'])