# Lab 20 The URL to get a random quote is https://favqs.com/api/qotd, send a request here, parse the JSON in the response into a python dictionary, and show the quote and the author.

# 1:15 mark of Week 5 > May 4th https://zoom.us/rec/play/tJN_Ie-hr203HdzGuASDUfUvW9S5Kv-shyMX8vYEzk_nB3JXYVOhYOAWY7ZqnZ74BFFAB8zTSaw49UG3?continueMode=true&_x_zm_rtaid=B_eY-b4sRDOhI4C9lZhUUQ.1590447779267.8865d7bf23014c3f1f90087953230acd&_x_zm_rhtaid=568
# sources: https://favqs.com/api/
# other cool ideas: https://www.programmableweb.com/category/keywords/api
import requests
import json 
import string

key = input("What keyword do you want to have a search for quotes by? :")

page=1
while True:
   
    url = f'https://favqs.com/api/quotes?page={page}1&filter={key}'
    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    print(data)
    # output = []
    # for quote in data['quotes']:

    #     output.append({
    #         'body': quote['body'],
    #         'author': quote['author']
    #     })
    #     print(output)


    if data['quotes'][0]['body'] == 'No quotes found':
        print("\nchoose a different keyword - that one yields no results\n")
        break

    for quote in data['quotes']:
        print(f" \nThe keyword: '{key}' yielded the following quote '{quote['body']}' -----{quote['author']} on page: {page}")
        
    
    next_page = input("Check the next page? (Y/n) : ")
    if next_page.lower() == 'n':
        break

    page+=1


# import requests
# import json

# # site we are using
# url = 'https://api.chucknorris.io/jokes/random'
# # send API request
# response = requests.get(url)
# # look at the text in raw JSON format
# print(response.text)
# # create a variable that represents a python dictionary
# # https://www.w3schools.com/python/python_json.asp
# joke = json.loads(response.text)

# print(f'The joke is : "{joke["value"]}".')

# RESULT:
# The joke is : "Chuck Norris can make you evacuate your bowels with a high five.".
