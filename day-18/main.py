from src.commons.lava_area_calculator import LavaAreaCalculator
from src.part_1.instruction_extractor import InstructionsExtractor
from src.part_2.instruction_extractor import InstructionsExtractor as HexInstructionsExtractor

if __name__ == "__main__":
    lines = [line.replace("\n","") for line in open("day-18/res/input.txt", "r")]
    print(LavaAreaCalculator(InstructionsExtractor()).calculate(lines))
    print(LavaAreaCalculator(HexInstructionsExtractor()).calculate(lines))