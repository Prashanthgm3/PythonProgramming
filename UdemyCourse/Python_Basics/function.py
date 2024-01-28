# def greet():
#     name = input("Enter your name")
#     print(f"Welcome to Python  {name}")

# greet


car = [
    
    { "make": "Toyota","model": "Innova","mileage": 23000,"fuel_consumed": 460},
    { "make": "Toyota","model": "Innova","mileage": 22454,"fuel_consumed": 800},
    { "make": "Toyota","model": "Innova","mileage": 5646,"fuel_consumed": 457},
    { "make": "Toyota","model": "Innova","mileage": 7678,"fuel_consumed": 657} ,   
        
        ]


def calculate_mpg(car_to_calculate):
    mpg = car_to_calculate["mileage"] / car_to_calculate["fuel_consumed"]
    name = f"{car_to_calculate['make']} {car_to_calculate['model']}"
    print(f"{name} does {mpg} miles per gallon.")

calculate_mpg(car[2])