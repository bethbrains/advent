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
    santa_path = find_path(map, 'SAN')
    you_path = find_path(map, 'YOU')
    for node in you_path:
        if node in santa_path:
            print(find_path(map, 'YOU').index(node)-1 + find_path(map, 'SAN').index(node)-1)
            break