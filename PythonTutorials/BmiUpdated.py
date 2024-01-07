height = int(input())
weight = int(input())

bmi = weight / (height * height)

if(bmi < 18.5):
    print(f"your bmis is {bmi} your under weight" )
elif(bmi <25):
    print(f"your bmi is {bmi}, your weight is normal")
elif(bmi <10):
    print(f"your bmi is {bmi}, your weight is slightly under weight ")
elif(bmi <25):
    print(f"your bmi is {bmi}, your weight is  slghtly over wight")
else:
    print(f"your bmi is {bmi} your clinically obesse")