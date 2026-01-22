
thickness = 5 #This must be an odd number
c = 'H'

for i in range(thickness+1):

    print((c*(i)).rjust(thickness)+(c*(i-1)).ljust(thickness))

for i in range(thickness):
    print((c*(thickness)).center(thickness*2) +(c*(thickness)).center(thickness*6))

for i in range(thickness):
    print((c*(thickness*5)).center(thickness*6))
for i in range(thickness):
    print((c*(thickness)).center(thickness*2) +(c*(thickness)).center(thickness*6))
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

