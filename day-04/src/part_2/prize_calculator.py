from src.commons.number_extractor import NumberExtractor

class PrizeCalculator:
    def __init__(self):
        self.number_extractor = NumberExtractor()

    def calculate(self, lines):
        units_by_card = dict()
        num_cards = len(lines)
        for index in range(num_cards):
            units_by_card[index+1] = 1
        for card_index in range(num_cards):
            numbers_of_current_card = units_by_card[card_index+1]
            prize_numbers, my_numbers = self.number_extractor.extract(lines[card_index])
            my_prized_numbers = prize_numbers.intersection(my_numbers)
            prize_size = len(my_prized_numbers)
            for prize_index in range(prize_size):
                prized_card_index = card_index + prize_index + 1
                units_by_card[prized_card_index+1] += numbers_of_current_card

        return sum(units_by_card.values())
