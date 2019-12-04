def check_num(num):
    digits = [int(x) for x in str(num)]
    double_count = 0
    i = 0
    digit_count = 1
    while i < len(digits) - 1:
        if digits[i] == digits[i + 1]:
            digit_count += 1
            if digit_count == 2:
                double_count += 1
            elif digit_count == 3:
                double_count -= 1
        else:
            digit_count = 1
        if not digits[i] <= digits[i + 1]:
            return False
        i = i + 1
    return double_count > 0


with open("4input.txt") as fp:
    poss_passwords = []
    input = list(map(int, fp.read().split("-")))
    for num in range(input[0], input[1] + 1):
        if check_num(num):
            poss_passwords.append(num)
    print(len(poss_passwords))
