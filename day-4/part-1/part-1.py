import re

GAME_DIVIDER = ':'
NUMBER_SECTION_DIVIDER = '|'
NUMBER_DIVIDER = ' '

def map_str_to_number_set(str_nums):
    nums_without_multiple_spaces = re.sub(r'\s{2,}', NUMBER_DIVIDER, str_nums)
    return set(nums_without_multiple_spaces.strip().split(NUMBER_DIVIDER))

def extract_numbers(line):
    _, numbers = line.split(GAME_DIVIDER)
    prize_numbers, my_numbers = numbers.split(NUMBER_SECTION_DIVIDER)
    return map_str_to_number_set(prize_numbers), map_str_to_number_set(my_numbers)

def day_4(lines):
    total_sum = 0
    for line in lines:
        prize_numbers, my_numbers = extract_numbers(line)
        my_prized_numbers = prize_numbers.intersection(my_numbers)
        prize_size = len(my_prized_numbers)
        if prize_size == 0:
            continue
        prize_value = pow(2, prize_size-1)
        total_sum += prize_value
    print(total_sum)


if __name__ == "__main__":
    input = open("day-4/input.txt", "r")
    lines = [line for line in input]
    day_4(lines)