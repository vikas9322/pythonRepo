
# Using functions

def addingTwoNumber(a,b):
    return a+b

print(addingTwoNumber(9,10))


#Add Two Numbers with User Input

number1 = input("please enter your first number")

number2 = input("\nplease enter your second number")

sum = float(number1) + float(number2)

print("the sum fo {0} and {1} is {2} :" .format(number1,number2,sum))


# Add Two Numbers Using operator.add() Method

num1 = 29 
num2 = 20

import operator

su = operator.add(num1,num2)

print("sum of ther {0} and {1} is {2}" .format(num1,num2,su))


#Add Two Number Using Lambda Function
add_number = lambda x,y:x+y

num1 = 1
num2 = 20

result = add_number(num1,num2)

print("teh sum of", num1 , "and" , num2 , "is",result )

#Add Two Numbers Using Recursive Function
def add_number_recursive(x,y):
    if y == 0:
        return x
    else:
        return  add_number_recursive(x + 1 , y - 1)

num1 = 5
num2 = 2

result = add_number_recursive(num1,num2)

print("teh sum of", num1 , "and" , num2 , "is",result )
