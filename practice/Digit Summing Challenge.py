'''
Sum the digits of every number in a list.

Constraints
The input variable numbers is a list of integers.
The integers in the list can be positive or negative.
The integers in the list can have multiple digits.
The length of the list can be any positive integer.
The integers in the list can be within the range of the integer data type.

Test Case #1
Input: [12345, 67890, -12345, -67890]
Output: [15, 30, 15, 30]
Description: This test case includes positive and negative multi-digit integers to test the function"s ability 
to correctly handle negative numbers and sum their digits irrespective of the sign.


Test Case #2
Input: [0, -111, 2222, -33333, 444444]
Output: [0, 3, 8, 15, 24]
Description: The function is tested with leading zero, negative numbers, and sequences of the same digit to verify 
that digit summation is handled consistently across various simple and repetitive patterns.
'''

def sum_digits(numbers):
    """ 
    :type numbers: List[int]
    :rtype: List[int]
    """
    result=[]
    for i in numbers:
        track=abs(i)
        sum_digits = sum(int(d) for d in str(track))
        result.append(sum_digits)
    return result

print(sum_digits([12345, 67890, -12345, -67890]))