import itertools


def apply_gravity(planets, axis):
    pairs = list(itertools.combinations([0, 1, 2, 3], 2))
    for pair in pairs:
        a = planets[pair[0]]
        b = planets[pair[1]]
        if a[axis][0] > b[axis][0]:
            a[axis][1] -= 1
            b[axis][1] += 1
        elif b[axis][0] > a[axis][0]:
            b[axis][1] -= 1
            a[axis][1] += 1
    return planets


def apply_velocity(planets, axis):
    for planet in planets:
        planet[axis][0] = planet[axis][0] + planet[axis][1]
    return planets


# EUCLID YO
def gcf(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcf(a, b)


with open("12input.txt") as fp:
    planets = []
    original_state = []
    for num, line in enumerate(fp, 0):
        x = int(line[3 : line.find(",")])
        y = int(line[line.find("y") + 2 : line.find("z") - 2])
        z = int(line[line.find("z") + 2 : line.find(">")])
        planets.append({0: [x, 0], 1: [y, 0], 2: [z, 0]})
        original_state.append({0: [x, 0], 1: [y, 0], 2: [z, 0]})
    cycles = []
    for axis in [0, 1, 2]:
        cycled = False
        cycle_count = 1
        while not cycled:
            planets = apply_velocity(apply_gravity(planets, axis), axis)
            match = True
            for planet in planets:
                if planet[axis] != original_state[planets.index(planet)][axis]:
                    match = False
                    cycle_count += 1
                    break
            if match:
                cycles.append(cycle_count)
                cycled = True
    print(cycles)

    print(lcm(cycles[2], lcm(cycles[0], cycles[1])))