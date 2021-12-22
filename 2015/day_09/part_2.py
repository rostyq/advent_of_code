from itertools import permutations

with open('input.txt', 'r') as f:
    lines = f.readlines()

cities = set()
distances = {}

for line in lines:
    s, distance = line.strip().split(" = ")
    distance = int(distance.strip())
    city1, city2 = s.split(" to ")

    cities.add(city1)
    cities.add(city2)

    distances.setdefault(city1, {})
    distances.setdefault(city2, {})

    distances[city1][city2] = distance
    distances[city2][city1] = distance

max_distance = 0

for route in permutations(cities):
    route_distance = 0
    for city1, city2 in zip(route[:-1], route[1:]):
        route_distance += distances[city1][city2]

    if route_distance > max_distance:
        max_distance = route_distance

print(max_distance)
