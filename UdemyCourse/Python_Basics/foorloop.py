#friends = ["Prashanth","Ram","Ron"]

#for friend in friends:
 #   print(friend)

#elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#for index in range(10):
 #   print(index)

students = [
    {"name": "Prashanth", "grade": 90},
    {"name": "John", "grade": 70},
    {"name": "Ram", "grade": 60},
]

for student in students:
    name= student["name"]
    grade = student["grade"]

    print(f"{name} has a grade of {grade}.")