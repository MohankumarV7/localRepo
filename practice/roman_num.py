s='MCMXCIV'
new_str=s.split()
n=len(s)
roman = {
    "I"         :1,
    "V"         :5,
    "X"         :10,
    "L"         :50,
    "C"         :100,
    "D"         :500,
    "M"         :1000,
}
total = 0
for i in range(n-1):
    print(i)
    if roman[s[i]]<roman[s[i+1]]:
        total-=roman[s[i]]
    else:
        total+=roman[s[i]]

total += roman[s[-1]]

print(total)

