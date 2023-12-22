from src.part_1.simple_bet_manager import SimpleBetManager as FirstBetManager
from src.part_2.bet_with_joker_manager import BetWithJokerManager as SecondBetManager
from src.bet_winnings_calculator import WinningCalculator


if __name__ == "__main__":
    lines = [line for line in open("day_7/res/input.txt", "r")]
    print(WinningCalculator(FirstBetManager()).calculate(lines))
    print(WinningCalculator(SecondBetManager()).calculate(lines))

