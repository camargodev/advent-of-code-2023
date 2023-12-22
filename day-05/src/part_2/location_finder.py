from src.commons.mapping_entities import *
from src.commons.seed_for_location_mapper import SeedForLocationMapper
from src.commons.mapping_info_factory import MappingInfoFactory

SEED = "seed"

class LowestLocationFinder:

    def __init__(self):
        self.mapping_info_factory = MappingInfoFactory()

    def find(self, lines):
        seeds_ranges = self.extract_seeds(lines)
        mapping_info_by_source = self.mapping_info_factory.make(lines)
        backtracked_mapping_info_by_source = self.mapping_info_factory.make_with_backtracking(lines)

        backtracked_range_starts = self.calculate_new_seed_ranges(seeds_ranges, backtracked_mapping_info_by_source)

        locations_for_valid_seeds = []
        for seed in backtracked_range_starts:
            locations_for_valid_seeds.append(SeedForLocationMapper.map(mapping_info_by_source, seed))
                
        return min(locations_for_valid_seeds)
    
    def calculate_new_seed_ranges(self, seeds_ranges, backtracked_mapping_info_by_source):
        backtracked_range_starts = []
        for mapping_info in backtracked_mapping_info_by_source.values():
            mapping_info.sort_ranges()
            for range in mapping_info.offset_ranges:
                backtracked_offset = self.calculate_backtracked_offset(backtracked_mapping_info_by_source, mapping_info.target, range.start)
                backtracked_value = range.start + backtracked_offset
                for seed_range in seeds_ranges:
                    if backtracked_value in seed_range:
                        backtracked_range_starts.append(backtracked_value)
                        break
        return backtracked_range_starts
    
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

    def extract_seeds(self, lines):
        sanitized_line = lines[0].replace("seeds:", "")
        numbered_seeds = [int(str_num) for str_num in sanitized_line.strip().split(" ")]
        seeds_ranges = []
        for i in range(int(len(numbered_seeds)/2)):
            start = numbered_seeds[2*i]
            range_size = numbered_seeds[2*i+1]
            seeds_ranges.append(range(start, start+range_size-1))
        return seeds_ranges