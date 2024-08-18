class Employee:
    company = 'Apple'
    def show(self):
        print(f'The name is {self.name} and company is {self.company}')

    @classmethod # by doing so
    def change_company(cls, new_company):
        cls.company = new_company

    
e1 = Employee()
e1.name = 'Harry'
e1.show()
e1.change_company('google') # change the company name of the instance of e1
e1.show() 
print(Employee.company) # Apple, by adding @classmethod it changes company name to google

