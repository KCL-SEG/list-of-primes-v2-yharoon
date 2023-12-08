"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):

    if number_of_primes < 1:
        raise ValueError("Only positive integets allowed")

    primes = []

    count = 0
    vals = 2

    while (count < number_of_primes):
        if isPrime(vals):
            primes.append(vals)
            count += 1
        vals += 1

    return primes

def isPrime(value):
    flag = True
    for i in range(2,value):
        if (value % i) == 0:
            flag = False
            break
    return flag