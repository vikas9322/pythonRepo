n = int(input("please enter the number :"))


def prime_number(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime=False
    if is_prime:
        print("It is a prime number")
    else:
        print("it is not a prime number")

prime_number(number=n)