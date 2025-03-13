from sys import stdin, argv
from ast import literal_eval
from json import dumps

part_two = len(argv) > 1 and argv[1] == "2"

literals: int = 0
chars: int = 0

if part_two:

    def fn(s: str) -> int:
        return len(dumps(s))

else:

    def fn(s: str) -> int:
        return len(literal_eval(s))


for s in filter(None, map(str.strip, stdin)):
    literals += len(s)
    chars += fn(s)

if part_two:
    print(chars - literals)
else:
    print(literals - chars)
