
#booleans
'''
"hello" #string literal
5 #int literal
False #bool literal



is hungry = True #has to be capitilized
has_food = True
is_eating = os_hungry and has_food

print(is_eating)

is_tired = True
is_night = False
is_sleeping = is_tire or is_night
print(is_sleeping)


temperature = 60
if temperature < 50:
    print('cold')
is_cold = temperature < 50
    print('cold')
#these are the same

name = 'mike'
is_matthew = name == 'matthew'
#this will print to false

has_name = 'matthew' in 'hello my name is matthew'
print(has_name)
#this would be true
has_name = 'matthewewe' in 'hello my name is matthew'
#this would be false

if 'apples' in ['apples', 'bananas', 'pears']
    print('has apples')
#can be used to check in an element is in a list
#or if a string is in a string


if
if-else condition
if-elif 
if-elif-else
if-elif-elif-elif-else


temperature = 45
if temperature <60:
    print('cold')
elif temperature >-60 and temperature < 70:
        print('warm')
    #the elif is unnecessary

if temperature < 60:
    print('cold')
elif temperature < 70:
    print('warm')


def min (a, b):
    return a if a <b else b

    or
    if a < b:
        return a
    return b
        #return a if a < b else b

print(min(5, 2)) #2
#you want your code to be succinct
not verbose
not too much on one line
more lines than less lines
but not too many lines

grade = 87
print(grade // 10) #tens digit
print(grade % 10) #ones digit


exit()

pip install colorama


sdffrom colorama import fore

import time #time module
#time.sleep will pause the loop
print(Fore.GREEN + 'look its green')

#loops
message = 'hello welcome to my program'
i=0
while i < len(message)
    print(message[i], end='')
    time.sleep(0.2)
    i +=1
     #1 number - upper bound
    #0 to 99 (100 times)
    for in range(100)
    print(i)

    #for 2 numbers - lower bound and upper bound
    #1 to 100 (100 times)
    for in in range ( 1, 101):
        print(i)

#3 numbers lower bound, upper bound, and increment
#1 to 100 ever 2 numbers (50 times)
for in in range(1, 101, 2):
    print(i)
        
 fruits = ['apples', 'bananas', 'pears', ]
 for fruit in fruits:
      print(fruit)

                #very different
                in 'apples' in fruits:
                    pass
for char in 'hello world':
    print(char)
    #prints each character on a separate line

fruits = ['apples', 'bananas', 'pear']
print(fruits[0]) #apples
    print(fruits)[i]
    fruits[i] += '!'
'''
import random
import string

alphabet = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
print(alphabet)

for i in range(10):
    print(random.choice(alphabet))

    

