from sys import stdin, argv
from itertools import combinations
from collections import Counter


liters = 150
containers = [*map(int, filter(None, map(str.strip, stdin)))]

combination_count: int = 0
container_counts: Counter[int] = Counter()

for count in range(1, len(containers) + 1):
    for combination in combinations(containers, count):
        if sum(combination) == liters:
            combination_count += 1
            container_counts[count] += 1


if len(argv) > 1 and argv[1] == "2":
    print(container_counts[min(container_counts)])
else:
    print(combination_count)
