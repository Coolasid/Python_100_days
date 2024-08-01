with open('myFile.txt', 'r') as f:
    print(type(f))

    f.seek(10) # Move to the 10th byte/char in the file

    print(f.tell()) # gives the current position 
    #Read the next 5 bytes/char
    data = f.read(5)
    print(f"==>> data: {data}")




with open('sample.txt', 'w') as f:
    f.write('Hello world!')
    f.truncate(5) ## truncate the file to only 5 bytes/chars


with open('sample.txt', 'r') as f:
    print(f.read())