from ast import literal_eval


with open("input.txt", "r") as f:
    strings = [line.strip() for line in f.readlines()]


literals = 0
chars = 0

for s in strings:
    literals += len(s)
    chars += len(literal_eval(s))

print(literals - chars)
