class Employee:
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, string):
        return cls(string.split('-')[0], string.split('-')[1])


e1 = Employee('siddesh', 12000)

string = 'Siddesh-12000'

e2 = Employee(string.split('-')[0], string.split('-')[1] )

e3 = Employee.from_string(string)

print(e3.name)
print(e3.salary)

