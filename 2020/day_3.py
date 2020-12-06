from enum import Enum


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


def parse_map(fp):
    forest = []
    for line in fp.readlines():
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


def main():
    from pathlib import Path

    input_path = Path(__file__).parent / "forest_map.txt"

    with input_path.open('r') as fp:
        forest = parse_map(fp)

    # part 1
    answer = count_trees(forest, create_steps(3, 1))
    print(answer)

    # part 2
    additional_slopes = [
        (1, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    for dx, dy in additional_slopes:
        answer *= count_trees(forest, create_steps(dx, dy))

    print(answer)


if __name__ == "__main__":
    main()
