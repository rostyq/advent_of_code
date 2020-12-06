def parse_numbers(fp):
    numbers = []
    for line in fp.readlines():
        numbers.append(int(line.strip()))
    return numbers


def solve_1(numbers):
    for n1 in numbers:
        for n2 in numbers:
            if (n1 + n2) == 2020:
                return n1 * n2


def solve_2(numbers):
    for n1 in numbers:
        for n2 in numbers:
            for n3 in numbers:
                if (n1 + n2 + n3) == 2020:
                    return n1 * n2 * n3


def main():
    from pathlib import Path

    input_path = Path(__file__).parent / "expense_report.txt"

    with input_path.open('r') as fp:
        numbers = parse_numbers(fp)

    print(solve_1(numbers))
    print(solve_2(numbers))


if __name__ == "__main__":
    main()
