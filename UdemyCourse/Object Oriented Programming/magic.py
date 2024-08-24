##class Student:
  ##  def __init__(self, name):
    ##    self.name= name

## movies = ['Matrix', 'Finding Nemo']

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self): #length dunder function
         return len(self.cars)

    def __getitem__(self, i): #getitem dunder function
        return self.cars[i]

    def __repr__(self):
        return f'<Garage {self.cars}>' #used when debugger

    def __str__(self):  #string dunder method
        return f'Garage with {len(self)} cars'

ford = Garage()
ford.cars.append('Fiesta123')
ford.cars.append('Icon')
ford.cars.append('FreeStyle')
ford.cars.append('Innova')

#print(len(ford))
#print(ford.cars[0])
#print(ford[1]) # Garage.__getitem__(ford, 0)

#for car in ford:
 #   print(car)

print(ford)