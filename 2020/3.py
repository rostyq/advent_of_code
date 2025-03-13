from enum import Enum
from sys import stdin, argv


class Tile(Enum):
    OPEN = 0
    TREE = 1

    @classmethod
    def from_str(cls, s):
        if s == '.':
            return cls.OPEN
        elif s == '#':
            return cls.TREE
        else:
            raise TypeError(f"cannot create tile from {s}")


def parse_map(lines):
    forest = []
    for line in lines:
        forest.append([Tile.from_str(char) for char in line.strip()])
    return forest


def create_steps(dx, dy):
    x = 0
    y = 0
    while True:
        x += dx
        y += dy
        yield x, y


def count_trees(forest, steps):
    tree_count = 0
    for x, y in steps:
        if y >= len(forest):
            break
        line = forest[y]
        tile = line[x % len(line)]

        if tile is Tile.TREE:
            tree_count += 1
    return tree_count


def solve_part1(forest):
    return count_trees(forest, create_steps(3, 1))


def solve_part2(forest):
    answer = count_trees(forest, create_steps(3, 1))
    additional_slopes = [
        (1, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    for dx, dy in additional_slopes:
        answer *= count_trees(forest, create_steps(dx, dy))

    return answer


forest = parse_map([line for line in filter(None, map(str.strip, stdin))])

part = "2" if len(argv) > 1 and argv[1] == "2" else "1"
if part == "1":
    print(solve_part1(forest))
else:
    print(solve_part2(forest))
