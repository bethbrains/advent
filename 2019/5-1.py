def process(memory):
    i = 0
    while True:
        instruction = memory[i]
        opcode = instruction % 100

        if opcode == 99:
            print("HALT")
            return
        elif opcode == 3:
            # input
            in_val = input()
            memory[memory[i + 1]] = int(in_val)
            i = i + 2
        elif opcode == 4:
            # output
            print(memory[memory[i + 1]])
            i = i + 2
        else:

            mode1, mode2 = 0,0
            if instruction > 99:
                paramnum = (instruction - opcode) // 100
                params = [int(x) for x in str(paramnum)]
                mode1 = params[-1]
                if len(params) > 1:
                    mode2 = params[-2]

            param1 = memory[i + 1] if mode1 == 1 else memory[memory[i+1]]
            param2 = memory[i + 2] if mode2 == 1 else memory[memory[i+2]]

            if opcode == 1:
                # add
                memory[memory[i + 3]] = param1 + param2
                i = i + 4
            elif opcode == 2:
                # multiply
                memory[memory[i + 3]] = param1 * param2
                i = i + 4


with open("5input.txt") as fp:
    input_data = list(map(int, fp.read().split(",")))
    process(input_data)
