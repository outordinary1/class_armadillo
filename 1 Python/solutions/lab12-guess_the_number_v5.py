


import random

lower_bound = 0
upper_bound = 100

input(f'Pick a number between {lower_bound} and {upper_bound}, hit enter when ready....')

while True:
    x = random.randint(lower_bound, upper_bound)
    answer = input(f'Is it {x}? yes or no: ')
    if answer == 'yes':
        print('Hooray! Feed me information and electricity please')
        break










