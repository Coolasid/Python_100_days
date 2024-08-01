# string method

a = "Siddesh!!!!!!!!!!!!!"
# print(a.lower())
# print(a.upper())
# print(a.rstrip("!"))  #rstrip() removes the trailing characters
# print(a.replace("Siddesh", "Siddesh Patil")) #replace() replaces the first argument with the second argument in the string and creates a new string.
# print(a.split("!")) #split() splits the string into a list of strings based on the argument passed to it.
# print(list(a)) #list() converts the string into a list of characters.

blogHeading = "pyThon is aWesOme"
# print(blogHeading.center(50)) #center() centers the string in the specified width.
# print(blogHeading.ljust(50)) #ljust() left justifies the string in the specified width.
# print(blogHeading.rjust(50)) #rjust() right justifies the string in the specified width.
# print(blogHeading.zfill(50)) #zfill() fills the string with zeros to the specified width.
# print(blogHeading.title()) #title() converts the first character of each word to uppercase.
# print(blogHeading.capitalize()) #capitalize() converts the first character of the string to uppercase.

print(blogHeading.count('s')) #count() counts the number of occurrences of the argument passed to it.

print(blogHeading.endswith('e')) #endswith() returns True if the string ends with the argument passed to it.
print(blogHeading[2:5])
print(blogHeading.endswith('o', 2, 5)) #endswith() can also take two more arguments, start and end index, to check the string within the specified range.

print(blogHeading.find('s')) #find() returns the index of the first occurrence of the argument passed to it.

print(blogHeading.isalnum()) #isalnum() returns True if all the characters in the string are alphanumeric.

print(blogHeading.isprintable()) #isprintable() returns True if all the characters in the string are printable.


print(blogHeading.islower()) #islower() returns True if all the characters in the string are lowercase.

print(blogHeading.isupper()) #isupper() returns True if all the characters in the string are uppercase.

str1 = '             '
print(str1.isspace()) #isspace() returns True if all the characters in the string are whitespaces.


str1 = 'World Health Organization'
print(blogHeading.istitle()) #istitle() returns True if the string is in title case.

print(blogHeading.join(str1)) #join() joins the elements of the string with the argument passed to it.

print(blogHeading.swapcase()) #swapcase() swaps the case of the characters in the string.

