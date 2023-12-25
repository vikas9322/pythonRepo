height = input()
weight = input()

weight_as_int = int(weight)
height_as_int = float(height)

bmi = weight_as_int / height_as_int ** 2
bmi_as_int = int(bmi)

print(bmi_as_int)

print(round(2/3))
 # or 
print(round(2//3))

score =0
height = 1.8
isWining = true 

# fstring 

print(f"your score is {score} , your height is {height} , and your winning is {isWining}")