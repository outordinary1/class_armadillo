import random  # contain function and choices to randomaze 
import string  # contain function and choices to randomaze 

# to run flask I need to enter the following in the terminal each time:  python3 -m flask run
# I may need to = export FLASK_ENV=development
# this will tell me which servers are running = ps -fA | grep python
# to change the port= export FLASK_RUN_PORT=5500
# I have the following error when trying to control z in the terminal = OSError: [Errno 48] Address already in use


from flask import Flask, render_template, request # I need to enter after the coma render_template to be able 
#connect index html to the browser
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'] ) # localhost:5000/
def index():
    return render_template('index.html') #  The index page will hav the link to go inside the ROT13 and Unit Converter 

@app.route('/rot13', methods=['GET', 'POST'] ) # localhost:5000/
def rotc13():
        # Lab 15: ROT Cipher Version 2
    #Allow the user to input the amount of rotation used in the encryption. (ROTN)
    word = ''
   
    if request.method == 'POST':
        user_input = request.form['user_input']
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        index =    ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']
        rot13 =    ['n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m']
        rotation = int(request.form['rotation'])
        print(request.form)
        print(user_input,rotation)
    
        # user_input = 'hello' #input('Enter any word: ')
        
        # print(alphabet.index('c'))
        # print(rot13[4])
        for letter in user_input: 
            x = (alphabet.index(letter) + rotation) % 26 #
            # print(alphabet[x])
            print(x)  
            word += alphabet[x]
            # print(index_letter)
            # print(rot13[index_letter])
        print(word)
    return render_template('rot13.html', word = word) # this is setting my key word argument
    

@app.route('/unit_converter', methods=['GET', 'POST'] ) # localhost:5000/
def units():
    result = '' # initialzing the variable to be able fix this error: UnboundLocalError: local variable 'result' referenced before assignment
    #return"Hello World"
    if request.method == 'POST':
        c_unit = request.form['c_unit']
        b_unit  = request.form['b_unit']
        num = int(request.form['num'])
        units = {
            'ft': .3048,
            'm': 1,
            'mi': 1609.34,
            'km': 1000,
            'yd':  0.9144,
            'in': 0.0254,

        }


        # num = int(input("Please enter a number to convert: "))
        # c_unit = input("Would you please enter the unit to convert from: ")
        # b_unit = input("Please enter the unit to convert to")

        product = num * units[c_unit]
        product2 = product / units[b_unit]
        result = f'{num} {c_unit} is equal to {product2} {b_unit}'
        print(result)
    return render_template('unit_converter.html', result = result) # this is setting my key word argument    

#Add Random Password Generator and get a logo:
@app.route('/random_password_generator/',methods=['GET', 'POST'])
def random_pw():
    word = ''
    # print('random thing')
    # return "hey"
    if request.method == 'POST':
        lower = string.ascii_lowercase  # the .dot will go inside the string module
        upper = string.ascii_uppercase  # the .dot will go inside the string module
        letters_input = request.form['letters_input']
        digits_input  = request.form['digits_input']
        punctuation_input = int(request.form['punctuation_input'])

        letters = string.ascii_letters
        digits = string.digits
        punctuations = string.punctuation
        # letters_input = int(input('How many letters do you want: '))
        # digits_input = int(input('How many digits do you want: '))
        # punctuation_input = int(input('How many Punctuation do you want: '))
        word = []

        for i in range(int(letters_input)):
            word.append(random.choice(letters))
        for i in range(int(digits_input)):
            word.append(random.choice(digits))
        for i in range(int(punctuation_input)):
            word.append(random.choice(punctuations))

        #word.shuffle() st
        random.shuffle(word)
        print(''.join(word))
        word = ''.join(word) # this is like striping brackets from the list. Changing from a list to a single string from list [p57UT-Rc6/] to string p57UT-Rc6/ 
    return render_template('random_password_generator.html', word = word) # this is setting my key word argument




