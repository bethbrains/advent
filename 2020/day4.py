import re


def check_birth_year(person):
    if not "byr" in person.keys():
        return False
    year = person["byr"]
    return len(year) == 4 and 1920 <= int(year) <= 2002


def check_issue_year(person):
    if not "iyr" in person.keys():
        return False
    year = person["iyr"]
    return len(year) == 4 and 2010 <= int(year) <= 2020


def check_exp_year(person):
    if not "eyr" in person.keys():
        return False
    year = person["eyr"]
    return len(year) == 4 and 2020 <= int(year) <= 2030


def check_height(person):
    if not "hgt" in person.keys():
        return False
    hgt = person["hgt"]
    unit = hgt[-2:]
    num = hgt[:-2]
    if unit == "cm":
        return 150 <= int(num) <= 193
    elif unit == "in":
        return 59 <= int(num) <= 76


def check_hair(person):
    if not "hcl" in person.keys():
        return False
    allowed = "abcdef0123456789"
    hcl = person["hcl"]
    return (
        hcl[0] == "#"
        and len(hcl[1:]) == 6
        and len([letter for letter in hcl[1:] if letter in allowed]) == 6
    )


def check_eyes(person):
    if not "ecl" in person.keys():
        return False
    return person["ecl"] in "amb,blu,brn,gry,grn,hzl,oth".split(",")


def is_valid(data):
    data_points = data.split(" ")
    person_info = {
        key: value for [key, value] in [data.split(":") for data in data_points if data]
    }

    return (
        check_eyes(person_info)
        and check_hair(person_info)
        and check_birth_year(person_info)
        and check_issue_year(person_info)
        and check_exp_year(person_info)
        and check_height(person_info)
        and ("pid" in person_info.keys() and len(person_info["pid"]) == 9)
        and (
            len(person_info.keys()) == 8
            or ("cid" not in person_info.keys() and len(person_info.keys()) == 7)
        )
    )


def part_one():
    valid_count = 0
    with open("4input.txt") as fp:
        fp = [line.replace("\n", " ") for line in fp.read().split("\n\n")]
        for passport in fp:
            valid_count += 1 if is_valid(passport) else 0
    return valid_count


if __name__ == "__main__":
    print(part_one())
