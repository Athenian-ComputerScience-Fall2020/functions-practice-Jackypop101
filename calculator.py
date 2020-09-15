'''
Collaborators: 

'''
def add():
    print(num1 + num2)

def subtract():
    print(num1 - num2)

def multiply():
    print(num1 * num2)

def divide():
    print(num1 / num2)

option = int(input("Input 1 for addition, input 2 for subtraction, input 3 for multiplication, input 4 for division."))
num1 = int(input("Input first number"))
num2 = int(input("Input second number"))

if option == (1):
    add()
        
elif option == (2):
    subtract()

elif option == (3):
    multiply()
       
elif option == (4):
    divide()
       


