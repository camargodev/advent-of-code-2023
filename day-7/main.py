from src.part_1.simple_bet_manager import SimpleBetManager as FirstBetManager
from src.part_2.bet_with_joker_manager import BetWithJokerManager as SecondBetManager
from src.bet_winnings_calculator import WinningCalculator

def print_result(result, expected):
    print(result)
    print("CORRECT" if result == expected else "WRONG")

if __name__ == "__main__":
    lines = [line for line in open("day-7/res/input.txt", "r")]
    print_result(WinningCalculator(FirstBetManager()).calculate(lines), 249748283)
    print_result(WinningCalculator(SecondBetManager()).calculate(lines), 248029057)

