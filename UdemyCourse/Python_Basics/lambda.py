# def divide(x, y):
#     return x /y          normal function declaration

divide = lambda x, y: x / y

#print((lambda x, y: x /y)(15, 3)) bad wau of writing lambda function


# def average(sequence):
#     return sum(sequence) / len(sequence)

average = lambda sequence: sum(sequence)/ len(sequence)


students = [

        {"name": "Rolf", "grades": (67, 90, 95, 100)},
        {"name": "Prashanth", "grades": (67, 89, 78, 100)},
        {"name": "Jen", "grades": (67, 87, 76, 100)},
]

for student in students:
    print(average(student["grades"]))


