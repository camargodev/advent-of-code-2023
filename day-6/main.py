from src.part_1.record_break_counter import RecordBreakCounter as FirstRecordBreakCounter
from src.part_2.record_break_counter import RecordBreakCounter as SecondRecordBreakCounter

if __name__ == "__main__":
    lines = [line for line in open("day-6/res/input.txt", "r")]
    print(FirstRecordBreakCounter().count(lines))
    print(SecondRecordBreakCounter().count(lines))