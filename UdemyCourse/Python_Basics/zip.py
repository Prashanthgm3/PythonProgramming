friends = ["Rolf", "Bob", "Jen", "Anne","Prashanth"]
time_since_seen = [3, 7, 15, 11]

long_timers = dict(zip(friends, time_since_seen))



# long_timers = {

#     friends[i]: time_since_seen[i]
#     for i in range(len(friends))
#     if time_since_seen[i] > 5
# }

print(long_timers)