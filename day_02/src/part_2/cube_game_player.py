import math
from src.commons.cube_game_parser import CubeGameParser

class CubeGamePlayer:

    def __init__(self):
        self.game_parser = CubeGameParser()

    def play(self, input):
        sum_products = 0
        for line in input:
            _, results_by_color = self.game_parser.parse(line)
            sum_products += self.calculate_min_product(results_by_color)
        return sum_products

    def calculate_min_product(self, results_by_color):
        return math.prod([max(results) for results in results_by_color.values()])