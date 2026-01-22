# if __name__ == '__main__':
#     scores =[]
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         scores.append([name,score]) 

# print(scores)

second = float('inf')
lowest = float('inf')
newlist = []
# scores = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]

scores = [
 ['Harry', 37.21],
 ['Berry', 37.21],
 ['Tina', 37.2],
 ['Akriti', 41.0],
 ['Harsh', 39.0]
]
sorted_scores = sorted(set(score for _,score in scores))
print(sorted_scores)

if len(sorted_scores)>1: 
    second=sorted_scores[1]
    names = [name for name,score in scores if score==second ]
    for name in sorted(names):
        print(name)