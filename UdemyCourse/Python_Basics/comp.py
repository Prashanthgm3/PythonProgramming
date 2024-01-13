friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = [f.lower() for f in friends]

present_friends = [

name.title()                 #list comprehension
for name in guests 
if name.lower() in friends_lower

]
print(present_friends)

# friends_lower = set([f.lower() for f in friends])
# guests_lower = set([g.lower() for g in guests])

# print(friends_lower.intersection(guests_lower))
