from dataclasses import dataclass
from sys import stdin, argv


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

    @classmethod
    def from_input(cls, line: str):
        name, _, _, speed, _, _, fly, *_, rest, _ = line.split(" ")

        return cls(name, int(speed), int(fly), int(rest))

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


def travel_distance(seconds: int, reindeer: Reindeer) -> int:
    distance = 0
    fly = reindeer.fly_duration
    rest = 0

    for _ in range(seconds):
        if fly > 0:
            distance += reindeer.fly_speed
            fly -= 1

            if fly == 0:
                rest = reindeer.rest_duration

        elif rest > 0:
            rest -= 1

            if rest == 0:
                fly = reindeer.fly_duration

    return distance


SECONDS = 2503

reindeers = [*map(Reindeer.from_input, filter(None, map(str.strip, stdin)))]

if len(argv) > 1 and argv[1] == "2":
    for _ in range(SECONDS):
        for deer in reindeers:
            deer.travel()

        lead_distance = max(reindeers, key=lambda d: d.travel_distance).travel_distance

        for deer in reindeers:
            if deer.travel_distance == lead_distance:
                deer.increase_score()

    print(max(reindeers, key=lambda d: d.score).score)
else:
    print(max(map(lambda deer: travel_distance(SECONDS, deer), reindeers)))
