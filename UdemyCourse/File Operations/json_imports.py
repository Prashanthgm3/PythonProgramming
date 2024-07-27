import json

file = open('friends_json.txt', 'r')
file_contents = json.load(file) # reads the file and converts into dict

file.close()

print(file_contents['friends'][0])

cars = [
    {'make':'Ford', 'mode1':'Fiesta'},
    {'make':'Ford', 'model': 'Focus'}
]

# Go and investigate how to use json.dump
file = open('cars_json.txt','w')
json.dump(cars,file)
file.close()

my_json_string = '[{"name": "Innova", "released":2004}, {"name": "Ford", "released":2008}]'
incorrect_car = json.loads(my_json_string)
print(incorrect_car[1]['name'])