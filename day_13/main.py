from src.commons.mirror_finder import MirrorFinder
if __name__ == "__main__":
    lines = [line for line in open("day_13/res/input.txt", "r")]
    print(MirrorFinder().find(lines, allowed_diffences=0))
    print(MirrorFinder().find(lines, allowed_diffences=1))
