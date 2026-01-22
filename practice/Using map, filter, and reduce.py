# Using map, filter, and reduce

from functools import reduce
nums = [1, 2, 3, 4]

map_conecept = list(map(lambda x : x*2, nums))
filter_concept = list(filter(lambda x:x%2==0, nums))
reduce_conecpt = reduce(lambda x,y:x+y, nums)

print(f"{map_conecept},{filter_concept},{reduce_conecpt}")