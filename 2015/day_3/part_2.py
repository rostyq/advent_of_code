from collections import Counter


with open("input.txt", "r") as f:
    input_raw = f.read()

s_x: int = 0
s_y: int = 0

r_x: int = 0
r_y: int = 0

houses = Counter({(0, 0): 2})

for i, char in enumerate(input_raw):
    dx, dy = 0, 0

    if char == ">":
        dx = 1
    elif char == "<":
        dx = -1
    elif char == "^":
        dy = 1
    elif char == "v":
        dy = -1
    else:
        continue

    if i % 2 == 0:
        s_x += dx
        s_y += dy
        x, y = s_x, s_y
    else:
        r_x += dx
        r_y += dy
        x, y = r_x, r_y

    houses[(x, y)] += 1

print(len(houses.keys()))
