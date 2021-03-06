def add(x, y): # functions for each operation which can be call if loop below
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# user_op = input('\nWhich operation (+, -, * or /)? ').lower()
# num1 = float(input('What is the first number? ')) # converts input from sting to a decimal number for math
# num2 = float(input('What is the second number? '))

while True: 
    user_op = input('\nWhich operation (+, -, * or /) or done? ').lower()
    if user_op in ['done', 'stop', 'exit']: # opportunity to quit calculator, no input validation
        print ('Goodbye!')
        break
    num1 = float(input('What is the first number? ')) # converts input from sting to a decimal number for math
    num2 = float(input('What is the second number? '))
    if user_op == '+':
        print(num1, '+', num2, '=', add(num1, num2)) # 5 + 3 = 8
    elif user_op == '-':
        print(num1, '-', num2, '=', subtract(num1, num2))
    elif user_op == '*':
        print(num1, '*', num2, '=', multiply(num1, num2))
    elif user_op == '/':
        print(num1, '/', num2, '=', divide(num1, num2))
       
 



'''
Lab 13: Simple Calculator

Version 1
Let's write a simple REPL (read evaluate print loop) calculator that can handle addition, subtraction, 
multiplication, and division. Ask the user for an operator and each operand. 
Don't forget that input returns a string, which you can convert to a float using float(user_input)
where user_input is the string you got from input. Below is some sample input/output.

> what is the operation you'd like to perform? +
> what is the first number? 5
> what is the second number? 12
> 5 + 12 = 17
> what is the operation you'd like to perform? done
> goodbye!

Version 2
Allow the user to enter a running menu

> what is the starting number? 34
> enter operation: + 10
> 44
> enter operation: * 3
> 132

Version 3 (optional)
Allow the user to write an expression, alternating numbers and operators. Evaluate the expression left-to-right.

> what is the expression? 5 + 6 * 2
> 22

Version 4 (optional)
Allow the user to write an expression, alternating numbers and operators. Follow the proper order of operations, evaluating first exponentiation, then multiplication and division, then addition and subtraction.

> what is the expression? 5 + 6 * 2
> 17

Version 5 (optional)
Allow the user to write an expression including parantheses.

> what is the expression? 5*(6 + 2)
> 40
'''