#emoticon lab
'''

    Define a list of eyes
    Define a list of noses
    Define a list of mouths
    Randomly pick a set of eyes
    Randomly pick a nose
    Randomly pick a mouth
    Assemble and display the emoticon
    make the emoticon display the emotion of the user
    generate horizontal or vertical
'''

import random

eyes = [':', ';', 'x', '8']
nose = ['-','.', 'v', '^', '*', '@']
mouth = ['3', '>', ')', '$', 'o']

emotion = input('Are you feeling happy, sad, angry or something else today? ')

if emotion == "happy":
    print(':-)))')
elif emotion == "sad":
    print(':-[[[')
elif emotion == "angry":
    print('>:{{{')
else:
    print(random.choice(eyes) + random.choice(nose) + random.choice(mouth))

    while True:
        user_input = input("Does that fit your emotion? ").lower()
        if user_input == "no":
            print(random.choice(eyes) + random.choice(nose) + random.choice(mouth))
        else:
            print('okie dokie, byeee')
            break


    '''
    for emoticon in range(5):
        face = random.choice(eyes) + random.choice(nose) + random.choice(mouth)
        print(face)
   


    face = random.choice(eyes) + random.choice(nose) + random.choice(mouth)
    print(face)

#lower convert to lowercase
#strip removes whitespace from beginning and end
response = input('would you like to continue?').lower().strip()
#response = True if response -- 'yes' else False
response = response == 'yes'
print(response)
'''