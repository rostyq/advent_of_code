from sys import stdin, argv


if len(argv) > 1 and argv[1] == "2":

    def fn(l: int, w: int, h: int) -> int:
        p1, p2, p3 = (2 * p for p in (l + w, w + h, h + l))
        return min(p1, p2, p3) + l * w * h

else:

    def fn(l: int, w: int, h: int) -> int:
        s1, s2, s3 = l * w, w * h, h * l
        return min(s1, s2, s3) + 2 * s1 + 2 * s2 + 2 * s3

result = 0

for line in filter(len, map(str.strip, stdin)):
    l, w, h = (int(i) for i in line.split("x"))
    result += fn(l, w, h)

print(result)
