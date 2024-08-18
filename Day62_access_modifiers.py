# public, private, protected

'''
public -> can be access from anywhere
protected -> can be access from only subclass only
private -> access within the class only
'''

class Employee:
    def __init__(self) -> None:
        self.__name = 'Siddesh'


a = Employee()
# print(a.__name) # cannot be access directly
# print(a._Employee__name)  # can be access indirectly (name mangling)
# print(a.__dir__())



class Student:
    def __init__(self) -> None:
        self._name = 'Siddesh'

    def _fun_name(self):
        return 'Siddesh Patil'

class Subject(Student):
    pass

obj = Student()
obj1 = Subject()

print(dir(obj))

print(obj._name)
print(obj._fun_name())

print(obj1._name)
print(obj1._fun_name())