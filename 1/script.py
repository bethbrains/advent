import math

total = 0

def getValue (input):
    return math.floor(input / 3) - 2

with open('input.txt') as fp:
    for line in fp:
        value = getValue(int(line))
        total = total + value

print(total)