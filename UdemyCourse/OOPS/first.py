my_student ={

    'name':'Prashanth',
    'grades': [70,88,90,99]
}

def student_avg(student):
   return sum(student['grades']) / len(student['grades'])

        
print(student_avg(my_student))
