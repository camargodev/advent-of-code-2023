from src.commons.entities import *

SEED = "seed"
LOCATION = "location"
EMPTY = ""
LINE_BREAK = "\n"

class LowestLocationFinder:

    def find(self, lines):
        seeds = self.extract_seeds(lines)

        mapping_info = dict()
        for raw_line in lines[1:]:
            line = raw_line.replace(LINE_BREAK, EMPTY)
            if line == EMPTY:
                last_was_empty = True
                continue
            if last_was_empty:
                last_was_empty = False
                source_type, target_type = self.get_source_and_target(line)
                mapping_info[source_type] = MappingInfo(source_type, target_type)
                continue
            target, source, size = [int(str_num) for str_num in line.strip().split(" ")]
            offset = target - source
            start = source
            end = source + size - 1
            mapping_info[source_type].add_offset_range(OffsetRange(start, end, offset))
            

        seed_locations = []
        for seed in seeds:
            location = self.find_location_for_seed(mapping_info, seed)
            seed_locations.append(location)

        return min(seed_locations)
    
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

    def extract_seeds(self, lines):
        sanitized_line = lines[0].replace("seeds:", "")
        return [int(str_num) for str_num in sanitized_line.strip().split(" ")]
    
    def get_source_and_target(self, line):
        sanitized_line = line.replace(" map:", "")
        source, _, target = sanitized_line.split("-")
        return source, target
