import numpy

def check_slope(x_inc, y_inc):
    tree_count = 0
    with open('3input.txt') as fp:
        fp = fp.read().splitlines()
        for i in range(0, len(fp)):
            if i % y_inc == 0:
                desired_x_index = (i/y_inc)*x_inc
                actual_x_index = desired_x_index % len(fp[i])
                if fp[i][actual_x_index] == '#':
                    tree_count += 1
    return tree_count

def part_two():
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)]
    return numpy.prod([check_slope(x, y) for (x, y) in slopes])

def part_one():
    x_inc = 3
    y_inc = 1
    return check_slope(x_inc, y_inc)


if __name__ == "__main__":
    print(part_one())
    print(part_two())
