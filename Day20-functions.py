def average(a=9, b=1):
  print('The avg is ', (a+b)/2)


average(1, 4)

average(b = 9, a = 21) # keyword arguments, in this we does not require to follow the sequence of argurments


#* variable length argument
def greet(*name): # *name takes argument as a array
  print('hello', name[0], name[1], name[2])

greet('sid',  'dinesh', 'patil')

def greet(**name): # **name takes argument as a dictonary/object
  print('Hello', name['fname'], name['mname'], name['lname'])

greet(fname = 'sid',  lname = 'patil', mname = 'dinesh')
