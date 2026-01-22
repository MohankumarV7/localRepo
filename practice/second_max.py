n = 2
# arr = map(int, input().split())

arr = [1,2,4,3]
max = 0
second=0


for i in arr:
    if i>max:
        second=max
        max=i
    if i < max and i!=max:
        second=i
print(second)

# 1, 1>0 ? --- second = 0, max = 1
# 2, 2>1? --- second = 1, max = 2
# 4, 4>2? --- second = 2 max = 4
# 3, 3>4? --- 3<4 and 3!=4 ?--- second =3
