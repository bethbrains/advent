import fractions


def get_slope(a, b):
    rise = b["y"] - a["y"]
    run = b["x"] - a["x"]
    if run == 0:
        slope = "und"
    else:
        quad = 0
        if rise < 0 and run < 0:
            quad = 4
        elif rise < 0 and run > 0:
            quad = 1
        elif rise > 0 and run < 0 :
            quad = 3
        elif rise > 0 and run > 0:
            quad = 2
        # dir = "up" if rise < 0 else "down"
        slope = (fractions.Fraction(rise, run), quad)
    return slope


def detect_asteroids(asteroids):
    for a in asteroids:
        a["detected"] = 0
        slopes = []
        for b in asteroids:
            if a != b:
                slopes.append(get_slope(a, b))
        a["slopes"] = slopes
        a["detected"] = len(set(slopes))
    return asteroids


def parse_map(fp):
    asteroids = []
    for num, line in enumerate(fp, 0):
        line_pos = 0
        for pos in list(line):
            if pos == "#":
                asteroids.append({"x": line_pos, "y": num})
            line_pos += 1
    return asteroids


with open("10input.txt") as fp:
    asteroids = parse_map(fp)
    asteroids = detect_asteroids(asteroids)
    besteroid = asteroids[0]
    for asteroid in asteroids:
        if asteroid["detected"] > besteroid["detected"]:
            besteroid = asteroid
    print(besteroid["x"])
    print(besteroid["y"])
    print(besteroid["detected"])
    print(set(asteroids[33]["slopes"]))
    print(asteroids[33])

    # loop
