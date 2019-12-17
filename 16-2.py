def sum_product(input, pattern):
    lists = input, pattern
    return sum([x * y for x, y in zip(*lists)])


with open("16input.txt") as fp:
    input_list = [int(x) for x in list(fp.read())] * 10000
    phase = 1
    max_phase = 4
    length = len(input_list)
    offset = input_list[:7]
    pattern = [0, 1, 0, -1]
    next_input = []
    patterns_by_step = {}
    for step in range(1, len(input_list) + 1):
        print(step)
        # patterns_by_step[step] = [pattern[(x+1) // step % 4] for x in range(len(input_list))]
    print(patterns_by_step)
    for j in range(phase, max_phase + 1):
        print('new phase: ' + str(j))
        for step in range(1, len(input_list) + 1):
            # patt_for_step = patterns_by_step[step]
            sumprod = sum(x * pattern[(x+1) // step % 4] for x in input_list)
            ones_digit = abs(sumprod) // 1 % 10
            next_input.append(ones_digit)
        input_list = next_input
        next_input = []
    print("".join([str(x) for x in input_list[offset:8]]))