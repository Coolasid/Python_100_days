#dictonary are ordered collection of key and value pair


dic ={
    'sid':'human being',
    'spoon':'Object'
}

print(dic.get("sid")) 
print(dic["sid"])

#** the main diff bt get and [] is that if key is not present in the dict then get will give None but [] will give error
print(dic.get("sid1"))


info = {'name': 'Siddesh', 'age':23, 'eligible':True}
print(info.keys()) 

for key in info.keys():
    print(info[key])

print(info.values())

#** to get key value pairs
print(info.items())

for key, value in info.items():
    print(f'The value correspoding to the key {key} is {value}')