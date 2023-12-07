class OffsetRange:
    def __init__(self, start, end, offset):
        self.start = start
        self.end = end
        self.offset = offset
        self.range = range(start, end+1)
    
    def is_number_inside(self, number):
        return number in self.range
    
class MappingInfo:
    def __init__(self, source, target):
        self.source = source
        self.target = target
        self.offset_ranges = []
    
    def add_offset_range(self, offset_range):
        self.offset_ranges.append(offset_range)

    def sort_ranges(self):
        self.offset_ranges.sort(key=lambda range: range.start)