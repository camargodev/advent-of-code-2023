from src.part_1.winning_calculator import WinningCalculator as FirstWinningCalculator
from src.part_2.winning_calculator import WinningCalculator as SecondWinningCalculator

def print_result(result, expected):
    print(result)
    print("CORRECT" if result == expected else "WRONG")

if __name__ == "__main__":
    lines = [line for line in open("day-7/res/input.txt", "r")]
    print_result(FirstWinningCalculator().calculate(lines), 249748283)
    print_result(SecondWinningCalculator().calculate(lines), 248029057)

