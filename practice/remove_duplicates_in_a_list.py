# Remove duplicates from a list
# Question:

# Remove duplicates from a list while maintaining order.

list = [1,1,1,2,3,4,5,6,6,6,7]
seen = set()
ls1 = []

for i in list:
    if i not in seen:
        seen.add(i)
        ls1.append(i)

print(ls1)