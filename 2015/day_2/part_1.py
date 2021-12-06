with open("input.txt", "r") as f:
    input_raw = f.readlines()

elves_list = [[int(i) for i in line.strip("\n").split("x")]
              for line in input_raw]

result = 0

for dimensions in elves_list:
    l, w, h = dimensions
    s1, s2, s3 = l * w, w * h, h * l

    result += 2 * s1 + 2 * s2 + 2 * s3
    result += min(s1, s2, s3)

print(result)
