import sys
from itertools import product
from math import gcd

THE_RANGE = list(range(1, 1000000000 + 1))
the_n_d_cartesian_product = product(THE_RANGE, THE_RANGE)


def conditions(n, d):
    if gcd(n, d) == 1:
        if n < d:
            return True
    return False


def proper_reduced_fractions():
    set_of_fractions = set()
    for n, d in the_n_d_cartesian_product:
        if conditions(n, d):
            fraction = n / d
            set_of_fractions.add(fraction)

    return len(set_of_fractions)


def main():
    try:
        print(proper_reduced_fractions())
    except KeyboardInterrupt:
        print('you chose to exit')
        sys.exit(0)


if __name__ == '__main__':
    main()
