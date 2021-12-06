with open("input.txt", "r") as f:
    input_raw = f.read()

result = 0

for char in input_raw:
    if char == "(":
        result += 1
    elif char == ")":
        result -= 1

print(result)
