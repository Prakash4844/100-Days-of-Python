# Write your code below this line 👇

def prime_checker(number):
    is_prime = True
    if number <= 1:
        print(
            'The Given number is not a prime.\n Explanation: \n primes are integers greater than one with '
            'no positive divisors besides one and itself. \n Negative numbers are excluded.')
    elif 2 == number or number == 3:
        print("The Given number is prime.")
    else:
        for i in range(2, number):
            if number * number % i == 0:
                is_prime = False
        if is_prime:
            print("It's a prime number")
        else:
            print("It's not a prime number")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))

prime_checker(number=n)
