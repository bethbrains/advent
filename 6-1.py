def makeMap(fp):
    map = {}
    for line in fp:
        items = line.strip('\n').split(")")
        node = items[0]
        satellite = items[1]
        if not node in map:
            map[node] = [satellite]
        else:
            map[node].append(satellite)
    return map


def count_key(map, key):
    count = len(map[key])
    for node in map[key]:
        if node in map:
            count += count_key(map, node)
    return count


def count_orbits(map):
    orbit_count = 0
    for key in map:
        orbit_count += count_key(map, key)
    return orbit_count


with open('6input.txt') as fp:
    map = makeMap(fp)
    print(map)
    count = count_orbits(map)
    print(count)