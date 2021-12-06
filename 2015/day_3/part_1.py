from collections import Counter


with open("input.txt", "r") as f:
    input_raw = f.read()

x: int = 0
y: int = 0

houses = Counter({(0, 0): 1})

for char in input_raw:
    if char == ">":
        x += 1
    elif char == "<":
        x -= 1
    elif char == "^":
        y += 1
    elif char == "v":
        y -= 1
    else:
        continue

    houses[(x, y)] += 1

result = len(houses.keys())

print(result)
