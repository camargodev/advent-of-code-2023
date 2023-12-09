SEED = "seed"
LOCATION = "location"

class SeedForLocationMapper:
    @staticmethod
    def map(mapping_info_by_source,  seed):
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