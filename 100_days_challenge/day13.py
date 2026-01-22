# string methods

'''
string is immutable in python, which means that once a string is created, it cannot be changed.

however, you can create new strings based on existing ones using various string methods. 

string methods are built-in functions that can be used to manipulate strings in various ways.
some common string methods include:
- upper(): converts all characters in a string to uppercase
- lower(): converts all characters in a string to lowercase
- strip(): removes leading and trailing whitespace from a string
- replace(old, new): replaces all occurrences of a substring with a new substring
- split(separator): splits a string into a list of substrings based on a separator
- join(iterable): joins a list of strings into a single string with a specified separator
'''

str = "!! mohan !!"
print(str.upper())  # MOHAN
print(str.strip("!"))  # mohan this removes leading and trailing '!'
print(str.rstrip("!"))  # mohan this removes trailing '!'
print(str.replace("mohan", "mohit"))  # !!mohit!!
print(str.split(" "))  # ['', '', 'mohan', '', ''] this splits the string into a list of substrings based on the separator ' '

heading = "welcome to python"
print(heading.capitalize())  # This capitalizes the first character of the string
print(heading.title())  # This capitalizes the first character of each word in the string

print(heading.center(30, '*'))  # This centers the string within a width of 30 characters, filling with '*' the default fill character is space
print(heading.count('o'))  # This counts the number of occurrences of 'o' in the string
print(heading.endswith('n'))  # This checks if the string ends with 'n'
print(heading.endswith('to', 4,10))  # This checks if the string ends with 'to' in the range of index 4 to 10
print(heading.find('to'))  # This finds the first occurrence of 'to' in the string and returns its index, raises -1 if not found
print(heading.index('to'))  # This finds the first occurrence of 'to' in the string and returns its index, raises ValueError if not found
print(heading.isalnum())  # This checks if the string is alphanumeric (contains only letters and numbers)
print(heading.isalpha())  # This checks if the string contains only alphabetic characters
print(heading.isprintable())  # This checks if the string is printable (contains only printable characters) (\n, \t, etc. are not printable)
print(heading.isspace())  # This checks if the string contains only whitespace characters

