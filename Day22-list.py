# l = [3, 4, 5, 4, 5, 7, 2, 7]

# print( type(l))

# if 6 in l:
#   print('Yes')
# else:
#   print("No")


# #same this applies for stirng as well
# # if 'sid' in 'siddesh':
# #   print('Yes')

# print(l[2:6])
# print(l[1:-1]) # l[1:7]
# # [4, 5, 4, 5, 7, 2]

# print(l[1: 7: 2])

# list comprehension
lst = [i for i in range(100)]
print(lst)

lst = [i*i+1 for i in range(100)]
print(lst)

#to make a list of only even numbers
lst = [ i for i in range(100) if i%2 == 0]
print(lst)

#to filter elements in the list
names = ['Milo', 'Sarah', "Bruno", 'Anastasia', "Rosa"]

namesWith_0 = [item for item in names if 'o' in item]
print(namesWith_0)

names_len_4 = [name for name in names if len(name) > 4]
print(names_len_4)



