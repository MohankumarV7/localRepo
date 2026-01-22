'''
Find common words in any given two sentences and return them sorted alphabetically.

Constraints
The input variables sentence1 and sentence2 must be of type str.
The input sentences should not be empty.
The sentences can contain any characters, including letters, numbers, punctuation marks, and whitespace.
The sentences can be of any length, from empty strings to very long sentences.
The sentences are case-insensitive, meaning that the comparison of words should be done in a case-insensitive manner.
The sentences can contain duplicate words, but the output set should only contain unique common words.
'''


import re
def find_common_words(input):

    sentence1 = input[0]
    sentence2 = input[1]

    sentence1_updated = re.sub(r"(\w)'s\b",r"\1s",sentence1)
    sentence1_updated = re.sub(r"(\w)'\b",r"\1",sentence1)
    
    sentence2_updated = re.sub(r"(\w)'s\b",r"\1s",sentence2)
    sentence2_updated = re.sub(r"(\w)'\b",r"\1",sentence2)
    


    
    words_in_str1 = re.findall(r"\b\w+\b", (sentence1_updated.lower()))
    words_in_str2 = re.findall(r"\b\w+\b", (sentence2_updated.lower()))
    
    seen = set()
    common= []
    for words in words_in_str1 :
        if words in words_in_str2:
            common.append(words)
    return sorted(common)

input = list(map(str,input().split(',')))
result = find_common_words(input)
print(result)





