import itertools
import numpy

def part_two():
    with open('1input.txt') as fp:
        numbers = [int(line) for line in fp]
        numbers.sort(reverse=True)
        for triplet in itertools.combinations(numbers, 3):
            if sum(triplet) == 2020:
                # return list(triplet)
                print(list(triplet))
                return numpy.prod(triplet)
        return []

def main():
    total = 0
    with open('1input.txt') as fp:
        numbers = [int(line) for line in fp]
        numbers.sort();
        start_index = 0
        end_index = -1
        target = 2020
        result = 0
        while not result == target:
            start = numbers[start_index]
            end = numbers[end_index]
            result = start + end
            if result > target:
                end_index -= 1
            elif result < target:
                start_index += 1
            else:
                print(start)
                print(end)
                print(result)
                print(start * end)

if __name__ == "__main__":
    print(part_two())
    # main()
