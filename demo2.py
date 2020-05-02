class Computer:
    
    def __init__(self):
        self.name = 'Vaibhav'
        self.age = 24

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False    



c1 = Computer()
c2 = Computer()

if c1.compare(c2):
    print('They are same')

# Every time you create an object it is allocated to new space.
print(id(c1))
print(id(c2))

c1.name = "Rich"

print(c1.name)
print(c2.name)