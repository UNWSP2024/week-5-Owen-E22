# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.
import random


def quiz():

    loop = 'y'
    while loop == 'y':
        number1 = random.randint(1,200)
        number2 = random.randint(1,200)
        print(number1, '+', number2, '=')
        user_answer = int(input('Enter answer here: '))
        answer = number1 + number2
        if user_answer == number1 + number2:
            print('Congratulations, that is correct')
            loop = str(input('Would you like another problem(y for yes)?'))
        else:
            print('That is incorrect, the answer is ',answer)
            loop = str(input('Would you like another problem(y for yes)?'))
quiz()