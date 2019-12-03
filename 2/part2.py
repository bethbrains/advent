def process (input):
    i = 0

    for noun in range(0,99):
        for verb in range(0,99):
            memory = list(input)
            memory[1] = noun
            memory[2] = verb

            i = 0
            while True:
                opcode = memory[i]
                if opcode == 99:
                    print(f"{noun} {verb} {memory[0]}")
                    if memory[0] == 19690720:
                        return f"SOLUTION: {(100 * noun) + verb}"
                elif opcode == 1:
                    # add
                    memory[memory[i+3]] = memory[memory[i+1]] + memory[memory[i+2]]
                elif opcode == 2:
                    # multiply
                    memory[memory[i+3]] = memory[memory[i+1]] * memory[memory[i+2]]
                i = i + 4


with open('2/input.txt') as fp:
    print(process(list(map(int,fp.read().split(",")))))
