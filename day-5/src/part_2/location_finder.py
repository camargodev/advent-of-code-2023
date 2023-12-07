from src.commons.mapping_entities import *
from src.commons.seed_for_location_mapper import SeedForLocationMapper
from src.commons.mapping_info_factory import MappingInfoFactory

EMPTY = ""
LINE_BREAK = "\n"
SEED = "seed"

class LowestLocationFinder:

    def __init__(self):
        self.mapping_info_factory = MappingInfoFactory()

    def find(self, lines):
        seeds_ranges = self.extract_seeds(lines)
        mapping_info_by_source = self.mapping_info_factory.make(lines)
        backtracked_mapping_info_by_source = self.mapping_info_factory.make_with_backtracking(lines)

        backtracked_range_starts = []
        for mapping_info in backtracked_mapping_info_by_source.values():
            mapping_info.sort_ranges()
            for range in mapping_info.offset_ranges:
                backtracked_offset = self.calculate_backtracked_offset(backtracked_mapping_info_by_source, mapping_info.target, range.start)
                backtracked_value = range.start + backtracked_offset
                backtracked_range_starts.append(backtracked_value)

        locations_for_valid_seeds = []
        for seed in backtracked_range_starts:
            is_valid_seed = False
            for seed_range in seeds_ranges:
                if seed in seed_range:
                    is_valid_seed = True
                    break
            if is_valid_seed:
                location = SeedForLocationMapper.map(mapping_info_by_source, seed)
                locations_for_valid_seeds.append(location)
                
        return min(locations_for_valid_seeds)
    
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
    
    def parse_mapping_info_maps(self, lines):
        mapping_info = dict()
        backtracked_mapping_info = dict()
        for raw_line in lines[1:]:
            line = raw_line.replace(LINE_BREAK, EMPTY)
            if line == EMPTY:
                last_was_empty = True
                continue
            if last_was_empty:
                last_was_empty = False
                source_type, target_type = self.get_source_and_target(line)
                mapping_info[source_type] = MappingInfo(source_type, target_type)
                backtracked_mapping_info[target_type] = MappingInfo(source_type, target_type)
                continue
            target, source, size = [int(str_num) for str_num in line.strip().split(" ")]
            offset = target - source
            start = source
            end = source + size - 1
            mapping_info[source_type].add_offset_range(OffsetRange(start, end, offset))
            backtracked_mapping_info[target_type].add_offset_range(OffsetRange(start+ offset, end+ offset, -offset))
        return mapping_info, backtracked_mapping_info

    def extract_seeds(self, lines):
        sanitized_line = lines[0].replace("seeds:", "")
        numbered_seeds = [int(str_num) for str_num in sanitized_line.strip().split(" ")]
        seeds_ranges = []
        for i in range(int(len(numbered_seeds)/2)):
            start = numbered_seeds[2*i]
            range_size = numbered_seeds[2*i+1]
            seeds_ranges.append(range(start, start+range_size-1))
        return seeds_ranges