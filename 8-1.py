import math

with open("8input.txt") as input:
    input = input.read()
    width = 3
    height = 2
    area = height * width
    length = len(input)
    layer = 0
    pixels = {}
    for i in range(1, length):
        print(i)
        print(input[i - 1])
        col = width if i % width == 0 else i % width
        print(f"col: {str(col)}")
        row = math.ceil(i / width)
        print(f"row: {str(row)}")
        layer = math.ceil(i / area)
        print(f"layer: {str(layer)}")
        pixels[i] = {"p": input[i - 1], "row": row, "col": col, "layer": layer}
    print(pixels)
    print(len[x for x in pixels if x['layer'] == 2])
