# Exception handling in Python

try:
    value = int(input("enter an integer: "))
    print(value)
except ValueError:
    print("enter a valid integer")