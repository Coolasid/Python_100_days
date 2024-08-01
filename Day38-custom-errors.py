a = input('enter any value bt 5 and 9: ')

if a == 'quit':
    exit()
elif int(a)< 5 or int(a)> 9: 
    raise ValueError("value should be bt 5 and 9")

