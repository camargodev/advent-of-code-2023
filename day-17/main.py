from src.part_1.best_path_finder import BestPathFinder as FirstBestPathFinder

if __name__ == "__main__":
    lines = [line.replace("\n","") for line in open("day-17/res/input.txt", "r")]
    print(FirstBestPathFinder().find(lines))