'''
Check if a given input is a palindrome.

Constraints
The input variable s must be a string.
'''

def is_palindrome(s):

    # return s == s[::-1]
    '''
    So what does s[::-1] do?
    s = "abcdef"

    print(s[::1])   # "abcdef" (normal order)
    print(s[::2])   # "ace"    (skip every 2nd character)
    print(s[::-1])  # "fedcba" (step = -1 → go backwards)
    Effectively, it reverses the string.
    '''
    n = len(s)
    
    for i in range(n//2):
        if s[i]!=s[n-i-1]:
            return False
    return True

print(f"This is: ",is_palindrome("ablewasiereisawelba"),"palindrome")  
    