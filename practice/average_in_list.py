d = {'Krishna': [67.0, 68.0, 69.0], 'Arjun': [70.0, 98.0, 63.0], 'Malika': [52.0, 56.0, 60.0]}
values = len(d.values())

list1 =[]

for i in d.values():
    list1.append(i)

# print(list1)
# sum = 0
average=0
avg = []
for i in list1:
    sum=0
    for j in range(len(i)):
        
        sum = sum+i[j]
    average=sum/len(i)
    avg.append(average)
# print(avg)
new_dic={}

j=0
for key in d.keys():
        for i in range(-1,j):
            new_dic[key]=avg[j]
            break
        j+=1
            # new_dic.values=

    
items_list = list(new_dic.items())
# print(items_list)

for key,value in new_dic.items():
     if key=="Malika":
          print(f"{value:.2f}")

