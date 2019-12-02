fname = 'input.txt'

# Part ONE

with open(fname) as fp:
    data = [
        int(_)
        for _
        in fp.read().strip().split(',')
    ]

data[1] = 12
data[2] = 2

p = 0
while True:
    if data[p] == 1:
        data[data[p + 3]] = data[data[p + 1]] + data[data[p + 2]]
        p += 4
        continue

    if data[p] == 2:
        data[data[p + 3]] = data[data[p + 1]] * data[data[p + 2]]
        p += 4
        continue

    if data[p] == 99:
        print(data[0])
        break

# Part TWO

for noun in range(100):
    for verb in range(100):
        with open(fname) as fp:
            data = [
                int(_)
                for _
                in fp.read().strip().split(',')
            ]

        data[1] = noun
        data[2] = verb

        p = 0
        while p < len(data):
            # print(p, data[p], data[p:p + 4])

            if data[p] == 1:
                data[data[p + 3]] = data[data[p + 1]] + data[data[p + 2]]
                p += 4
                continue

            if data[p] == 2:
                data[data[p + 3]] = data[data[p + 1]] * data[data[p + 2]]
                p += 4
                continue

            if data[p] == 99:
                p += 1
                # print(data[0], noun, verb, 100 * noun + verb)
                if data[0] == 19690720:
                    print(100 * noun + verb)
                break
