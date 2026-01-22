'''Count the number of words in a given sentence. A word is defined as any sequence of characters separated by whitespace. Punctuation, hyphens, and underscores that appear within or around words are not treated as separators.

Constraints
The input variable sentence must be a string.'''

sentence = str(input("enter the word:"))

words = sentence.strip().split()
# print(len(words))

'''
The split() method without arguments already ignores leading and trailing whitespace, 
so in most cases strip() is not necessary when using split() without parameters.

split() automatically ignores leading and trailing whitespace and treats multiple spaces as one separator.

But if you use split(' ') with a space character explicitly, then strip() matters:

sentence = "   Hello   world  "
words = sentence.split(' ')
print(words)
# Output: ['', '', '', 'Hello', '', '', 'world', '', '']

'''
ls=sentence.strip().split()
# count=0
newls = {}
for i in ls:
    count = 0
    for j in range(0,len(ls)):
        if  i==ls[j]:
            count+=1  
    newls[i]=count

print(newls)
    
