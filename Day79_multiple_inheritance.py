class Employee:
    def __init__(self, name) -> None:
        self.name = name
    
    def show(self):
        print(f'The name is {self.name}')

class Dancer:
    def __init__(self, dance) -> None:
        self.dance = dance

    def show(self):
        print(f'The dance is {self.dance}')

class DancerEmployee(Employee, Dancer):
    def __init__(self, dance, name) -> None:
        self.dance = dance
        self.name = name

o = DancerEmployee('Kathak', 'Shivani')

print(o.name)
print(o.show())
print(o.dance)

print(DancerEmployee.mro())