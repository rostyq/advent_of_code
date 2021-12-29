import json
from pathlib import Path


with (Path(__file__).parent / 'input.txt').open('r') as fp:
    data = json.load(fp)


def solution(data):
    if isinstance(data, list):
        return sum(solution(item) for item in data)
    elif isinstance(data, dict):
        if "red" in [*data.keys(), *data.values()]:
            return 0
        else:
            return sum(solution(item) for item in data.values())
    elif isinstance(data, int):
        return data
    else:
        return 0



print(solution(data))
