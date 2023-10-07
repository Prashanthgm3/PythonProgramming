nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}

# Ask the user for the name of a friend

# Add the name to the empty set

# Print out the intersection between both sets. This gives us a set with those friends that are nearby.


friend = input("Enter an name")
user_friends = user_friends.add(friend)
result = user_friends.intersection(nearby_people)
print(result)