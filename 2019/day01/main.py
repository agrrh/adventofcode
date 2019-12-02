import math


def fuel_reqs(m):
    r = math.floor(m / 3) - 2
    return r if r > 0 else 0


def fuel_reqs_recursive(m):
    s = 0
    while fuel_reqs(m) > 0:
        s += fuel_reqs(m)
        m = fuel_reqs(m)
    return s


if __name__ == '__main__':
    with open('input.txt') as fp:
        data = fp.readlines()

    data = [int(_.strip()) for _ in data]

    r = [
        fuel_reqs(module_mass)
        for module_mass
        in data
    ]

    print('sum of the fuel requirements for all of the modules: {}'.format(sum(r)))

    r = [
        fuel_reqs_recursive(module_mass)
        for module_mass
        in data
    ]

    print('sum of the fuel requirements for all of the modules on your spacecraft when also taking into account the mass of the added fuel: {}'.format(sum(r)))
