from pathlib import Path
from itertools import permutations
from sys import maxsize, stdin, argv


guests = set()
happiness_map = {}

for line in filter(None, map(str.strip, stdin)):
    guest_1, _, sign, value, *__, guest_2 = line.strip(".").split(" ")

    value = int(value if sign == "gain" else "-%s" % value)

    happiness_map[(guest_1, guest_2)] = value

    guests.add(guest_1)
    guests.add(guest_2)

if len(argv) > 1 and argv[1] == "2":
    guests.add("myself")
    for guest in guests:
        happiness_map[("myself", guest)] = 0
        happiness_map[(guest, "myself")] = 0

max_hapinness = -maxsize

for table in permutations(guests):
    total_hapinness = 0

    for i, guest in enumerate(table):
        j = i - 1 if i > 0 else -1
        k = i + 1 if i < (len(table) - 1) else 0
        neighbor_1, neighbor_2 = table[j], table[k]

        total_hapinness += happiness_map[(guest, neighbor_1)]
        total_hapinness += happiness_map[(guest, neighbor_2)]

    max_hapinness = max(max_hapinness, total_hapinness)

print(max_hapinness)
