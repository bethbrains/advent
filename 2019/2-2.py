def process (memory):
    i = 0
    while True:
        opcode = memory[i]
        if opcode == 99:
            return memory
        elif opcode == 1:
            # add
            memory[memory[i+3]] = memory[memory[i+1]] + memory[memory[i+2]]
        elif opcode == 2:
            # multiply
            memory[memory[i+3]] = memory[memory[i+1]] * memory[memory[i+2]]
        i = i + 4


with open('2input.txt') as fp:
    input = list(map(int,fp.read().split(",")))
    for noun in range(0,100):
        for verb in range(0,100):
            input[1] = noun
            input[2] = verb
            output = process(list(input))[0]
            if output == 19690720:
                print(f"SOLUTION: {(100 * noun) + verb}")