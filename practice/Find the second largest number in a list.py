# Find the second largest number in a list

def second_largest(lst):
    second = 0
    largest = 0
    

    for i in lst:
        if i > largest:
            second=largest
            largest=i
        elif i > second and i!= largest:
            second = i

    return second

def simple(nums):
    unique = list(set(nums))
    unique.sort()
    return unique[-2]

print(second_largest([10, 20, 4, 45, 99]))
print(simple([10, 80, 42, 34, 99]))



