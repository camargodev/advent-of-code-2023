import re

GAME_DIVIDER = ':'
NUMBER_SECTION_DIVIDER = '|'
NUMBER_DIVIDER = ' '

class NumberExtractor:

    def extract(self, line):
        _, numbers = line.split(GAME_DIVIDER)
        prize_numbers, my_numbers = numbers.split(NUMBER_SECTION_DIVIDER)
        return self.map_str_to_number_set(prize_numbers), self.map_str_to_number_set(my_numbers)
    
    def map_str_to_number_set(self, str_nums):
        nums_without_multiple_spaces = re.sub(r'\s{2,}', NUMBER_DIVIDER, str_nums)
        return set(nums_without_multiple_spaces.strip().split(NUMBER_DIVIDER))