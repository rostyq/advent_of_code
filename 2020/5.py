from sys import stdin, argv

def find_position(s: str) -> tuple:
    row = int(s[:7].replace('F', '0').replace('B', '1'), 2)
    col = int(s[7:].replace('L', '0').replace('R', '1'), 2)
    return row, col


def convert_to_id(row: int, col: int) -> int:
    return row * 8 + col


def parse_ids(lines):
    ids = []
    for line in lines:
        row, col = find_position(line.strip())
        ids.append(convert_to_id(row, col))
    return ids


def solve_part1(seat_ids):
    return max(seat_ids)


def solve_part2(seat_ids):
    seat_ids = set(seat_ids)
    max_seat_id = max(seat_ids)
    all_possible_seat_ids = set(range(max_seat_id))

    for seat_id in all_possible_seat_ids.difference(seat_ids):
        if set((seat_id - 1, seat_id + 1)).issubset(seat_ids):
            return seat_id


seat_ids = parse_ids([line for line in filter(None, map(str.strip, stdin))])

part = "2" if len(argv) > 1 and argv[1] == "2" else "1"
if part == "1":
    print(solve_part1(seat_ids))
else:
    print(solve_part2(seat_ids))
