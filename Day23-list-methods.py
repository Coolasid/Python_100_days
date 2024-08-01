l = [1, 2, 3, 4, 3, 1]
print(l)
l.append(7)
# l.sort()
# l.sort(reverse=True)
# l.reverse()
# print(l.index(1)) # this method returns the first occurance index of the element

# print(l.count(1)) # count the occurance of the element

# m = l.copy() # this make a new copy of the list and use pass by value phenomena
# m[0] = 0
# print(l)

l.insert(1, 899)



m = [900, 1000, 1100]

l.extend(m) # One of the method to concate the array

k = l + m  # another method to concate the array
print(f"==>> k: {k}")

print(l)


