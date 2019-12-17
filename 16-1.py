def get_patt_at_step(step, num_char):
    pattern = [0, 1, 0, -1]
    pattern_to_repeat = [ele for ele in pattern for i in range(step)]
    q, r = divmod(num_char, len(pattern_to_repeat))
    r += 1  # extend by one so i can pop off the first element
    step_patt = (q * pattern_to_repeat + pattern_to_repeat[:r])[1:]
    return step_patt


def sum_product(input, pattern):
    lists = input, pattern
    return sum([x * y for x, y in zip(*lists)])


with open("16input.txt") as fp:
    input_list = [int(x) for x in list(fp.read())]
    phase = 1
    max_phase = 100
    next_input = []
    for j in range(phase, max_phase + 1):
        for step in range(1, len(input_list) + 1):
            step_patt = get_patt_at_step(step, len(input_list))
            ones_digit = abs(sum_product(input_list, step_patt)) // 1 % 10
            next_input.append(ones_digit)
        input_list = next_input
        next_input = []
    print("".join([str(x) for x in input_list[:8]]))

