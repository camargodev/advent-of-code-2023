from src.part_1.prize_calculator import PrizeCalculator as FirstPrizeCalculator
from src.part_2.prize_calculator import PrizeCalculator as SecondPrizeCalculator

if __name__ == "__main__":
    lines = [line for line in open("day_4/res/input.txt", "r")]
    print(FirstPrizeCalculator().calculate(lines))
    print(SecondPrizeCalculator().calculate(lines))