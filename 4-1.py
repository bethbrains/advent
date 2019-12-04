def check_num(num):
    digits = [int(x) for x in str(num)]
    has_double = False
    i = 0
    while i < len(digits) - 1:
        if digits[i] == digits[i + 1]:
            has_double = True
        if not digits[i] <= digits[i + 1]:
            return False
        i = i + 1
    return has_double


with open("4input.txt") as fp:
    poss_passwords = []
    input = list(map(int, fp.read().split("-")))
    for num in range(input[0], input[1] + 1):
        if check_num(num):
            poss_passwords.append(num)
    print(len(poss_passwords))
