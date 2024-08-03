from functools import reduce


def cube(x):
    return x*x*x


l = [1, 2, 3, 4, 5 ]

map_l = list(map(cube, l))
map_lambda_l = list(map(lambda x: x*x*x, l))

print(f"==>> map_lambda_l: {map_lambda_l}")
print(f"==>> map_l: {map_l}")



def filter_function(a):
    return a<4

filter_l = list(filter(filter_function, l ))
filter_lambda_l = list(filter(lambda a: a<4, l ))


print(f"==>> filter_lambda_l: {filter_lambda_l}")
print(f"==>> filter_l: {filter_l}")



sum = reduce(lambda x, y: x+y, l)
print(f"==>> sum: {sum}")