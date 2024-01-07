height = int(input())


if(height> 120):
    age =  int(input())
    if(age < 12 ):
        bill = 5
        print("yout ticket value is 5 rupee")            
    if(age >= 12 or age <= 18):
        bill = 7
        print("your ticket price is 7 rupee")
    if(age>18):
        bill=12
        print("your ticket price is 12 rupee")
    
    wantPhoto = input("do you want to take a phtoto")
    if(wantPhoto=="Y"):
        bill += 3

else:
    print("you need to grow")
