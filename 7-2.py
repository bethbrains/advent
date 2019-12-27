import itertools




def process(memory, pc, phase_setting, input_val, outputs):
    i = pc
    given_phase_setting = False
    while True:
        instruction = memory[i]
        opcode = instruction % 100
        print(i)
        print(opcode)

        if opcode == 99:
            return opcode
        elif opcode == 3:
            # input
            if phase_setting is not None and input_val is not None:
                if not given_phase_setting:
                    memory[memory[i + 1]] = phase_setting
                    given_phase_setting = True
                else:
                    memory[memory[i + 1]] = input_val
            else:
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
                outputs.append(param1value)
                i = i + 2
                return opcode, i


with open("7input.txt") as fp:
    input_data = list(map(int, fp.read().split(",")))
    feedback_phase_settings = [5,6,7,8,9]
    feedback_phase_setting_combos = list(itertools.permutations(feedback_phase_settings,5))
    max_output = 0
    pcs = [0,0,0,0,0]
    for combo in [(9, 8, 7, 6, 5)]: # this is just from the test; set it back to in feedback_phase_setting_combos
        computers = []
        outputs = []
        for i in range(5):
            outputs.append([])
        # outputs[0].append(73)
        print(outputs)
        for i in range(0,5):
            computers.append(list(input_data)) # confirmed this gives 5 unique memory lists -- append does deep copy, not reference.
        input_val = 0
        done = False
        while not done:
            for index in range(len(combo)):
                print("computer: {}".format(index))
                opcode, pc = process(computers[index], pcs[index], combo[index], input_val, outputs[index])
                pcs[index] = pc
                input_val = outputs[index][-1]
                if input_val == 139629729:
                    print('got it')
                    print(opcode)
                    print(outputs)
                if opcode == 99:
                    print(outputs)
                    print('halt')
                    done = True
                    break
        max_output = input_val if input_val > max_output else max_output
    print(max_output)
