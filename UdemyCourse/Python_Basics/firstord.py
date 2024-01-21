
operations = {

    "average": lambda seq: sum(seq) / len(seq),
    "total": lambda seq: sum(seq),
     "top": lambda seq: max(seq)

}

students = [

        {"name": "Rolf", "grades": (67, 90, 95, 100)},
        {"name": "Prashanth", "grades": (67, 89, 78, 100)},
        {"name": "Jen", "grades": (67, 87, 76, 68)},
        {"name": "Tom", "grades": (66, 84, 78, 66)},
]

for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"Student :{name}")
    operation = input("Enter 'average', 'total', or 'top': ")

    operation_function = operations[operation]
    print(operation_function(grades))