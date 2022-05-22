import re
from pathlib import Path
from dataclasses import dataclass, astuple
from typing import Optional

@dataclass
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

    def match(self, other: 'Clue') -> int:
        score = 0
        for s, o in zip(astuple(self), astuple(other)):
            if o is not None and o == s:
                score += 1
        return score
        

clues: list[Clue] = []

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
    perfumes=1
)

with open(Path(__file__).parent / 'input.txt', 'r') as f:
    for line in f.readlines():
        m = re.match(r"Sue (\d{3}): ", line)

        if m is None:
            continue

        id = int(m.group(1))

        clue_data = [item.split(": ") for item in line[m.end():].strip().split(", ")]
        clue_data = {name: int(value) for name, value in clue_data}

        clues.append(Clue(id=id, **clue_data))

max_id = None
max_score = 0

for clue in clues:
    score = gift_clue.match(clue)
    if score > max_score:
        max_score = score
        max_id = clue.id

print(max_id)
