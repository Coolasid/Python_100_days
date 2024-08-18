class Employee:
    company_name = 'apple' # this is class vairable
    no_of_employees = 0

    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02 # this is instance variables
        Employee.no_of_employees += 1

    def show_details(self):
        print(f'The name of the Employee is {self.name} and the raise amount in {self.company_name} is {self.raise_amount} ')

    

emp1 = Employee('Harry')
emp1.raise_amount = 0.03
emp1.company_name = 'apple india' # this is instance variable we are making to change company name 
emp1.show_details()
Employee.company_name = 'google' 
print(Employee.company_name)

emp2 = Employee('Rohan')
emp2.company_name = 'apple USA'
emp2.show_details()