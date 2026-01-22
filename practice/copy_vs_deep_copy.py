import copy

a = [[1,2], [3,4]]
b = copy.copy(a)
c = copy.deepcopy(a)

a[0][0] = 99

print(b)  # changed
print(c)  # unchanged
