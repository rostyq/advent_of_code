from itertools import count
from hashlib import md5

for i in count():
    s = "bgvyzdsv" + str(i)

    hash = md5(s.encode()).hexdigest()

    if hash.startswith("000000"):
        print(i)
        break

