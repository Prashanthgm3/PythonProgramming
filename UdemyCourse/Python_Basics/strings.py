"""
Strings
This talks about strings.
"""

my_string = "Hello, world"
print(my_string)

my_string2 = 'Hello, Raspberrypi'
print(my_string2)

another_with_quotes = 'He said "Your amazing" today.'
print(another_with_quotes)

multiline = """Hello world.
My name is Prashanth Welcome to Python
"""

print(multiline)



name = "Prashanth"
greeting = "Hello, " + name
print(greeting)

age = 27
age_as_str = str(age)
print("You are " + age_as_str)

print(f"You are {name}")


final_greeting = "What are you doing, {name}?"
prashanth_greeting = final_greeting.format(name=name)
print(prashanth_greeting)



