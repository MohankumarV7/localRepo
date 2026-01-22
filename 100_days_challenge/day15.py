'''
Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. 
Your program should use time module to get the current hour. Here is a sample program and documentation link for you:
'''

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime

if int(time.strftime('%H')) >= 0 and int(time.strftime('%H')) < 12:
    print("Good morning")
elif int(time.strftime('%H')) >= 12 and int(time.strftime('%H')) <= 16:
    print("Good Afternoon")
else :
    print("Good Evening")
