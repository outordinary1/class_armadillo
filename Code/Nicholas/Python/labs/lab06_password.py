#this lab generates a random password, the length is based on user input

import string
import random
import time

more_pw = True  #while loop so user can generate another password
while more_pw:
    password_char = string.ascii_lowercase + string.ascii_uppercase+string.punctuation + string.digits  #password will only contain characters from these string constants
    print('Welcome to the random password generator!')
    time.sleep(1)  #pauses for 2 seconds after welcome message before asking for pw length
    password_length = int(input('How many characters would you like your password to be? '))  #user inputs password length
    random_password = ""

    for x in range(password_length):  #for loop to print password based on user input
        random_password += random.choice(password_char)  #adds random characters to create random password
    print(random_password)
    
    pw = input("Generate another password? Type 'no' to finish ").lower()  #breaks if user selects no, otherwise loops back to input
    if pw == 'no':
        print('later!')
        break