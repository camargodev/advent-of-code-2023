from src.part_1.oasis_protector import OasisProtector as FirstOasisProtector
from src.part_2.oasis_protector import OasisProtector as SecondOasisProtector


if __name__ == "__main__":
    lines = [line for line in open("day_9/res/input.txt", "r")]
    print(FirstOasisProtector().predict_values_to_save_oasis(lines))
    print(SecondOasisProtector().predict_values_to_save_oasis(lines))

