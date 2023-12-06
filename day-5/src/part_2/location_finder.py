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
        backtracked_mapping_info_by_source = self.parse_backtracking_mapping_info_by_source_type(lines)
        mapping_info_by_source = self.parse_mapping_info_by_source_type(lines)

        # print("SEEDS RANGES", seeds_ranges)
        # for mapping_info in mapping_info_by_source.values():
        #     mapping_info.sort_ranges()
        #     mapping_info.print()

        backtracked_range_starts = []
        for source_type, mapping_info in backtracked_mapping_info_by_source.items():
            mapping_info.sort_ranges()
            for range in mapping_info.offset_ranges:
                backtracked_offset = self.calculate_backtracked_offset(backtracked_mapping_info_by_source, mapping_info.target, range.start)
                backtracked_value = range.start + backtracked_offset
                backtracked_range_starts.append(backtracked_value)
                # print(source_type, ": FOR VALUE", range.start, "BACKTRACKS TO ", backtracked_value, "-> OFFSET OF", backtracked_offset)

        locations_for_valid_seeds = []
        for seed in backtracked_range_starts:
            is_valid_seed = False
            for seed_range in seeds_ranges:
                if seed in seed_range:
                    is_valid_seed = True
                    break
            if is_valid_seed:
                location = self.find_location_for_seed(mapping_info_by_source, seed)
                locations_for_valid_seeds.append(location)
                
        return min(locations_for_valid_seeds)
    
    def find_location_for_seed(self, mapping_info_by_source,  seed):
        source_type = SEED
        current_value = seed
        while source_type != LOCATION:
            mapping_info = mapping_info_by_source[source_type]
            for offset_range in mapping_info.offset_ranges:
                if current_value in offset_range.range:
                    current_value += offset_range.offset
                    break    
            source_type = mapping_info.target
        return current_value
    
    def calculate_backtracked_offset(self, mapping_info_by_source, current_type, value):
        backtrack_target = current_type
        backtrack_offset = 0
        current_value = value
        while backtrack_target != SEED:
            mapping_info = mapping_info_by_source[backtrack_target]
            for backtrack_offset_range in mapping_info.offset_ranges:
                if backtrack_offset_range.is_number_inside(current_value):
                    current_value += backtrack_offset_range.offset
                    backtrack_offset += backtrack_offset_range.offset
                    break
            backtrack_target = mapping_info.source
        return backtrack_offset
    
    def parse_mapping_info_by_source_type(self, lines):
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
        return mapping_info_by_source
    
    def parse_backtracking_mapping_info_by_source_type(self, lines):
        mapping_info_by_source = dict()
        for raw_line in lines[1:]:
            line = raw_line.replace(LINE_BREAK, EMPTY)
            if line == EMPTY:
                last_was_empty = True
                continue
            if last_was_empty:
                last_was_empty = False
                source_type, target_type = self.get_source_and_target(line)
                mapping_info_by_source[target_type] = MappingInfo(source_type, target_type)
                continue
            target, source, size = [int(str_num) for str_num in line.strip().split(" ")]
            offset = target - source
            start = source + offset
            end = source + size + offset- 1
            mapping_info_by_source[target_type].add_offset_range(OffsetRange(start, end, -offset))
        return mapping_info_by_source

    def extract_seeds(self, lines):
        sanitized_line = lines[0].replace("seeds:", "")
        numbered_seeds = [int(str_num) for str_num in sanitized_line.strip().split(" ")]
        seeds_ranges = []
        for i in range(int(len(numbered_seeds)/2)):
            start = numbered_seeds[2*i]
            range_size = numbered_seeds[2*i+1]
            seeds_ranges.append(range(start, start+range_size-1))
        return seeds_ranges
    
    def get_source_and_target(self, line):
        sanitized_line = line.replace(" map:", "")
        source, _, target = sanitized_line.split("-")
        return source, target
