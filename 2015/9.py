from sys import stdin, argv
from math import inf
from itertools import permutations
from operator import lt, gt


cities: set[str] = set()
distances: dict[str, dict[str, int]] = {}

for line in filter(None, map(str.strip, stdin)):
    s, distance = line.strip().split(" = ", 1)
    distance = int(distance.strip())
    city1, city2 = s.split(" to ", 1)

    cities.update([city1, city2])

    distances.setdefault(city1, {})[city2] = distance
    distances.setdefault(city2, {})[city1] = distance

threshold: int
if len(argv) > 1 and argv[1] == "2":
    threshold, op = 0, gt
else:
    threshold, op = inf, lt

for route in permutations(cities):
    route_distance = 0
    for city1, city2 in zip(route[:-1], route[1:]):
        route_distance += distances[city1][city2]

    if op(route_distance, threshold):
        threshold = route_distance

print(threshold)
