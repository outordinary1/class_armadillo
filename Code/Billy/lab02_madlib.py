print('\nWELCOME TO MADLIBS...where your words complete the story! \n')


holiday = input('What is your favorite holiday? ')
noun = input('In which room/building are you currently? ')
thing = input('''Look up! What's the first object you see? ''')
body_part1 = input('What is your favorite body part? ')
verb1 = input('What do you do like to do when happy (verb)? ')
verb2 = input('''What do you do whenever you're sad (verb)? ''')
body_part2 = input('What is your LEAST favorite body part? ')

cont = input('Would you like to see your story? ')

if cont == 'yes':
    print('-'*80)
    print(f'''\nIt's close to {holiday} and something evil's lurkin' in the {noun}. 
Under the {thing}, you see a sight that almost stops your {body_part1}.
You try to {verb1} but terror takes the sound before you make it.
You start to {verb2} as horror looks you right between the {body_part2}.
You're paralyzed!\n''')
    print('-'*80)
elif cont != 'yes':
     print('GOOD BYE...have a nice day!')
        
    

    # cont_2 = ' '
    # while cont_2 != 'no':
    #     cont_2 = input('Would you like to try again with different words? ')
    #     if cont_2 != 'yes':
    #         break
    #     print('*'*80)
    #     print(f'''It's close to {holiday} and something evil's lurkin' in the {noun}. 
    #     Under the {thing} you see a sight that almost stops your {body_part1}.
    #     You try to {verb1} but terror takes the sound before you make it.
    #     You start to {verb2} as horror looks you right between the {body_part2},
    #     You're paralyzed!''')
    #     print('*'*80)




# emoticon_gen = " "
# while emoticon_gen != "no":
#     emoticon_gen = input("Would you like to generate more random emoticons? ")
#     if emoticon_gen != "yes":
#        break  
#     for x in range(5):
#         random_eyes = random.choice(eyes) 
#         random_nose = random.choice(nose)
#         random_mouth = random.choice(mouth)
#         print(random_eyes + random_nose + random_mouth)