def rule_1(word: str) -> bool:
    vowels = 0
    for s in word:
        if s in "aeiou":
            vowels += 1

    return vowels >= 3


def rule_2(word: str) -> bool:
    for s in range(0, len(word) - 1):
        if word[s] == word[s + 1]:
            return True
    return False


def rule_3(word: str) -> bool:
    for s in ("ab", "cd", "pq", "xy"):
        if s in word:
            return False
    return True


def is_nice(word: str) -> bool:
    return all((rule(word) for rule in (rule_1, rule_2, rule_3)))


with open("input.txt", "r") as f:
    words = [line.strip('\n') for line in f.readlines()]


nice = 0

print(sum([is_nice(word) for word in words]))
