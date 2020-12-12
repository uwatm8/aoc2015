filepath = 'data.txt'

l = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()

nl = len(l)

c = 0

a = ""

for i in range(nl):
    tl = l[i]

    a += tl

    for i in range(len(a)):
        char = a[i]
        if char == '(':
            c += 1
        if char == ')':
            c -= 1

        if c == -1:
            print("i", i+1)
