from operator import and_, rshift, lshift, or_, invert


with open("input.txt", "r") as f:
    instructions = [line.strip() for line in f.readlines()]

wires = {}

operators = {
    "AND": and_,
    "OR": or_,
    "LSHIFT": lshift,
    "RSHIFT": rshift,
    "NOT": invert,
}

for instruction in instructions:
    leftside, rightside = (s.strip() for s in instruction.split("->"))
    leftside = leftside.split()

    name = rightside
    operator = None
    left_wire = None
    right_wire = None

    if len(leftside) == 1:
        left_wire = leftside[0]
    elif len(leftside) == 2:
        operator, right_wire = leftside
    elif len(leftside) == 3:
        left_wire, operator, right_wire = leftside

    if left_wire is not None and left_wire.isdigit():
        left_wire = int(left_wire)

    if right_wire is not None and right_wire.isdigit():
        right_wire = int(right_wire)

    if operator is not None:
        operator = operators[operator]

    leftside = [p for p in [left_wire, operator, right_wire]
                if p is not None]

    wires[name] = leftside[0] if len(leftside) == 1 else leftside


def find(name):
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

wires["b"] = 3176
print(find('a'))
