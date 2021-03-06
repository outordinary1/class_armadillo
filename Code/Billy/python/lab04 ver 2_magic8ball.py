import random
import time

answers = ["It is certain.", "It is decidedly so.", "Reply hazy, try again.", "Ask again later.", "Don't count on it.", "Outlook good.", "Very doubtful.", "Signs point to yes.", "Hell to the NO!", "100% Yes. Sike! Lol.", "No! What are you smoking?", "You bet!"]

print('\n' + '*'*80) # border
print('Welcome to the Magic 8-Ball...where your fortune awaits!') # welcome msg
print('*'*80) # border

time.sleep(2) # time delay of 2 seconds before next line of code

while True: # while loop keeps asking questions until broken
    question = input('\n' + 'ASK MAGIC 8-BALL A QUESTION AND THEN BE AMAZED BY ITS REPLY: ') # user input string
    random_answer = random.choice(answers) # random answer randomly selected from the answers list above
    time.sleep(1.5) # time delay
    print('\n' + random_answer + '\n') # printed with line skip above and below
    time.sleep(1.5) # time delay
    next_question = input('Would you like to ask another question? (yes/no) ').lower() # user input made to lower case
    if next_question != 'yes': # if users answers above question anthing other than yes then program ends, otherwise, prompts to enter another question
        print('\nOK! Bye!\n') # good bye msg if no or anything other than yes entered
        break


'''
# Lab 4: Magic 8-Ball

Let's write a program to simulate the classic "[Magic Eight Ball](https://en.wikipedia.org/wiki/Magic_8-Ball)"

## Concepts Covered

- input, print
- import
- random.choice

## Instructions

1. Print a welcome screen to the user.
2. Use the random module's `random.choice()` to choose a prediction.
3. Prompt the user to ask the 8-ball a question "will I win the lottery tomorrow?"
5. Display the result of the 8-ball.

Below are some example 'predictions':

- It is certain
- It is decidedly so
- Without a doubt
- Yes definitely
- You may rely on it
- As I see it, yes
- Most likely
- Outlook good
- Yes
- Signs point to yes
- Reply hazy try again
- Ask again later
- Better not tell you now
- Cannot predict now
- Concentrate and ask again
- Don't count on it
- My reply is no
- My sources say no
- Outlook not so good
- Very doubtful


## Version 2

Using a `while` loop, keep asking the user for a question, if they enter 'done', exit
'''


