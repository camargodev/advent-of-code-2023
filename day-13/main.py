from src.part_1.mirror_finder import MirrorFinder as FirstMirrorFinder
from src.part_2.mirror_finder import MirrorFinder as SecondMirrorFinder

if __name__ == "__main__":
    lines = [line for line in open("day-13/res/debug.txt", "r")]
    # print(FirstMirrorFinder().find(lines))
    print(SecondMirrorFinder().find(lines))
