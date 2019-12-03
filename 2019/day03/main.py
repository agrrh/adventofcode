fname = 'input.txt'

# Part ONE

with open(fname) as fp:
    cables = [
        cable.strip().split(',')
        for cable
        in fp.readlines()
    ]

# print(cables)

def path(cable):
    dirs = {
        'U': (0, -1),
        'R': (+1, 0),
        'D': (0, +1),
        'L': (-1, 0),
    }

    path = []

    x, y = (0, 0)

    for part in cable:
        _dir, len = dirs[part[0]], int(part[1:])

        while len > 0:
            path.append((x, y))
            x += _dir[0]
            y += _dir[1]
            len -= 1

    return path


paths = [path(cable) for cable in cables]
# print(paths)

p1 = paths[0]
p2 = paths[1]

intersections = set(p1).intersection(p2)

# print(intersections)

distances = [abs(x) + abs(y) for (x, y) in intersections]
distances.sort()
print(distances[1])

# Part TWO

prices = []
for isect in intersections:
    price1 = p1.index(isect)
    price2 = p2.index(isect)

    prices.append(price1 + price2)

prices.sort()

print(prices[1])

print('done')
