input_ = range(136760, 595730 + 1)

# Part ONE


def validate(p):
    if p > 999999 or p < 100000:
        return False

    seen_same = False

    for i in range(len(str(p)) - 1):
        if str(p)[i] > str(p)[i + 1]:
            return False
        if str(p)[i] == str(p)[i + 1]:
            seen_same = True

    if not seen_same:
        return False

    return True


i = 0
for password in input_:
    if validate(password):
        i += 1

print(i)


# Part TWO


def double(p):
    clusters = []

    for d in str(p):
        if not clusters:
            clusters.append([d])
        else:
            if d in clusters[-1]:
                clusters[-1].append(d)
            else:
                clusters.append([d])

    if 2 in [len(c) for c in clusters]:
        return True

    return False


i = 0
for password in input_:
    if validate(password) and double(password):
        i += 1

print(i)
