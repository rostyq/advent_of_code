with open("input.txt", "r") as f:
    input_raw = f.read()

result = 0

for i, char in enumerate(input_raw, start=1):
    if char == "(":
        result += 1
    elif char == ")":
        result -= 1

    if result == -1:
        print(i)
        break

