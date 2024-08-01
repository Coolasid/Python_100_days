# a = input('enter the number: ')

# print(f'multiplication table of {a} is:')

# try:
#     for i in range(1, 11):
#         print(f'{int(a)} X {i} = {int(a)*i}')
# except:
#     print('Invalid input!')


# print("some lines of code")
# print("end of program")


# try:
#     num = int(input('Enter an integer: '))
#     a = [6, 3]
#     print(a[num])
# except ValueError:
#     print("Number entered is not an integer.")
# except IndexError:
#     print('Index Error')
# finally:
#     print('In the finally')


#** In the below function finally will run even if we return from the try or except block 

'''
usecases of finally 
1. db connection break
2. cleanup call of a function
'''

def func1():
    try:
        l = [1, 2, 3, 4 ,54 ]
        i = int(input("enter the index:"))
        print(l[i])
        return 1
    except:
        print('some error occurred')
        return 0
    finally:
        print('I am always executed')
    # print('I am always executed')


x = func1()
print(f"==>> x: {x}")

