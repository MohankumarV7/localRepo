# For loops

'''
FOR LOOP
Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loops. Based on this loops are further classified into following main types;

1. for loop
2. while loop

for loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.

WHILE LOOP
As the name suggests, while loops execute statements while the condition is True. As soon as the condition becomes False, the interpreter comes out of the while loop.

Else with While Loop

We can even use the else statement with the while loop. 
Essentially what the else statement does is that as soon as the while loop condition becomes False, the interpreter comes out of the while loop and the else statement is executed.

x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('counter is 0')
'''


'''
Do-While loop in python
do..while is a loop in which a set of instructions will execute at least once (irrespective of the condition) and then 
the repetition of loop's body will depend on the condition passed at the end of the while loop. It is also known as an exit-controlled loop.

To create a do while loop in Python, you need to modify the while loop a bit in order to get similar behavior to a do while loop.

The most common technique to emulate a do-while loop in Python is to use an infinite while loop with a break statement wrapped in an if statement 
that checks a given condition and breaks the iteration if that condition becomes true:

while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break
    
This loop uses True as its formal condition. This trick turns the loop into an infinite loop. 
Before the conditional statement, the loop runs all the required processing and updates the breaking condition. 
If this condition evaluates to true, then the break statement breaks out of the loop, and the program execution continues its normal path.

'''