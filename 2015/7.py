from sys import argv, stdin
from operator import and_, rshift, lshift, or_, invert


wires: dict[str, list | str | int] = {}

for instruction in filter(None, map(str.strip, stdin)):
    leftside, rightside = map(str.strip, instruction.split("->", 1))
    leftside = leftside.split()

    name = rightside
    op = None
    left_wire = None
    right_wire = None

    if len(leftside) == 1:
        left_wire = leftside[0]
    elif len(leftside) == 2:
        op, right_wire = leftside
    elif len(leftside) == 3:
        left_wire, op, right_wire = leftside

    if left_wire is not None and left_wire.isdigit():
        left_wire = int(left_wire)

    if right_wire is not None and right_wire.isdigit():
        right_wire = int(right_wire)

    match op:
        case "AND":
            op = and_
        case "OR":
            op = or_
        case "LSHIFT":
            op = lshift
        case "RSHIFT":
            op = rshift
        case "NOT":
            op = invert

    leftside = [p for p in [left_wire, op, right_wire] if p is not None]

    wires[name] = leftside[0] if len(leftside) == 1 else leftside


if len(argv) > 1:
    wires["b"] = int(argv[1])


def find(name: str):
    exp = wires[name]

    result = None

    if isinstance(exp, list):
        if len(exp) == 3:
            left, op, right = exp
            right = right if isinstance(right, int) else find(right)
            left = left if isinstance(left, int) else find(left)
            result = op(left, right)
        elif len(exp) == 2:
            op, right = exp
            result = op(right if isinstance(right, int) else find(right))
        else:
            raise
    elif isinstance(exp, str):
        result = find(exp)
    elif isinstance(exp, int):
        result = exp
    else:
        raise

    wires[name] = result

    return result


print(find("a"))
