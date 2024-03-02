# # Function to calculate x raised to 
# # the power y


# def power(x,y):
#     if y == 0:
#         return 1
#     if y % 2 ==0:
#         return power(x,y // 2) * power(x,y // 2)
#     return x * power(x,y // 2) * power(x,y // 2)

# def order(x):
#     n = 0
#     while( x != 0):
#         n = n +1
#         x = x // 10

#     return n

# def isArmstrong(x):
#     n = order(x)
#     temp = x
#     sum1 = 0

#     while(temp != 0):
#         r = temp % 10
#         sum1 = sum1 + power(r,n)
#         temp = temp // 10

#     return (sum1 == x)


# x = 1534
# print(isArmstrong(x))


# print("##################################################")

# #Armstrong number without using the power function

# n = int(input("Enter the number of your choice "))
# s = n
# b = len(str(n)) 
# sum1 = 0
 
# while n != 0:
#     r = n % 10
#     sum1 = sum1 + (r**b)
#     n = n//10
# if s == sum1:
#     print("The given number",s, " is armstrong number")
# else:
#     print("The given number ", s , "si not armstong number")


# Armstrong number without using the power function

n = 153
s = n
b = len(str(n))
sum1 = 0

while n != 0:
    r = n % 10
    sum1 = sum1 + (r**b)
    n = n // 10

if s == sum1:
    print("the give number is armstrong number", s)
else:
    print("the given number is not armstrong number",s)

