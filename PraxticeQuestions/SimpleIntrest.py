def simpleIntrest(p,t,r):
    print("The principa; is ", p)
    print("The time period is ", t)
    print("The rate of intrets os ",r)

    si = (p*t*r)/100

    print("The simple intrest is ", si)
    return si 


simpleIntrest(8,6,9)


print("########################################################################")
# Program for simple interest with Taking input from user

def simpleIntrest(a,b,c):
    print("The principa; is ", a)
    print("The time period is ", b)
    print("The rate of intrets os ",c)

    si = (a*b*c)/100

    print("The simple intrest is ", si)
    return si 

a = int(input("Please enter the principal amount:"))
b = int(input("Enter the time period :"))
c = int(input("Enter the reate of interest:"))

simpleIntrest(a,b,c)