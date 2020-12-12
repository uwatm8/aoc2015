import hashlib
filepath = 'data.txt'


l = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()

nl = len(l)

c = 0

n = 0

for i in range(nl):
    tl = l[i]

    res = hashlib.md5((tl + str(n)).encode('utf-8')).hexdigest()

    while res[:6] != "000000":
        res = hashlib.md5((tl + str(n)).encode('utf-8')).hexdigest()
        n += 1

    print("md5: ", n-1)


print("answer: ", c)
