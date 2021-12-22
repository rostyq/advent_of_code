from json import dumps


with open("input.txt", "r") as f:
    strings = [line.strip() for line in f.readlines()]


encoded = 0
literals = 0

for s in strings:
    literals += len(s)
    encoded += len(dumps(s))

print(encoded - literals)
