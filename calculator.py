'''
Collaborators: 
Megan
'''
def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2

option = int(input("Input 1 for addition, input 2 for subtraction, input 3 for multiplication, input 4 for division."))
num1 = int(input("Input first number"))
num2 = int(input("Input second number"))

if option == (1):
    print(add(num1,num2))
        
elif option == (2):
    print(subtract(num1,num2))

elif option == (3):
    print(multiply(num1,num2))
       
elif option == (4):
    print(divide(num1,num2))
       


