# python docstrings are the string literals that apperar right after the defination of a function, method, classs or module.
# ** We need to specify docstring right after function name. 

def square(n):
  '''Take in a number n, returns the square of n '''
  print(n**2)

square(5)
print(square.__doc__) # its not a common string, python stores it as a value 


