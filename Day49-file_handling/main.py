
'''
** r is the default mode if no mode is passed to open

r => reading
w => writing
a => appending in existing file
'''

# reading a file

# f = open('myFile.txt', 'r')
# f1 = open('myFile1.txt', 'w')
# text = f.read()
# print(text)
# f.close()

#Writing a file
# f = open('myfile.txt', 'w')
# # f = open('myfile.txt', 'a') 
# f.write('Hello, world!')
# f.close()


# New way of file handling, in this we need not to close the file
with open('myFile.txt','a') as f:
    f.write('hey i am inside with')
