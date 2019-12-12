import itertools


def get_energy(planets):
    print(planets)
    total_energy = 0
    for planet in planets:
        kin = 0
        pot = 0
        for i in planet["pos"]:
            pot += abs(i)
        for i in planet["vel"]:
            kin += abs(i)
        total_energy += kin * pot
    return total_energy


def apply_gravity(planets):
    pairs = list(itertools.combinations([0, 1, 2, 3], 2))
    for pair in pairs:
        a = planets[pair[0]]
        b = planets[pair[1]]
        for axis in [0, 1, 2]:
            if a["pos"][axis] > b["pos"][axis]:
                a["vel"][axis] -= 1
                b["vel"][axis] += 1
            elif b["pos"][axis] > a["pos"][axis]:
                b["vel"][axis] -= 1
                a["vel"][axis] += 1
    return planets


def apply_velocity(planets):
    for planet in planets:
        for axis in [0, 1, 2]:
            planet["pos"][axis] = planet["pos"][axis] + planet["vel"][axis]
    return planets


with open("12input.txt") as fp:
    planets = []
    for num, line in enumerate(fp, 0):
        x = int(line[3 : line.find(",")])
        y = int(line[line.find("y") + 2 : line.find("z") - 2])
        z = int(line[line.find("z") + 2 : line.find(">")])
        planets.append({"pos": [x, y, z], "vel": [0, 0, 0]})
    steps = 1000
    for i in range(0, steps):
        print(planets)
        planets = apply_velocity(apply_gravity(planets))
    print(get_energy(planets))
