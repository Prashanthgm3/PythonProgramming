friends = ["Prashanth","Ron","Bob"]
friends.append("Tom")
friends.remove("Bob")

join = ";".join(friends)

print(f"My friends are {join}.")


print(len(friends))
print(friends)

grades = [80, 75, 90, 100]

total = sum(grades)
length = len(grades)

average = total//length

print("The Average value", average)

