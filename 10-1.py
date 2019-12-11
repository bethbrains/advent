import fractions


def get_slope(a, b):
    rise = b["y"] - a["y"]
    run = b["x"] - a["x"]
    quad = 0
    if rise < 0 and run < 0:
        quad = 4
    elif rise < 0 and run >= 0:
        quad = 1
    elif rise >= 0 and run < 0 :
        quad = 3
    elif rise >= 0 and run >= 0:
        quad = 2
    if run == 0:
        slope = 'und', quad
    else:
        slope = fractions.Fraction(rise, run), quad
    return slope

# order the slopes


def detect_asteroids(asteroids):
    for a in asteroids:
        a["detected"] = 0
        slopes = []
        for b in asteroids:
            if a is not b:
                slopes.append(get_slope(a, b))
        #a["slopes"] = slopes
        a["detected"] = len(set(slopes))
    return asteroids


def parse_map(fp):
    asteroids = []
    for line_num, line in enumerate(fp, 0):
        for char_num, character in enumerate(line, 0):
            if character == "#":
                asteroids.append({"x": char_num, "y": line_num})
    return asteroids


with open("10input.txt") as fp:
    asteroids = detect_asteroids(parse_map(fp))
    print(asteroids)
    besteroid = asteroids[0]
    for asteroid in asteroids:
        if asteroid["detected"] > besteroid["detected"]:
            besteroid = asteroid
    print(besteroid["x"])
    print(besteroid["y"])
    print(besteroid["detected"])
    #print(set(asteroids[33]["slopes"]))
    #print(asteroids[33])

    # loop
