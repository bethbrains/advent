def process (input):
    i = 0
    while True:
        opcode = int(input[i])
        if opcode == 99:
            return input
        elif opcode == 1:
            # add
            input[input[i+3]] = input[input[i+1]] + input[input[i+2]]
        elif opcode == 2:
            # multiply
            input[input[i+3]] = input[input[i+1]] * input[input[i+2]]
        i = i + 4


with open('input.txt') as fp:
    input = list(map(int,fp.read().split(",")))
    input[1] = 12
    input[2] = 2
    print(input)
    output = process(input)
    print(output[0])
