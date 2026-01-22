
# Given input records, filter only valid users (age > 18).

data = [
    {"name": "Mohan", "age": 23},
    {"name": "Kumar", "age": 15}
]

def valid (data):
    for items in data:
        if items["age"]>18:
            return items 
        
print(valid(data))

