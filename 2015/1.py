from sys import argv


fn = lambda x: x == -1 if len(argv) > 1 and argv[1] == "2" else lambda x: False
result = 0

for i, char in enumerate(input(), start=1):
    match char:
        case "(":
            result += 1
        case ")":
            result -= 1
        case _:
            continue

    if fn(result):
        print(i)
        break
else:
    print(result)
