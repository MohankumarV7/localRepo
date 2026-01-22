'''
Alphabetize Strings

Sort a given string alphabetically.

Constraints

The input variable string must be a string.
There are no specific constraints on the length of the string.

Test Case #1
Input: "zxbyacd"
Output: "abcdxyz"
Description: This test case involves a mix of letters that are not in alphabetical order to verify the function’s ability to sort efficiently.

Test Case #2
Input: "escapevelocity"
Output: "acceeeilopstvy"
Description: The function is tested with a longer string containing varied characters to ensure correct alphabetical sorting over a more extensive sequence.

Test Case #3
Input: "PythonRocks"
Output: "PRchknoosty"
Description: A mixed-case string to check if the sorting function correctly respects the case sensitivity (where uppercase letters come before lowercase letters in ASCII).
'''

##################################################################################
## BUBBLE SORT ##

'''
Imagine:

You have a row of kids standing in a line, and each is holding a number card. You want them arranged from smallest to biggest number.

How Bubble Sort works:

Compare two kids standing next to each other.
If the left kid is holding a bigger number than the right kid → swap their places.
(So the bigger number goes one step to the right.)

Move to the next pair (kid 2 & kid 3) and do the same thing.
Keep repeating this until you reach the end of the line.

By the time you reach the end, the biggest number "bubbles up" to the last position (like a bubble rising to the top of water).

Now, ignore the last kid (since they are already in the correct spot) and repeat the process for the rest.

Keep doing this until no swaps are needed → then the kids are sorted in order.

Example:

Kids holding cards:
[5, 2, 4, 1]

Step 1: Compare 5 and 2 → swap → [2, 5, 4, 1]

Step 2: Compare 5 and 4 → swap → [2, 4, 5, 1]

Step 3: Compare 5 and 1 → swap → [2, 4, 1, 5]
👉 Now, 5 is at the end (largest bubbled up).

Next round (ignore last element now):

Compare 2 and 4 → no swap → [2, 4, 1, 5]

Compare 4 and 1 → swap → [2, 1, 4, 5]

Next round:

Compare 2 and 1 → swap → [1, 2, 4, 5]

Now sorted ✅

'''

def sort_string(string):
    """
    :type string: str
    :rtype: str
    """
    temp = ""
    # sorted_list = sorted(string)

    # for i in sorted_list:
    #     temp= temp+i
    # print(temp)

    lst = list(string)
    
    n = len(lst)

    for i in range(n):
        for i in range(n-i-1):
            if lst[i]>lst[i+1]:
                lst[i+1],lst[i] = lst[i],lst[i+1]
    for i in lst:
        temp=temp+i
    print(temp)


sort_string("zxbya")