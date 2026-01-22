'''
Given a list of values containing NULLs, for every null value, replace it with its preceding non-null value.

Constraints
The input variable lst is a list.
The elements of lst can be either integers or None.
The length of lst can be any positive integer.
The list lst may contain multiple consecutive None values.
The list lst may start with a None value.
The list lst may end with a None value.

Test Case #1
Input: [null, 5, null, 8, null, null, 3, null]
Output: [null, 5, 5, 8, 8, 8, 3, 3]
Description: This test case assesses the function’s ability to handle lists with null values at the beginning 
and multiple consecutive null values.
'''


def replace_null_values(lst):
    
    rep_value = None
    result= []
    
    for i in lst:
        if i is not None:
            rep_value = i 
        result.append(rep_value)
    return (result)
            
lst = [12, 14, None, None, 7, None, 19, None, None, 23]
print(replace_null_values(lst))
