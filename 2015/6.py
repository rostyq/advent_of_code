from typing import Literal
from sys import argv, stdin
from re import match, findall


Pt = tuple[int, int]
Cmd = Literal["toggle", "turn on", "turn off"]


def parse_point(s: str) -> Pt:
    return tuple(map(int, s.split(",", 1)))


def parse_instruction(s: str) -> tuple[Cmd, Pt, Pt]:
    p0, p1 = (parse_point(p) for p in findall(r"\d+,\d+", s))
    cmd = match(r"\D+", s).group(0).strip()
    return cmd, p0, p1


size = 1000
grid = [[0 for _ in range(0, size)] for _ in range(0, size)]

if len(argv) > 1 and argv[1] == "2":

    def fn(cmd: Cmd, x: int, y: int):
        match cmd:
            case "toggle":
                grid[y][x] += 2
            case "turn on":
                grid[y][x] += 1
            case "turn off":
                grid[y][x] = max(0, grid[y][x] - 1)

else:

    def fn(cmd: Cmd, x: int, y: int):
        match cmd:
            case "toggle":
                grid[y][x] = int(not grid[y][x])
            case "turn on":
                grid[y][x] = 1
            case "turn off":
                grid[y][x] = 0


for cmd, (x0, y0), (x1, y1) in map(
    parse_instruction, filter(None, map(str.strip, stdin))
):
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            fn(cmd, x, y)


print(sum([value for line in grid for value in line]))
