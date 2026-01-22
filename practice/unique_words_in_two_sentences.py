'''
Find non-repeated words in any given 2 sentences.

Constraints
The input variables sentence1 and sentence2 must be of type str.
There are no specific constraints on the length or format of the sentence
'''

import re
def non_repeated_words(input):
    """
    :type input: List[str]
    :rtype: List[str]
    """
    sentence1 = input[0]
    sentence2 = input[1]
    sentence1_updated = re.sub(r"(\w)'s\b",r"\1s",sentence1)
    sentence1_updated = re.sub(r"(\w)'\b",r"\1",sentence1)
    
    sentence2_updated = re.sub(r"(\w)'s\b",r"\1s",sentence2)
    sentence2_updated = re.sub(r"(\w)'\b",r"\1",sentence2)
    
    words_in_str1 = re.findall(r"\b\w+\b", (sentence1_updated))
    words_in_str2 = re.findall(r"\b\w+\b", (sentence2_updated))
    
    unique= []
    for words in words_in_str1 :
        if words not in words_in_str2:
            unique.append(words)
    
    for words in words_in_str2:
        if words not in words_in_str1:
            unique.append(words)
    return(unique)
            

input = list(map(str,input().split(',')))
result = non_repeated_words(input)
print(result)