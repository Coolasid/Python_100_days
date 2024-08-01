# f = open('myFile.txt', 'r')

# while True:
#     line = f.readline() # reading file line by line
#     print(line)
#     if not line:
#         print(line, type(line))
#         break

# f1 = open('myFile1.txt', 'r')
# i = 0
# while True:
#     line = f1.readline() # reading file line by line
#     if not line:
#         print(line, type(line))
#         break
#     m1 = line.split(',')[0]
#     m2 = line.split(',')[1]
#     m3 = line.split(',')[2]
#     print(f'marks of student {i} in maths is: {m1} ')
#     print(f'marks of student {i} in english is: {m2} ')
#     print(f'marks of student {i} in sst is: {m3} ')
#     print(line)
#     i+=1
  

f = open('myFile2.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()