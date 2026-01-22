#  Sort a dictionary by value

data = {"data": 3, "engineering": 1, "python": 2}

sorted = dict(sorted(data.items(), key = lambda x:x[1]))



print(sorted)


# n = ['5', '10', '9', '1']
# n=map((lambda x:str(x)),n)
# print(list(n))