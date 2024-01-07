print("Love calculator is calculating your score")
name1 = input()
name2 = input()

combined_name = name1 + name2 
lower_case = combined_name.lower()

t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")

first_digit = t + r + u + e

l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")

second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if(score<10) or (score>90):
    print(f"your score is {score} you go togther like coke na d mentos")
elif(score>=40) and (score<=50):
    print(f"your score is {score},you are alright togther")
else:
    print(f"your socre is {score}")