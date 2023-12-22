from src.commons.cube_game_parser import CubeGameParser

MAX_PIECES_BY_COLOR = {
    "red": 12,
    "green": 13,
    "blue": 14
}
class CubeGamePlayer:

    def __init__(self):
        self.game_parser = CubeGameParser()

    def play(self, input):
        sum_ids = 0
        for line in input:
            game_id, results_by_color = self.game_parser.parse(line)
            if self.is_game_valid(results_by_color):
                sum_ids += game_id
        return sum_ids


    def is_game_valid(self, results_by_color):
        for color, results in results_by_color.items():
            if MAX_PIECES_BY_COLOR[color] < max(results):
                return False
        return True