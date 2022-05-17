from dataclasses import dataclass
from pathlib import Path

@dataclass
class Reindeer:
    name: str
    speed: int
    fly: int
    rest: int

reindeers: list[Reindeer] = []

with (Path(__file__).parent / 'input.txt').open('r') as f:
    for line in f.readlines():
        name, _, _, speed, _, _, fly, *_, rest, _ = line.split(" ")

        reindeers.append(Reindeer(name, int(speed), int(fly), int(rest)))


def travel_distance(seconds: int, reindeer: Reindeer) -> int:
    distance = 0
    fly = reindeer.fly
    rest = 0

    for _ in range(seconds):
        if fly > 0:
            distance += reindeer.speed
            fly -= 1

            if fly == 0:
                rest = reindeer.rest

        elif rest > 0:
            rest -= 1

            if rest == 0:
                fly = reindeer.fly
    
    return distance

max_distance = max([travel_distance(2503, reindeer) for reindeer in reindeers])

print(max_distance)
