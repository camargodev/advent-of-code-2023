from src.part_1.winning_calculator import WinningCalculator as FirstWinningCalculator

if __name__ == "__main__":
    lines = [line for line in open("day-7/res/input.txt", "r")]
    print(FirstWinningCalculator().calculate(lines))