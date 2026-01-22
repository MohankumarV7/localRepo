#  Write a function to check if a string is a palindrome

def is_palindrome(str):
    
    # if str == str[::-1]:
    #     return True
    # else:
    #     return False

    for i in range(0,len(str)):
        if str[i]==str[len(str)-i-1]:
            continue
        else:
            return False
    return True

print(is_palindrome("level"))



    
