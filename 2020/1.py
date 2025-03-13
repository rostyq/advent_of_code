from typing import Iterable
from sys import stdin, argv


YEAR = 2020


def solve_1(numbers: Iterable[int]):
    for n1 in numbers:
        for n2 in numbers:
            if (n1 + n2) == YEAR:
                return n1 * n2


def solve_2(numbers: Iterable[int]):
    for n1 in numbers:
        for n2 in numbers:
            for n3 in numbers:
                if (n1 + n2 + n3) == YEAR:
                    return n1 * n2 * n3


numbers = map(int, filter(None, map(str.strip, stdin)))
solve = solve_2 if len(argv) > 1 and argv[1] == "2" else solve_1
print(solve(numbers))
