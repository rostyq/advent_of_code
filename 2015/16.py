from sys import stdin, argv
from functools import cache
from dataclasses import dataclass, astuple, fields, field
from re import match
from typing import Optional, Self


@dataclass(kw_only=True)
class Clue:
    id: int
    children: Optional[int] = None
    cats: Optional[int] = None
    samoyeds: Optional[int] = None
    pomeranians: Optional[int] = None
    akitas: Optional[int] = None
    vizslas: Optional[int] = None
    goldfish: Optional[int] = None
    trees: Optional[int] = None
    cars: Optional[int] = None
    perfumes: Optional[int] = None

    @classmethod
    @cache
    def allowed_fields(cls) -> list[str]:
        return [field.name for field in fields(cls)]

    @classmethod
    def try_parse(cls, line: str) -> Optional[Self]:
        m = match(r"Sue (\d{3}): ", line)

        if m is None:
            return None

        id = int(m.group(1))

        clue_data = [item.split(": ") for item in line[m.end() :].strip().split(", ")]
        clue_data = {
            name: int(value)
            for name, value in clue_data
            if name in cls.allowed_fields()
        }

        return cls(id=id, **clue_data)


def match_clues_1(left: Clue, right: Clue) -> int:
    score = left.children == right.children
    score += left.cats == right.cats
    score += left.samoyeds == right.samoyeds
    score += left.pomeranians == right.pomeranians
    score += left.akitas == right.akitas
    score += left.vizslas == right.vizslas
    score += left.goldfish == right.goldfish
    score += left.trees == right.trees
    score += left.cars == right.cars
    score += left.perfumes == right.perfumes
    return score


def match_clues_2(left: Clue, right: Clue) -> int:
    score = left.children == right.children
    score += right.cats is not None and left.cats < right.cats
    score += left.samoyeds == right.samoyeds
    score += right.pomeranians is not None and left.pomeranians > right.pomeranians
    score += left.akitas == right.akitas
    score += left.vizslas == right.vizslas
    score += right.goldfish is not None and left.goldfish > right.goldfish
    score += right.trees is not None and left.trees < right.trees
    score += left.cars == right.cars
    score += left.perfumes == right.perfumes
    return score


gift_clue = Clue(
    id=0,
    children=3,
    cats=7,
    samoyeds=2,
    pomeranians=3,
    akitas=0,
    vizslas=0,
    goldfish=5,
    trees=3,
    cars=2,
    perfumes=1,
)

match_clues = match_clues_2 if len(argv) > 1 and argv[1] == "2" else match_clues_1

scores = {
    clue.id: match_clues(gift_clue, clue)
    for clue in filter(None, map(Clue.try_parse, stdin))
}
print(max(scores, key=scores.get))
