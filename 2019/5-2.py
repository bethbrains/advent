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
        else:
            mode1, mode2 = 0, 0
            if instruction > 99:
                paramnum = (instruction - opcode) // 100
                params = [int(x) for x in str(paramnum)]
                mode1 = params[-1]
                if len(params) > 1:
                    mode2 = params[-2]
            param1value = memory[i + 1] if mode1 == 1 else memory[memory[i + 1]]
            if opcode != 4:
                param2value = memory[i + 2] if mode2 == 1 else memory[memory[i + 2]]

            if opcode == 1:
                # add
                memory[memory[i + 3]] = param1value + param2value
                i += 4
            elif opcode == 2:
                # multiply
                memory[memory[i + 3]] = param1value * param2value
                i += 4
            elif opcode == 5:
                # Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
                if param1value != 0:
                    i = param2value
                else:
                    i += 3
            elif opcode == 6:
                # Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
                if param1value == 0:
                    i = param2value
                else:
                    i += 3
            elif opcode == 7:
                # Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
                if param1value < param2value:
                    memory[memory[i + 3]] = 1
                else:
                    memory[memory[i + 3]] = 0
                i += 4
            elif opcode == 8:
                # Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
                if param1value == param2value:
                    memory[memory[i + 3]] = 1
                else:
                    memory[memory[i + 3]] = 0
                i += 4
            elif opcode == 4:
                # output
                print("CODE: " + str(param1value))
                i = i + 2


with open("5input.txt") as fp:
    input_data = list(map(int, fp.read().split(",")))
    process(input_data)
