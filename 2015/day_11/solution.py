from string import ascii_lowercase


MIN = ord(min(ascii_lowercase))
MAX = ord(max(ascii_lowercase))


def rule_1(s: str) -> bool:
    for i in range(len(s) - 3):
        if s[i:i+3] in ascii_lowercase:
            return True
    return False


def rule_2(s: str) -> bool:
    for l in s:
        if l in 'iol':
            return False
    return True


def rule_3(s: str) -> bool:
    pairs = set()
    for v1, v2 in zip(s[:-1], s[1:]):
        if v1 == v2:
            pairs.add(v1)

    if len(pairs) >= 2:
        return True
    else:
        return False


def rules(s: str) -> bool:
    for rule in [rule_1, rule_2, rule_3]:
        if not rule(s):
            return False

    return True


def increment(s: str) -> str:
    arr = [ord(l) for l in s[::-1]]
    result = []
    incr = True

    for v in arr:
        if incr:
            incr = v == MAX
            v = MIN if incr else v + 1
        result.append(chr(v))

    return "".join(result[::-1])


if __name__ == "__main__":
    from sys import argv

    password = increment(argv[1])

    while not rules(password):
        password = increment(password)

    print(password)
