from sys import argv
from collections import Counter


def step(char: str) -> tuple[int, int]:
    match char:
        case ">":
            return 1, 0
        case "<":
            return -1, 0
        case "^":
            return 0, 1
        case "v":
            return 0, -1
        case _:
            return 0, 0


sx: int = 0
sy: int = 0

if len(argv) > 1 and argv[1] == "2":
    rx: int = 0
    ry: int = 0

    def fn(i: int, dx: int, dy: int):
        global sx, sy, rx, ry
        if i % 2 == 0:
            sx += dx
            sy += dy
            return sx, sy
        else:
            rx += dx
            ry += dy
            return rx, ry

else:

    def fn(i: int, dx: int, dy: int):
        global sx, sy
        sx += dx
        sy += dy
        return sx, sy


houses = Counter({(0, 0): 1})

for i, char in enumerate(input()):
    dx, dy = step(char)
    houses[fn(i, dx, dy)] += 1


print(len(houses.keys()))
