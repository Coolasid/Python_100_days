class Employee:
    def __init__(self, name, emp_id) -> None:
        self.name = name
        self.emp_id = emp_id

    def show_details(self):
        print(f'The name of Employee: {self.name} is {self.emp_id}')


class Programmer(Employee):
    def show_language(self):
        print('The default language is Python')


e = Employee('siddesh', 69)

e.show_details()

e2 = Programmer('sid', 49)
e2.show_language()