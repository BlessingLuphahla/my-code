def calculate_r(a, n):
    return ((a - 1) ** n + (a + 1) ** n) % a ** 2


def find_r_max(value_of_a):
    max_r = 0

    for n in range(1, 5000):
        r = calculate_r(value_of_a, n)
        if r > max_r:
            max_r = r

    return max_r


def summation_of_r_max():
    total_sum = 0
    for a in range(3, 1000 + 1):
        total_sum += find_r_max(a)
    return total_sum


print(summation_of_r_max())
