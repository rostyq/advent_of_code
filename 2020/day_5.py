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


def main():
    from pathlib import Path

    input_path = Path(__file__).parent / "boarding_passes.txt"

    with input_path.open('r') as fp:
        seat_ids = parse_ids(fp.readlines())

    # part 1
    max_seat_id = max(seat_ids)
    print(max_seat_id)

    # part 2
    seat_ids = set(seat_ids)
    all_possible_seat_ids = set(range(max_seat_id))

    for seat_id in all_possible_seat_ids.difference(seat_ids):
        if set((seat_id - 1, seat_id + 1)).issubset(seat_ids):
            print(seat_id)
            break


if __name__ == "__main__":
    main()
