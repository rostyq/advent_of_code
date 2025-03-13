from sys import argv

def look_and_say(digits: str) -> str:
    length = len(digits)
    current = 0
    result = ""

    while current < length:
        digit = digits[current]

        count = 1
        offset = current + 1
        while offset < length:
            if digit == digits[offset]:
                count += 1
                offset += 1
            else:
                break

        result += f"{count}{digit}"

        current = offset

    return result

steps = int(argv[1]) if len(argv) > 1 else 40
result = input()

for _ in range(steps):
    result = look_and_say(result)

print(len(result))
