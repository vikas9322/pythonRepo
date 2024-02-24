def maximum(a,b):
    if a > b:
        return a
    else:
        return b
    
print(maximum(2,4))

# Find Maximum of two numbers Using max() function
a = 2
b = 5

maximum = max(a,b)

print(maximum)


# Maximum of two numbers Using Ternary Operator

a = 10
b = 1

print(a if a > b else b)

# Maximum of two numbers Using lambda function

a=2;b=4
maximum = lambda a,b:a if a>b else b 
print(f"{maximum(a,b)} is a maximum number")

# Maximum of two numbers Using list comprehension
a=2;b=5
x = [a if a>b else b]
print(x)


# Maximum of two numbers Using sort() method
a = 2
b =4
x = [a,b]
x.sort()
print(x[-1])