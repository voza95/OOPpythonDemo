class Car:
    # Class variables or static variable
    wheels = 4
    def __init__(self):
        self.mil = 10
        self.com = 'BMW'
        
c1 = Car()
c2 = Car()

c1.mil = 5

Car.wheels = 5

print(c1.mil, c1.com, c1.wheels)
print(c1.mil, c1.com, c1.wheels)