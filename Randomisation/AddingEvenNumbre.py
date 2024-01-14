target = int(input())

sum = 0
for number in range (2,target +1,2):
    if (target % 2 == 0):
        sum += target

print(sum)