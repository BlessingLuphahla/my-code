from itertools import product

THE_RANGE = list(range(95,100))
the_a_b_cartesian_product = product(THE_RANGE, THE_RANGE)

def googol_determination():
    max_value = 0
    for a,b in the_a_b_cartesian_product:
        googol = a**b
        possible_max = sum([int(number) for number in str(googol)])
        if possible_max > max_value:
            max_value = possible_max

    return max_value


print(googol_determination())