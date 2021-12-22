with open("input.txt", "r") as f:
    input_raw = f.readlines()

elves_list = [[int(i) for i in line.strip("\n").split("x")]
              for line in input_raw]

result = 0

for dimensions in elves_list:
    l, w, h = dimensions
    p1, p2, p3 = (2 * p for p in (l + w, w + h, h + l))

    result += min(p1, p2, p3)
    result += l * w * h

print(result)
