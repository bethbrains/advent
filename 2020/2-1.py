import re

def main():
    valid_count = 0
    with open('2input.txt') as fp:
        for line in fp:
            bits = re.split(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', line)
            min = int(bits[1])
            max = int(bits[2])
            letter = bits[3]
            pw = bits[4]
            count = 0
            for char in pw:
                if char == letter:
                    count += 1
            if min <= count <= max:
                valid_count += 1
    print(valid_count)

def part_two():
    valid_count = 0
    with open('2input.txt') as fp:
        for line in fp:
            bits = re.split(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', line)
            ind1 = int(bits[1]) - 1
            ind2 = int(bits[2]) - 1
            letter = bits[3]
            pw = bits[4]
            count = 0
            if pw[ind1] == letter:
                count += 1
            if pw[ind2] == letter:
                count += 1
            if count == 1:
                valid_count += 1
    print(valid_count)

if __name__ == "__main__":
    main()
    part_two()
