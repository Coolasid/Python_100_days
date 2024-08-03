a = 4
b = '4'

print(a == b) # exact location of object in memory , False
print( a is b) # value, False



a = [1,2, 3, 4]
b = [1, 2,3 , 4]

print(a == b) # True
print(a is b) # False

#python creates different memory location for the mutable value so is will be False 




a = 3
b = 3

c = 'sid'
d = 'sid'

e = (1, 2)
f = (1, 2)

g = None
h = None

print(a == b) # True
print(a is b) # True

print(c == d) # True
print(c is d) # True

print(e == f) # True
print(e is f) # True

print(g == h) # True
print(g is h) # True
print(g is None) # True

# If we compare an immutable values then we will get true in both the cases, because python stores it in only one location for memory optimization.

