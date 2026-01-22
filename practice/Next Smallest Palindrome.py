'''
Given a number as an input, find the following smallest palindrome number. For simplicity, 
assume the input value will not exceed 1 million. The next palindrome may be greater than 1 million.

Constraints:

--The input variable n is an integer.
--The input value n will not exceed 1,000,000. The resulting palindrome may be greater than this limit.

Test Case #1
Input: 123
Output: 131
Description: This test case checks the algorithm""s ability to find the next palindrome for a small 
three-digit number that is far from being a palindrome.


Test Case #2
Input: 999999
Output: 1000001
Description: This case challenges the function with a number close to the given upper limit, 
ensuring it can handle boundary cases and large numbers efficiently.


Test Case #3
Input: 123456
Output: 124421
Description: This case tests the algorithm""s efficiency with a six-digit number, ensuring it can 
find the following palindrome in a sequence with a larger search space.
'''

def next_palindrome(integer):
    """
    :type n: int
    :rtype: int
    """

    # for i in range(integer+1,10000000):
    #     if str(i)==str(i)[::-1]:
    #         return i

    for i in range(integer+1,1000000):

        data= str(i)
        n=len(data)      
        is_palindrome=True
        for j in range(n//2):
            if data[j] != data[n-j-1]:
                is_palindrome = False
                break
        if is_palindrome:
            return i
        return data
    
    
integer = int(input())
print(next_palindrome(integer))

