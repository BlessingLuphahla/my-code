from itertools import permutations
from typing import Set, List


def different_multiples(x: int) -> Set:
    return {x, 2 * x, 3 * x, 4 * x, 5 * x, 6 * x}


def different_permutations(x: int) -> Set:
    x = str(x)
    return set(int(''.join(value)) for value in permutations(x))


def final_destination(X: List):
    for x in X:
        if different_permutations(x).issuperset(different_multiples(x)):
            print(x)


final_destination([i for i in range(100_000, 999_999 + 1)])
