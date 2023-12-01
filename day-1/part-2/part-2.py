import re

number_name_map = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
    "zero": "z0e",
}

def sanitize_line(line):
    for number_name, target in number_name_map.items():
        line = line.replace(number_name, target)
    return line

def day_1(input):
    sum = 0
    for line in input:
        sanitized_line = sanitize_line(line)
        numbers = re.findall('[0-9]', sanitized_line)
        value = numbers[0] + numbers[-1]
        sum += int(value)

    print(sum)

if __name__ == "__main__":
    input = open("day-1/input.txt", "r")
    day_1(input)