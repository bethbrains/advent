import math

total = 0

def get_module_fuel (total, input):
    fuel = math.floor(input / 3) - 2
    if (fuel > 0):
        return get_module_fuel(total + fuel, fuel)
    else:
        return total

with open('input.txt') as fp:
    for module in fp:
        module_fuel = get_module_fuel(0, int(module))
        total = total + module_fuel

print(total)