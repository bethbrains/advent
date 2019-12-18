with open("16input.txt") as fp:
    input = [int(x) for x in list(fp.read())] * 10000
    phase = 1
    max_phase = 4
    length = len(input)
    offset = int("".join([str(x) for x in input[:7]]))
    print(offset)
    pattern = [0, 1, 0, -1]
    next_input = []
    for j in range(phase, max_phase + 1):
        print('new phase: ' + str(j))
        for row in range(1, len(input) + 1):
            print('ROW' + str(row))
            # print(input)

            sumprod = 0

            start_add_slice = row-1

            if row > length // 2:
                sumprod = sum(input[start_add_slice:])
            else:
                start_sub_slice = row * 3 - 1

                while start_add_slice < length:
                    # print('ADDING')
                    # print(sum(input[start_slice:start_slice + row]))
                    sumprod += sum(input[start_add_slice:start_add_slice + row])
                    start_add_slice += (row * 4)

                    if row < length // 4:
                        # print('SUBTRACTING')
                        # print(sum(input[start_slice:start_slice + row]))
                        sumprod -= sum(input[start_sub_slice:start_sub_slice + row])
                        start_sub_slice += row * 4

            # print(sumprod)
            ones_digit = abs(sumprod) // 1 % 10
            # print(ones_digit)
            next_input.append(ones_digit)
        # print(next_input)
        input = next_input
        next_input = []
    print("".join([str(x) for x in input[offset:8]]))