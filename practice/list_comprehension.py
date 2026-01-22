x=1
y=1
z=1
n=2

newlist=[]
newlist = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n]
# result=[]
# for x in newlist:
#     if sum(x)!=n:
#         result.append(x)
print(newlist)