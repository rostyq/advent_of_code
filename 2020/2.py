from typing import Iterable
from sys import stdin, argv
from re import match


class Policy:
    def __init__(self, letter):
        self.letter = letter

    def check_password(self, s):
        raise


class Policy1(Policy):
    def __init__(self, letter, lowest, highest):
        super().__init__(letter)
        self.lowest = lowest
        self.highest = highest

    def check_password(self, s):
        n = s.count(self.letter)
        if n < self.lowest:
            return False
        elif n > self.highest:
            return False
        else:
            return True


class Policy2(Policy):
    def __init__(self, letter, first, second):
        super().__init__(letter)
        self.first = first - 1
        self.second = second - 1

    def check_password(self, s):
        contains_first = s[self.first] == self.letter
        contains_second = s[self.second] == self.letter

        if contains_first and not contains_second:
            return True
        elif not contains_first and contains_second:
            return True
        else:
            return False


def parse_entry(s, policy_factory):
    result = match(r"(\d+)-(\d+) ([a-zA-Z]): ([a-zA-Z]+)", s)
    if result:
        number1, number2, letter, password = result.groups()
        return policy_factory(letter, int(number1), int(number2)), password


def solve(entries: Iterable[str], policy_factory: type[Policy]):
    valid_count = 0

    for entry in entries:
        policy, password = parse_entry(entry, policy_factory)

        if policy.check_password(password):
            valid_count += 1

    return valid_count


entries = [line for line in filter(None, map(str.strip, stdin))]

policy_factory = Policy2 if len(argv) > 1 and argv[1] == "2" else Policy1
print(solve(entries, policy_factory))
