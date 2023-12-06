SEED = "seed"
LOCATION = "location"
EMPTY = ""
LINE_BREAK = "\n"

class LowestLocationFinder:

    def find(self, lines):
        seeds = self.extract_seeds(lines)
        all_mappings = dict()
        last_was_empty = False
        mappings_for_source = []
        for raw_line in lines[1:]:
            line = raw_line.replace(LINE_BREAK, EMPTY)
            if line == EMPTY:
                last_was_empty = True
                continue
            if last_was_empty:
                last_was_empty = False
                source_type, target_type = self.get_source_and_target(line)
                mappings_for_source = []
                all_mappings[source_type] = (target_type, mappings_for_source)
                continue
            target, source, size = [int(str_num) for str_num in line.strip().split(" ")]
            offset = target - source
            mappings_for_source.append((range(source, source+size), offset))

        seed_locations = []
        for seed in seeds:
            source_type = SEED
            current_value = seed
            while source_type != LOCATION:
                source_type, mappings_for_type = all_mappings[source_type]
                for mapping_for_type in mappings_for_type:
                    mapping_range, offset = mapping_for_type
                    if current_value in mapping_range:
                        current_value += offset
                        break    
            seed_locations.append(current_value)

        return min(seed_locations)

    def extract_seeds(self, lines):
        sanitized_line = lines[0].replace("seeds:", "")
        return [int(str_num) for str_num in sanitized_line.strip().split(" ")]
    
    def get_source_and_target(self, line):
        sanitized_line = line.replace(" map:", "")
        source, _, target = sanitized_line.split("-")
        return source, target
