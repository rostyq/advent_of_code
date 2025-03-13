from functools import reduce
from sys import stdin, argv


def solve_part1(groups):
    answers = [len(set(group.replace("\n", ""))) for group in groups]
    return sum(answers)


def solve_part2(groups):
    def agg(intersect, answers):
        return answers if intersect is None else intersect & answers

    intersect_answers = [
        reduce(agg, map(set, group.split("\n")))
        for group in groups
    ]

    return reduce(lambda count, ans: count + len(ans), intersect_answers, 0)


groups = stdin.read().strip().split("\n\n")

part = "2" if len(argv) > 1 and argv[1] == "2" else "1"
if part == "1":
    print(solve_part1(groups))
else:
    print(solve_part2(groups))
