# Matt helped me with this
#referred to demo_json.py in Matt's demo folder
# https://github.com/PdxCodeGuild/class_armadillo/blob/master/1%20Python/docs/08%20-%20Dictionaries.md
# https://github.com/PdxCodeGuild/class_armadillo/blob/master/0%20General/09%20-%20JSON,%20CSV,%20&%20XML.md#json
import json 
# path = r'C:\Users\flux\programs\class_armadillo\Code\Matthew\contacts.json'
# path = 'contacts.json'
# with open(path, 'r') as file:
#   text = file.read()
# print(text)

def load_contacts(path):
    with open(path, 'r') as file: # open the file
        text = file.read() # read the text out of the file
    contacts = json.loads(text) # convert the text containing json into a dictionary
    contacts = contacts['contacts'] # extract the list inside the dictionary
    return contacts

def save_contacts(path, contacts):
    contacts = {'contacts': contacts} # put the list of contacts in to a dictionary
    with open(path, 'w') as file: # open the file
        text = json.dumps(contacts, indent=4, sort_keys=True) # convert our list of dictionaries into json
        file.write(text) # write the json to the file

def retrieve_contacts(contacts):
    #contacts = {'contacts': contacts}
    for i in range(0, len(contacts)): #start at 0
        #if [i] == [j]:
        print(i, contacts[i]) # printing individual dictionary
        print(contacts[i]['name']) # using key to get the value of the dictionary
        print(contacts[i]['age'])
        print(contacts[i]['email'])
        print(contacts[i]['favorite color'])
# not returning anything - that's why it returns 'None'

# loading the contacts from the file
path = 'contacts.json'
contacts = load_contacts(path)

# print(contacts)
# print(type(contacts))

# print(contacts[0]['name'])
# print(contacts['contacts'][0]['name'])


while True:
  command = input('what is your command? ')
  if command in ['done', 'exit', 'quit']:
    break
  elif command == 'create':
    name = input("What is the contact's name? : ")
    age = int(input("What is the age? : "))
    email = input("What is the email? : ")
    favorite_color = input("What is the favorite color? : ")
    contact = {
        'name' : name,
        'age' : age,
        'email' : email,
        'favorite color' : color,
    }
    contacts.append(contact)
  elif command == 'retrieve':
    (retrieve_contacts(contacts)) # not returning anything
  elif command == 'update':
        ...
  elif command == 'delete':
        ...
  elif command == 'list':
    for contact in contacts:
      print(contact['name'])
      print('  Age:', contact['age'])
      print('  Email:', contact['email'])
      print('  Favorite Color: ', contact['favorite color'])
  else:
    print('command not recognized')


# saving our contacts to the file
save_contacts(path, contacts)