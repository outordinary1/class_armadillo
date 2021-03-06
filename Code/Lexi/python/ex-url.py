import requests
import json

# Prompt the user for a keyword, list 
def get_categories():
  keyword = input("Enter a keyword to search for quotes : ")
  # make formatted string to use line 6 for quote category
  url = f'https://favqs.com/api/quotes?page=1&filter={keyword}'
  return url

# must comment out two lines below in order to make it work,
# WHY? b/c access token is needed
# response = requests.get(url)
# print(response.text)

def get_fact(category=None):

  headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
  response = requests.get(url, headers=headers)
  print(response.text)

  #converting JSON into a dictionary
  dictionary = json.loads(response.text)
  print(dictionary)
  return data['vaue']



#RESULT
# Enter a keyword to search for quotes : {"page":1,"last_page":false,"quotes":[{"id":0,"favorites_count":0,"favorite":false,"dialogue":false,"body":"No quotes found","tags":[]}]}
# {'page': 1, 'last_page': False, 'quotes': [{'id': 0, 'favorites_count': 0, 'favorite': False, 'dialogue': False, 'body': 'No quotes found', 'tags': []}]}

# must change 'false' to 'False' in the below dictionary - b/c Python cannot
# read all lowercase boolean values (JSON can)
data = {"page":1,"last_page":False,"quotes":[{"id":0,"favorites_count":0,"favorite":False,"dialogue":False,"body":"No quotes found","tags":[]}]}
# accessing the dictionary
if data['quotes'][0]['body'] == "No quotes found":
  print("No quote found")
else:
  print("else statement")

# print(contacts['contacts'][0]['name']) # Joe
# print(json.loads(contacts, indent=4, sort_keys=True))
while True:
  # ask user to select category
  category = input('Which category? : ')


  # iterate through all the categories
  for i in range(len(category)):
    print(f' {i}{category[i]}')


# the quotes you get in response, and 
# print(keyword)
# # prompt the user to either show the 
# if-else
# # next page or enter a new keyword. 
# # You can use string concatenation to build the URL.
# what?
