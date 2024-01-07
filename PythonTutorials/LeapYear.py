year = int(input())

if(year % 4 == 0):
    if(year % 100 == 0):
        if(year%400 == 0):
            print(f"this year {year} is a leap year")
        else:
            print(f"this year {year} is not a leap year")
    else:
        print(f"this year {year} is a leap year ")
else:
    print(f"this year {year} is not a leap year")

####################################################################################
    


