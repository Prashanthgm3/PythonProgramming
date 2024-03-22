
def average_grade(student):
    return sum(student['grades']) / len(student['grades'])


class Student: #self is an blank object and def __init__ is called as dunder function
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    def getname(self):
        print(self.name)

    def average(self):
        return sum(self.grades) / len(self.grades)


student_one = Student('Prashanth', [70,80, 90, 99])
student_two = Student('Rolf', [50,60, 90, 99])


print(f" The name of student is {student_one.name} and average score is {student_one.average()} ")