# This Python program uses a recursive function to calculate the factorial of a given number. 
# The factorial is computed by multiplying the number with the factorial of its preceding number.
# def factorial(n):
#     return 1 if (n==1 or n == 0 ) else n * factorial(n-1)

# num= 5
# print("factorial of ", num ,"is", factorial(num))


# Find the Factorial of a Number Using Iterative approach
# def factorial(n):
#     if n < 0:
#         return 0
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         fact = 1
#         while(n>1):
#             fact *= n
#             n-=1
#         return fact
    

# num= 5
# print("factorial of ", num ,"is", factorial(num))

# def factorial(n):
       
#     res = 1
      
#     for i in range(2, n+1):
#         res *= i
#     return res
#  # Driver Code
# num = 5
# print("Factorial of", num, "is",
# factorial(num))


# Find the Factorial of a Number Using One line Solution (Using Ternary operator): 
# def factorial(n):
#     return 1 if (n==1 or n==0) else n * factorial(n-1)
# num = 5 
# print("factorial of ", num , "is" , factorial(num))

# Find the Factorial of a Number Using using In-built function
# import math

# def factorial(n):
#     return (math.factorial(n))

# num = 5
# print(factorial(num))


# Prime Factorization Method to find Factorial
# Initialize the factorial variable to 1.
# For each number i from 2 to n, do the following:
# a. Find the prime factorization of i.
# b. For each prime factor p and its corresponding power k in the factorization of i, multiply the factorial variable by p raised to the power of k.
# Return the factorial variable.

def primeFactors(n):
    factors = {}
    i = 2
    while i * i <= n:
        while n % i == 0:
            if i not in factors:
                factors[i]==0
            factors[i] += 1
            n //= i
        i += 1
    if n > 1:
        if n not in factors:
            factors[n]==0
        factors[n] += 1
    return factors


def factorial(n):
    result = 1 
    for i in range(2,n+1):
        factors = primeFactors(i)
        for p in factors:
            result *= p ** factors[p]
    return result

num = 5
print("Factorial of",num,"is",factorial(num))