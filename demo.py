
class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
        # print('in init')

    def config(self):
        print('Congif is: ', self.cpu, self.ram)


com1 = Computer('i5', 16)
com2 = Computer('Ryzen 3', 8)

print(type(com1))

com1.config()
com2.config()


def get_greeting(name: str) -> str:
    return 'Hello, ' + name
