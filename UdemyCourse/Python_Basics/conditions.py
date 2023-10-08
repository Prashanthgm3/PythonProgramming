friends = ["A","B","C"]
family = ["P","Q"]
user_name = input("Enter your name:")

if user_name in friends:
    print("Hello ", friends)

if user_name in family:
    print("Hello ", family)

else:
    print("Wrong input")