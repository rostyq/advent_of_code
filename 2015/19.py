from sys import stdin, argv
from itertools import takewhile
from collections import defaultdict


def parse_replacement(s: str) -> tuple[str, str]:
    left, right = map(str.strip, s.strip().split("=>", 1))
    return left, right


def parse_elements(molecule: str) -> list[str]:
    return [
        char + "".join(takewhile(str.islower, molecule[i + 1 :]))
        for i, char in enumerate(molecule)
        if char.isupper()
    ]


puzzle = map(str.strip, stdin)

replacements = defaultdict[str, list[list[str]]](list)
for left, right in map(parse_replacement, takewhile(bool, puzzle)):
    replacements[left].append(parse_elements(right))

input_molecule = next(puzzle)
molecule_elements = parse_elements(input_molecule)

if len(argv) > 1 and argv[1] == "2":
    # https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4h7ji/
    # steps = #elements - #Rn - #Ar - 2 * #Y - 1
    print(
        len(molecule_elements)
        - molecule_elements.count("Rn")
        - molecule_elements.count("Ar")
        - 2 * molecule_elements.count("Y")
        - 1
    )
else:
    distinct_molecules = set[str]()
    for replace_element, replace_variants in replacements.items():
        replace_indices = [
            index
            for index, element in enumerate(molecule_elements)
            if element == replace_element
        ]

        for replace_variant in replace_variants:
            for replace_index in replace_indices:
                temp_elements = molecule_elements.copy()
                temp_elements[replace_index : replace_index + 1] = replace_variant
                distinct_molecules.add("".join(temp_elements))

    print(len(distinct_molecules))
