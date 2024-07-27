import json

file = open('csv_file.txt','r')
file_contents = json.load(file)

file.close()


