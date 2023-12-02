import re

def day_1(input):
    sum = 0
    for line in input:
        numbers = re.findall('[0-9]', line)
        value = numbers[0] + numbers[-1]
        sum += int(value)

    print(sum)

if __name__ == "__main__":
    input = open("day-1/part-1/example.txt", "r")
    day_1(input)