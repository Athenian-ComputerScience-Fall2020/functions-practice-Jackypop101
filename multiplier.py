'''
Adapt the code from one of the functions above to create a new function called 'multiplier'.
The user should be able to input two numbers that are stored in variables.
The function should multiply the two variables together and return the result to a variable in the main program.
The main program should output the variable containing the result returned from the function.
'''
def multiplier():
   num1 = x
   num2 = y
   return num1 * num2

x = int(input("Input a number:"))
y = int(input("Input a number:"))

output_num = multiplier()
print(output_num)