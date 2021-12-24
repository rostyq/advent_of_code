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


def main():
    from sys import argv

    result = argv[1]
    steps = int(argv[2])

    for _ in range(steps):
        result = look_and_say(result)

    print(len(result))


if __name__ == '__main__':
    main()

