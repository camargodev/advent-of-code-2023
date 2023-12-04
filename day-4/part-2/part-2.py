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
    units_by_card = dict()
    num_cards = len(lines)
    for index in range(num_cards):
        units_by_card[index+1] = 1
    for card_index in range(num_cards):
        numbers_of_current_card = units_by_card[card_index+1]
        prize_numbers, my_numbers = extract_numbers(lines[card_index])
        my_prized_numbers = prize_numbers.intersection(my_numbers)
        prize_size = len(my_prized_numbers)
        for prize_index in range(prize_size):
            prized_card_index = card_index + prize_index + 1
            if prized_card_index == len(lines):
                break
            units_by_card[prized_card_index+1] += numbers_of_current_card

    total_sum = sum(units_by_card.values())

    print(total_sum)


if __name__ == "__main__":
    input = open("day-4/input.txt", "r")
    lines = [line for line in input]
    day_4(lines)