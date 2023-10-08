
'''user_input = input("Do you want to enter p or q")
while user_input:
        if user_input == "p":
            print("Hello")
            user_input=input("Do you want to continue")
        else:
            user_input = False
 '''

     # Ask the user to choose one of two options:
    # if they type 'p', our program should print "Hello" and then ask the user again. Keep repeating this until...
    # if they type 'q', our program should terminate.
     
    # Let's begin by asking the user to type either 'p' or 'q':
user_input = input("Enter q or p: ")
     
    # Now we must repeat until they type 'q':
while user_input != "q":
        # Inside our loop, check if they typed 'p'. If they did, print "Hello"
        if user_input == "p":
            print("Hello")
        # Now we must ask the user for their input again—otherwise we would be in an infinite loop!
        user_input = input("Enter q or p: ")           