class Employee:
    def __init__(self):
        print("This is employee constructor")

    def display(self):
        print("This is display method")

class Manager(Employee):
    Employee
    print("This is Manager construtor")

M1=Manager()
M1.display()