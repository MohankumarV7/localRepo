#string slicing

'''
len(variable) - gives the length of the string
for slicing a string we use variable[start:end:step] ex: variable[0:5:1] ex: variable[0:5]
negative indexing is also allowed in python, ex: variable[-1] gives the last character of the string
basically in negative indexing the python uses len(variable) - given index to find the character
'''



fruit = "Mango"

mangoLen = len(fruit)
print(fruit[0:4])  # including 0 but not  4
print(fruit[1:4]) # including 1 but not 4
print(fruit[:5])  # including 0 but not 5
print(fruit[0:-3]) # this will work like print(fruit[:len(fruit)-3])
print(fruit[-1:len(fruit)-3]) #this becomes 4:2 which doesn't make sense, so it will return an empty string
print(fruit[-3:-1])

## quick quiz

nm= "mohan"
print(nm [-4:-2]) 