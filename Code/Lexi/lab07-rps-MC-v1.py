import random

#python is the only language with the while True else issue - Matt C

rps = ['rock', 'paper', 'scissors']
human_score = 0
comp_score = 0

while True:         # advantage of while True loops is you can choose any point to break
comp_choice = random.choice(rps)

while True:
    human_choice = input('Rock, paper or scissors? ').lower().strip()
    if human_choice in rps:
        break
    print('please enter a valid option')

human_choice = None #got to set this
while human_choice not in rps:
    human_choice = input('Rock, paper or scissors? ').lower().strip()


if human _choice == comp_choice:
    print('tie')
elif human_choice == 'rock' and comp_choice == 'paper':
    print('computer wins')
elif human_choice == 'rock' and comp_choice == 'scissors':
    print('homo sapien wins')
elif human_choice == 'rock' and comp_choice == 'rock':
    print('TIE')
elif human_choice == 'scissors' and comp_choice == 'paper':
    print('computer wins')
elif human_choice == 'scissors' and comp_choice == 'scissors':
    print('computer wins')
elif human_choice == 'scissors' and comp_choice == 'rock':
    print('computer wins')