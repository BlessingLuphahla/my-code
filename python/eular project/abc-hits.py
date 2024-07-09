import itertools
import math


def is_prime(number):
    divisors = set()
    for i in range(1, round(int(number ** 0.5)) + 1):
        if number % i == 0:
            divisors.add(i)
            divisors.add(number / i)
    divisors = [round(number) for number in divisors]

    return len(divisors) == 2


def prime_factors(number):
    primes = []
    for divisor in range(1, number + 1):
        if is_prime(divisor):
            if number % divisor == 0:
                primes.append(divisor)

    return primes


def radical(number):
    product = 1
    for value in prime_factors(number):
        product *= value
    return product


def is_abc_hit(a, b, c):
    if math.gcd(a, b) == math.gcd(a, c) == math.gcd(c, b) == 1:
        if a < b:
            if a + b == c:
                if radical(a * b * c) < c:
                    return True
        return False


def sum_it_up():
    total = 0
    percentage_keeper = 0
    for a, b, c in itertools.product(list(range(0, 1000)), list(range(0, 1000)), list(range(0, 1000))):
        percentage_keeper += 1
        if is_abc_hit(a, b, c):
            total += c
        if percentage_keeper % 50_000 == 0:
            print('percentage: ', float('{0:.6f}'.format(percentage_keeper / (1000 ** 3) * 100)), ' %')
    return 'total: ' + str(total)


result = sum_it_up()
print(result)
