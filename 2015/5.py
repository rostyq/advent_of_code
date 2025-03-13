from sys import argv, stdin


def rule_1_1(word: str) -> bool:
    vowels = 0
    for s in word:
        if s in "aeiou":
            vowels += 1

    return vowels >= 3


def rule_1_2(word: str) -> bool:
    for i in range(len(word) - 1):
        if word.count(word[i : i + 2]) >= 2:
            return True
    return False


def rule_2(word: str, *, param: int = 1) -> bool:
    for s in range(0, len(word) - param):
        if word[s] == word[s + param]:
            return True
    return False


def rule_3(word: str) -> bool:
    for s in ("ab", "cd", "pq", "xy"):
        if s in word:
            return False
    return True


if len(argv) > 1 and argv[1] == "2":
    rules = (rule_1_2, lambda word: rule_2(word, param=2))
else:
    rules = (rule_1_1, rule_2, rule_3)


def is_nice(word: str) -> bool:
    return all((rule(word) for rule in rules))


print(sum([is_nice(word) for word in filter(None, map(str.strip, stdin))]))
