from functools import reduce
from itertools import product
from pathlib import Path
from dataclasses import dataclass

@dataclass
class Properties:
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int

    def __add__(self, other: 'Properties') -> 'Properties':
        return self.__class__(
            capacity=self.capacity + other.capacity,
            durability=self.durability + other.durability,
            flavor=self.flavor + other.flavor,
            texture=self.texture + other.texture,
            calories=self.calories + other.calories,
        )
    
    def __iadd__(self, other: 'Properties') -> 'Properties':
        self.capacity = self.capacity + other.capacity
        self.durability = self.durability + other.durability
        self.flavor = self.flavor + other.flavor
        self.texture = self.texture + other.texture
        self.calories = self.calories + other.calories

        return self

    def score(self) -> int:
        return reduce(
            lambda s, v: s * max(v, 0),
            [self.capacity, self.durability, self.flavor, self.texture],
            1
        )
    
    @classmethod
    def zero(cls) -> 'Properties':
        return cls(0, 0, 0, 0, 0)


@dataclass
class Ingridient(Properties):
    name: str

    def __mul__(self, other: int) -> 'Ingridient':
        return self.__class__(
            name=self.name,
            capacity=self.capacity * other,
            durability=self.durability * other,
            flavor=self.flavor * other,
            texture=self.texture * other,
            calories=self.calories * other,
        )
    
    def __hash__(self):
        return hash(self.name)
    

def recipe_score(recipe: dict[str, int], ingridients: list[Ingridient]) -> int:
    # print("recipe:", recipe)
    mix = Properties.zero()
    for ingridient in ingridients:
        mix += (ingridient * recipe[ingridient.name])

    # print("result:", mix)
    # print("score:", mix.score())

    return mix.score() if mix.calories == 500 else 0


def generate_recipes(names: set[str], total: int):
    start = 1
    stop = total - len(names) + 2
    for counts in product(range(start, stop), repeat=len(names)):
        if sum(counts) == total:
            yield {name: counts[i] for i, name in enumerate(names)}
        else:
            continue

ingridients: set[Ingridient] = set()

with open(Path(__file__).parent / 'input.txt', 'r') as f:
    for line in f.readlines():
        name, description = line.strip().split(":")

        stats = [desc.strip().split(" ") for desc in description.split(",")]
        stats = {stat: int(value) for (stat, value) in stats}

        ingridients.add(Ingridient(name=name, **stats))

print(
    max(
        [
            recipe_score(recipe, ingridients)
            for recipe in generate_recipes(set(i.name for i in ingridients), 100)
        ]
    )
)
