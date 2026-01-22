'''
EXERCISE:

Create a program capable of displaying questions to the user like KBC. Use List data type to store the questions and their correct answers. 
Display the final amount the person is taking home after playing the game.

'''
def crorepathi(questions, answers):
 
    count = 0
    i=0
    for j in questions:
        print(j)
        user_ans = str(input())

        if user_ans == answers[i]:
            count+=1
            i+=1
            continue
        else:
            return count
    return count
                

questions = [
    "1. What is the capital of France?",
    "2. Who wrote the play 'Romeo and Juliet'?",
    "3. What is the largest planet in our solar system?",
    "4. Which gas do humans need to breathe to survive?",
    "5. What is the chemical symbol for water?",
    "6. Who was the first person to step on the Moon?",
    "7. In which year did India gain independence?",
    "8. What is the square root of 81?",
    "9. Which animal is known as the King of the Jungle?",
    "10. What is the fastest land animal?"
]

answers = [
    "Paris",
    "William Shakespeare",
    "Jupiter",
    "Oxygen",
    "H2O",
    "Neil Armstrong",
    "1947",
    "9",
    "Lion",
    "Cheetah"
]



values_dict = {
    0: "Sorry, wrong answer. You won X amount",
    1: 100,
    2: 1000,
    3: 10000,
    4: 100000,
    5: 1000000,
    6: 10000000,
    7: 100000000,
    8: 1000000000,
    9: 10000000000,
    10: 100000000000
}

result = crorepathi(questions,answers)
answered_no = list(values_dict.keys())
amount = list(values_dict.values())
if result in answered_no:
    print(f"user count of right answers out of 10 is: ", result, "and the amount won is: ",amount[result])


    