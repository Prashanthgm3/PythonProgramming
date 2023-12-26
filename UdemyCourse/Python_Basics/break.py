cars = ["ok", "ok", "ok", "faulty","ok", "ok"]
all_successfull = True

for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        all_successfull = False
        break
    print(f"This car is {status}")
    print("Shipping new car to customer!")


else:
    print("All cars built successfully. No faulty cars!")