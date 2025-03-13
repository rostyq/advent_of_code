from sys import argv
from itertools import count
from hashlib import md5

puzzle = input()
prefix = "000000" if len(argv) > 1 and argv[1] == "2" else "00000"

for i, s in enumerate(map(str, count())):
    s = (puzzle + s).encode()

    if md5(s).hexdigest().startswith(prefix):
        print(i)
        break
