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


def path_node(map, node, path):
    for sat in map:
        if node == 'COM':
            return path
        elif node in map[sat]:
            path.append(sat)
            return path.append(path_node(map, sat, path))


def find_path(map, node):
    path = [node]
    path.append(path_node(map, node, path))
    #print(path)
    return path


with open('6input.txt') as fp:
    map = makeMap(fp)
    count = count_orbits(map)
    print(count)
    for node in find_path(map, 'YOU'):
        if node in find_path(map, 'SAN'):
            print(find_path(map, 'YOU').index(node)-1 + find_path(map, 'SAN').index(node)-1)
            break