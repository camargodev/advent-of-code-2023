SEED = "seed"
LOCATION = "location"
EMPTY = ""
LINE_BREAK = "\n"

class OffsetRange:
    def __init__(self, start, end, offset):
        self.start = start
        self.end = end
        self.offset = offset
        self.range = range(start, end+1)
    
    def is_number_inside(self, number):
        return number in self.range
    
    def print(self):
        print("START IN", self.start, "END IN", self.end, "WITH OFFSET OF", self.offset)
    
class MappingInfo:
    def __init__(self, source, target):
        self.source = source
        self.target = target
        self.offset_ranges = []
    
    def add_offset_range(self, offset_range):
        self.offset_ranges.append(offset_range)

    def sort_ranges(self):
        self.offset_ranges.sort(key=lambda range: range.start)

    def print(self):
        print("SOURCE", self.source, "TARGET", self.target)
        for offset_range in self.offset_ranges:
            offset_range.print()

class LowestLocationFinder:

    def find(self, lines):
        seeds_ranges = self.extract_seeds(lines)
        mapping_info_by_source = dict()
        for raw_line in lines[1:]:
            line = raw_line.replace(LINE_BREAK, EMPTY)
            if line == EMPTY:
                last_was_empty = True
                continue
            if last_was_empty:
                last_was_empty = False
                source_type, target_type = self.get_source_and_target(line)
                mapping_info_by_source[source_type] = MappingInfo(source_type, target_type)
                continue
            target, source, size = [int(str_num) for str_num in line.strip().split(" ")]
            start = source
            end = source + size - 1
            offset = target - source
            mapping_info_by_source[source_type].add_offset_range(OffsetRange(start, end, offset))
        
        print("SEEDS RANGES", seeds_ranges)
        for mapping_info in mapping_info_by_source.values():
            mapping_info.sort_ranges()
            mapping_info.print()

        new_seeds = []
        for seed_range in seeds_ranges:
            new_ranges_points = []
            range_start, range_end = seed_range
            new_ranges_points.append(range_start)
            new_ranges_points.append(range_end)
            current_type = SEED
            # print(SEED, seed_range)
            while current_type != LOCATION:
                # print("SOURCE TYPE", current_type)
                mapping_info = mapping_info_by_source[current_type]
                current_type = mapping_info.target
                for offset_range in mapping_info.offset_ranges:
                    # if offset_range.end < range_start or offset_range.start > range_end:
                    #     continue
                    # if offset_range.end >= range_end and offset_range.start <= range_start:
                    #     continue
                    # print("RANGE START IN", offset_range.start, "END IN", offset_range.end)
                    if offset_range.start > range_start:
                        new_ranges_points.append(offset_range.start)
                    if offset_range.end < range_end:
                        new_ranges_points.append(offset_range.end)
                    range_start = offset_range.start
                    range_end = offset_range.end
            sorted_range_points = sorted(new_ranges_points)
            print(sorted_range_points)
            for i in range(len(sorted_range_points)-1):
                new_seeds.append(sorted_range_points[i])

        print("NEW SEEDS", new_seeds)
        seed_locations = []
        for seed in new_seeds:
            source_type = SEED
            current_value = seed
            while source_type != LOCATION:
                mapping_info = mapping_info_by_source[source_type]
                source_type = mapping_info.target
                for offset_range in mapping_info.offset_ranges:
                    if current_value in offset_range.range:
                        current_value += offset_range.offset
                        break    
            seed_locations.append(current_value)
        return min(seed_locations)
        

    def extract_seeds(self, lines):
        sanitized_line = lines[0].replace("seeds:", "")
        numbered_seeds = [int(str_num) for str_num in sanitized_line.strip().split(" ")]
        seeds_ranges = []
        for i in range(int(len(numbered_seeds)/2)):
            start = numbered_seeds[2*i]
            range_size = numbered_seeds[2*i+1]
            seeds_ranges.append((start, start+range_size-1))
        return seeds_ranges
    
    def get_source_and_target(self, line):
        sanitized_line = line.replace(" map:", "")
        source, _, target = sanitized_line.split("-")
        return source, target
