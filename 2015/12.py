from sys import stdin, argv
from json import load


result = 0


def collect_int(v: str):
    global result
    v = int(v)
    result += v
    return v


def sum_int_2(data):
    if isinstance(data, list):
        return sum(sum_int_2(item) for item in data)
    elif isinstance(data, dict):
        if "red" in [*data.keys(), *data.values()]:
            return 0
        else:
            return sum(sum_int_2(item) for item in data.values())
    elif isinstance(data, int):
        return data
    else:
        return 0


data = load(stdin, parse_int=collect_int)

if len(argv) > 1 and argv[1] == "2":
    print(sum_int_2(data))
else:
    print(result)
