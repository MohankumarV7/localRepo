sentence = '''HackerRank.com presents "Pythonist 2".''' 

s2 = "".join([ i.lower() if i.isupper() else i.upper() for i in sentence])


'''-------below are the common o(n)2 mehtod'''
# newsentence=""
# for i in sentence:
#     if i == i.upper():
#         newsentence=newsentence+i.lower()
#     elif i==i.lower():
#         newsentence=newsentence+i.upper()
# print(newsentence)

# print(sentence.swapcase())


# s2=""
# for i in sentence:
#     if i.isupper():
#         s2= s2+i.lower()
#     else:
#         s2=s2+i.upper()

print(s2)