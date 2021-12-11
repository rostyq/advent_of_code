import re

def parse_line(s: str) -> tuple:
    p0, p1 = (tuple(int(i) for i in p.split(','))
                          for p in re.findall("\d+,\d+", s))

    cmd = re.match("\D+", s).group(0).strip()
    return cmd, (p0, p1)


with open("input.txt", "r") as f:
    instructions = [parse_line(line) for line in f.readlines()]

size = 1000
grid = [[0 for _ in range(0, size)] for _ in range(0, size)]

for cmd, ((x0, y0), (x1, y1)) in instructions:
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            if cmd == "toggle":
                grid[y][x] += 2
            elif cmd == "turn on":
                grid[y][x] += 1
            elif cmd == "turn off":
                grid[y][x] = max(0, grid[y][x] - 1)

print(sum([value for line in grid for value in line]))
