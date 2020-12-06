import re
from functools import reduce

REQUIRED_FIELDS = {
    "byr",  # (Birth Year)
    "iyr",  # (Issue Year)
    "eyr",  # (Expiration Year)
    "hgt",  # (Height)
    "hcl",  # (Hair Color)
    "ecl",  # (Eye Color)
    "pid",  # (Passport ID)
    # "cid",  # (Country ID) optional
}


def parse_passports(s: str) -> iter:
    for entry in s.strip().split("\n\n"):
        yield dict([
            pair.split(":")
            for pair in entry.replace("\n", " ").split(" ")
        ])


def check_passport_1(passport: dict) -> bool:
    return REQUIRED_FIELDS.issubset(set(passport.keys()))


def check_bounds(value: int, lower: int, upper: int) -> bool:
    if value >= lower and value <= upper:
        return True
    else:
        return False


def check_year(s: str, lower: int, upper: int) -> bool:
    if re.match(r"\d{4}$", s) is None:
        return False
    else:
        return check_bounds(int(s), lower, upper)


def check_height(s: str) -> bool:
    result = re.match(r"(\d+)(cm|in)$", s)
    if result is None:
        return False
    value, unit = result.groups()
    value = int(value)
    if unit == "cm":
        return check_bounds(value, 150, 193)
    elif unit == "in":
        return check_bounds(value, 59, 76)



def check_passport_2(passport: dict) -> bool:
    if not check_passport_1(passport):
        return False

    if not check_year(passport["byr"], 1920, 2002):
        return False

    if not check_year(passport["iyr"], 2010, 2020):
        return False

    if not check_year(passport["eyr"], 2020, 2030):
        return False

    if not check_height(passport["hgt"]):
        return False

    if re.match(r"#([0-9a-f]{6})$", passport["hcl"]) is None:
        return False

    if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False

    if re.match(r"\d{9}$", passport["pid"]) is None:
        return False

    return True


def main():
    from pathlib import Path

    input_path = Path(__file__).parent / "passports.txt"

    with input_path.open('r') as fp:
        passports = list(parse_passports(fp.read()))

    def agg(count, passport, checker):
        return count + 1 if checker(passport) else count

    for f in check_passport_1, check_passport_2:
        valid_count = reduce(lambda c, p: agg(c, p, f), passports, 0)
        print(valid_count)


if __name__ == "__main__":
    main()
