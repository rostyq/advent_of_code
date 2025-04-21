from sys import stdin, argv


Grid = dict[tuple[int, int], bool]


def neighbours(grid: Grid, *, row: int, col: int) -> int:
    return sum(
        grid.get((y, x), False)
        for x in (col - 1, col, col + 1)
        for y in (row - 1, row, row + 1)
        if not (row == y and col == x)
    )


grid: Grid = {
    (row, col): True if char == "#" else False
    for row, line in enumerate(stdin)
    for col, char in enumerate(line.strip())
    if char in "#."
}

stuck: list[tuple[int, int]] = []
if len(argv) > 1 and argv[1] == "2":
    bottom = max(y for y, _ in grid)
    right = max(x for _, x in grid)
    left = min(x for _, x in grid)
    top = min(y for y, _ in grid)
    stuck = [(top, left), (top, right), (bottom, left), (bottom, right)]

for (row, col) in stuck:
    grid[(row, col)] = True

steps = 100
for step in range(steps):
    temp = grid.copy()
    for (row, col), state in grid.items():
        count = neighbours(grid, row=row, col=col)
        if (row, col) in stuck:
            temp[(row, col)] = True
        elif state and count not in (2, 3):
            temp[(row, col)] = False
        elif not state and count == 3:
            temp[(row, col)] = True
    
    grid = temp


print(sum(grid.values()))
