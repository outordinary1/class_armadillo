import requests 

response = requests.get('http://www.gutenberg.org/cache/epub/5200/pg5200.txt') #The Metamorphosis
text = response.text

for char in text:
    if char in '[]()@$%*-.?!,\'/:1234567890': #replace punctuation with blank space
        text=text.replace(char,' ')
text = text.lower() #makes all characters lower case

lines = text.split('\n')  #divides text into individual lines
lines[26:2003]  #defines particular lines to include(removes beginning and end fluff)

word_list = text.split()  #returns list of words
# print(word_list) #prints word list


word_count = {}  #creates dictionary for word count
for word in word_list:  #iterates over over word
    if word not in word_count: #if word only found once, count 1
        word_count[word] = 1
    else:    #if word found multiple times, adds to total count
        word_count[word] += 1

words = list(word_count.items())  # converts list with counts to tuples 
# print(words)          

words.sort(key=lambda tup: tup[1], reverse=True)  #sorts tuples numerically, largest first
for i in range(min(10, len(words))):  #produces top 10 most frequently used words 
    print(words[i])  #prints top 10 words
