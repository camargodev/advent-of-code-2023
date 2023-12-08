from src.part_1.trebuchet_calibrator import TrebuchetCalibrator as FirstTrebuchetCalibrator
from src.part_2.trebuchet_calibrator import TrebuchetCalibrator as SecondTrebuchetCalibrator

if __name__ == "__main__":
    lines = [line for line in open("day-1/res/input.txt", "r")]
    print(FirstTrebuchetCalibrator().calibrate(lines))
    print(SecondTrebuchetCalibrator().calibrate(lines))