def rule_1(word: str) -> bool:
    for i in range(len(word) - 1):
        if word.count(word[i:i+2]) >= 2:
            return True
    return False


def rule_2(word: str) -> bool:
    for i in range(len(word) - 2):
        if word[i] == word[i + 2]:
            return True

    return False


def is_nice(word: str) -> bool:
    return all((rule(word) for rule in (rule_1, rule_2)))


with open("input.txt", "r") as f:
    words = [line.strip('\n') for line in f.readlines()]


nice = 0

print(sum([is_nice(word) for word in words]))
