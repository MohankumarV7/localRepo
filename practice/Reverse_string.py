s ="Mohan"
lst = list(s)
reverse=""
empty=[]
n = len(lst)

for i in range(0,n):
    empty.append(s[n-i-1])

for i in empty:
    reverse=reverse+i

