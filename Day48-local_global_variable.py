
x = 4

print(x)

def hello():
    global x
    global y
    x = 5
    y = 10
    print(f'The local x is {x}')
    print("hello siddesh")

print(f'The global x is {x}')
hello()
print(f'The global x is {x}')
print(f'The global y is {y}')