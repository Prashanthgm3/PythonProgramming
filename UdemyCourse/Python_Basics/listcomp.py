numbers = range(0,99)
doubled_numbers = []

#for number in numbers:
 #   doubled_numbers.append(number * 2)

doubled_numbers = [number * 2 for number in numbers] # 2nd way of list comprehension
print(doubled_numbers)


friend_ages = [22, 31, 35, 37]
age_strings = [f"My friend is {age} years old" for age in friend_ages]

print(age_strings)

names = ["ROLF", "BOB", "JEN"]
names2 = ["a","b","c"]


friend = input("Enter your friends name?")
friends = ["Rolf", "Bob", "Jen", "Charlie", "Anne"]

if friend in friends:
    print(f"{friend} is one of your friends.")

else:
    print(f"{friend} Name not found")