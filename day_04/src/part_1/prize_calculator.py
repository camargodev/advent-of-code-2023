from src.commons.number_extractor import NumberExtractor

class PrizeCalculator:
    def __init__(self):
        self.number_extractor = NumberExtractor()

    def calculate(self, lines):
        total_sum = 0
        for line in lines:
            prize_numbers, my_numbers = self.number_extractor.extract(line)
            my_prized_numbers = prize_numbers.intersection(my_numbers)
            prize_size = len(my_prized_numbers)
            if prize_size == 0:
                continue
            prize_value = pow(2, prize_size-1)
            total_sum += prize_value
        return total_sum
