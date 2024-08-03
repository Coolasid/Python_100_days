# def double(x):
#     return x*2

double = lambda x: x*2
cube = lambda x: x*x*x

avg = lambda x, y, z: (x+y+z)/3

def appl(fx, value):
    return 6 + fx(value)

print(double(2))
print(cube(4))
print(avg(3, 5, 10))
print(appl(cube, 2))


'''
its like arrow functions
const func = () => {
console.log('sid')
}
'''