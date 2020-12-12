import math

filepath = 'data.txt'

l = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()

nl = len(l)

c = 0

print("nl", nl)

for i in range(nl):
    tl = l[i]
    print(tl)

for i in range(nl):
    tl = str(l[i])

    p = tl.split('x')

    le = int(p[0])
    w = int(p[1])
    h = int(p[2])

    print(le, w, h)

    total = 2*le*w + 2*w*h + 2*h*le

    reserve = min(le*w, w*h, h*le)

    c += total+reserve

print("answer: ", c)
