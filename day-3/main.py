from commons.part_1.engine import Engine as FirstEngine
from commons.part_2.engine import Engine as SecondEngine

if __name__ == "__main__":
    lines = [line for line in open("day-3/res/input.txt", "r")]
    print(FirstEngine().run(lines))
    print(SecondEngine().run(lines))