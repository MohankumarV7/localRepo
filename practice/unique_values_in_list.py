# Unique Order Values

'''
Find unique values in a given list.

Constraints
The input variable must be a list of integers.
There are no constraints on the length of the input list.
The input list can contain both positive and negative integers.
The input list can contain duplicate values.
The order of the elements in the input list must be preserved in the output list.

'''

def find_unique(values):
    seen = set()
    unique = []

    for num in values:
        if num not in seen:
            seen.add(num)
            unique.append(num)

    return unique
            

values = list(map(int, input("Enter the values with comma seperated: ").split(',')))
output=find_unique(values)
print(output)
