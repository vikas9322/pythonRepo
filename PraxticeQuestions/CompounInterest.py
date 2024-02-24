# A = P(1 + R/100) t 
# Compound Interest = A – P 
# Where, 
# A is amount 
# P is the principal amount 
# R is the rate and 
# T is the time span



def compound_interest(principal,rate,time):

    Amount = principal * (pow((1 + rate /100),time))
    CI = Amount - principal
    print("Compound Intest is ", CI)

compound_interest(10000,10.25,5)

print("################################################################################")

def compound_interest(principal, rate, time):
 
    # Calculates compound interest
    Amount = principal * (pow((1 + rate / 100), time))
    CI = Amount - principal
    print("Compound interest is", CI)
 
 
# Driver Code
#Taking input from user.
principal = int(input("Enter the principal amount: "))
rate = int(input("Enter rate of interest: "))
time = int(input("Enter time in years: " ))
#Function Call
compound_interest(principal,rate,time)

