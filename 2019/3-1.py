def get_line_coordinates (line):
    line = line.split(",")
    x = 0
    y = 0
    line_coordinates = []
    for dir in line:
        distance = int(dir.strip("RLUD"))
        if dir.startswith("R"):
            for i in range(1, distance+1):
                x = x + 1
                line_coordinates.append([x,y])
        if dir.startswith("L"):
            for i in range(1, distance+1):
                x = x - 1
                line_coordinates.append([x,y])
        if dir.startswith("U"):
            for i in range(1, distance+1):
                y = y + 1
                line_coordinates.append([x,y])
        if dir.startswith("D"):
            for i in range(1, distance+1):
                y = y - 1
                line_coordinates.append([x,y])
    return line_coordinates


def intersection(lst1, lst2):
    tup1 = map(tuple, lst1)
    tup2 = map(tuple, lst2)
    return list(map(list, set(tup1).intersection(tup2)))


def get_min_manhattan(crosses):
    distances = []
    for cross in crosses:
        distances.append(abs(cross[0]) + abs(cross[1]))
    return min(distances)


with open("3input.txt") as fp:
    paths = {}
    for num, line in enumerate(fp, 1):
        paths[num] = get_line_coordinates(line)
    wire1 = paths[1]
    wire2 = paths[2]
    crosses = intersection(wire1, wire2)
    min_manhattan = get_min_manhattan(crosses)
    print(min_manhattan)
