def is_prime(number):
    if number in (0, 1):
        return False
    elif number in (2, 3):
        return True
    divisors = set()
    for i in range(4, round(int(number ** 0.5)) + 1):
        if number % i == 0:
            divisors.add(i)
            divisors.add(number / i)
    divisors = [round(number) for number in divisors]
    return len(divisors) == 2


result = is_prime(3)
print(result)
