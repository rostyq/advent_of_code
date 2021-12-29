import json
from pathlib import Path

with (Path(__file__).parent / 'input.txt').open('r') as f:
    raw = f.read()

sum = 0

def parse_int(i):
    global sum
    i = int(i)
    sum += i
    return i

json.loads(raw, parse_int=parse_int)

print(sum)
