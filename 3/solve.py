filepath = 'data.txt'

l = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()

nl = len(l)

c = 0

x = 0
y = 0

rx = 0
ry = 0

houses = {}

for i in range(nl):

    tl = l[i]

    for j in tl:
        if j == '>':
            x += 1
        if j == '<':
            x -= 1
        if j == '^':
            y += 1
        if j == 'v':
            y -= 1

        key = ""+str(x)+"."+str(y)

        if not key in houses:
            houses[key] = 1

print(len(houses))

print("answer: ", c)
