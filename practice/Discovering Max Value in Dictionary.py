'''
Find the maximum value, its key, and index from a dictionary. Assume all values are unique.

Constraints
The input variable dictionary must be of type dict.
The dictionary must contain unique values.

'''
def find_max_value(data):


    keys = list(data.keys())

    lst = []
    result=[]

    for i in data:
        lst.append(data[i])

    max = 0

    for i in range(0,len(lst)):
        if lst[i]>max:
            max = lst[i]
    result.append(max)

    for i in data:
        if data[i]==max:
            track = i
            result.append(i)

    for i in range(len(keys)):
        if keys[i]==track:
            result.append(i)
    return result

input = {"pear": 75, "apple": 100, "peach": 150, "banana": 50} 
ouput = find_max_value(input)
print(ouput)


'''
OPTIMIZED way:

def find_max_value(data):
    keys = list(data.keys())
    max_key = max(data, key=data.get)
    max_value = data[max_key]
    key_index = keys.index(max_key)
    
    return [max_value, max_key, key_index]



'''