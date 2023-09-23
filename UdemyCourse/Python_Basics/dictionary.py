
#Duplicate keys is not allowed in Dict
'''friends_ages = {"Rolf":24, "Adam":30, "Anne": 27}

friends_ages["Bob"] = 35
friends_ages["Rolf"] = 25

print(friends_ages)
'''

friends = (
    {"name": "Prashanth", "age":26},
    {"name": "Tom", "age":24},
    {"name": "Ram", "age":30}
)

print(friends[0]["name"])
print(friends[1]["name"])
print(friends[2]["name"])
