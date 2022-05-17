from dataclasses import dataclass
from pathlib import Path

@dataclass
class Reindeer:
    name: str

    fly_speed: int
    fly_duration: int
    rest_duration: int

    fly_time_left: int = 0
    rest_time_left: int = 0
    travel_distance: int = 0
    score: int = 0

    def __post_init__(self):
        self.fly_time_left = self.fly_duration

    def travel(self):
        if self.fly_time_left > 0:
            self.travel_distance += self.fly_speed
            self.fly_time_left -= 1

            if self.fly_time_left == 0:
                self.rest_time_left = self.rest_duration

        elif self.rest_time_left > 0:
            self.rest_time_left -= 1

            if self.rest_time_left == 0:
                self.fly_time_left = self.fly_duration
    
    def increase_score(self, value: int = 1):
        self.score += value

reindeers: list[Reindeer] = []

with (Path(__file__).parent / 'input.txt').open('r') as f:
    for line in f.readlines():
        name, _, _, speed, _, _, fly, *_, rest, _ = line.split(" ")

        reindeers.append(Reindeer(name, int(speed), int(fly), int(rest)))


for _ in range(2503):
    for deer in reindeers:
        deer.travel()

    lead_distance = max(reindeers, key=lambda d: d.travel_distance).travel_distance

    for deer in reindeers:
        if deer.travel_distance == lead_distance:
            deer.increase_score()

print(max(reindeers, key=lambda d: d.score).score)
