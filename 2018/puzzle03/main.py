fname = "input_sample.txt"
fp = open(fname)

"""
#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
"""

size = 10
fabric = [[0] * size] * size


def blueprint(area, notation):
    start_and_size = notation.split('@ ')[-1].strip()
    start_pair, size_pair = start_and_size.split(': ')
    x, y = start_pair.split(',')
    w, h = size_pair.split('x')

    for px in range(int(w)):
        for py in range(int(h)):
            area[int(y) + py][int(x) + px] += 1

    return area


for line in fp.readlines():
    line = line.strip()

    fabric = blueprint(fabric, line)

fabric = "\n".join(["".join(ln) for ln in fabric])
print(fabric)
