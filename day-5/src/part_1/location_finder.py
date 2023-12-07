from src.commons.mapping_entities import *
from src.commons.seed_for_location_mapper import SeedForLocationMapper
from src.commons.mapping_info_factory import MappingInfoFactory

class LowestLocationFinder:

    def __init__(self):
        self.mapping_info_factory = MappingInfoFactory()

    def find(self, lines):
        seeds = self.extract_seeds(lines)

        mapping_info_by_source = self.mapping_info_factory.make(lines)            

        seed_locations = []
        for seed in seeds:
            seed_locations.append(SeedForLocationMapper.map(mapping_info_by_source, seed))

        return min(seed_locations)

    def extract_seeds(self, lines):
        sanitized_line = lines[0].replace("seeds:", "")
        return [int(str_num) for str_num in sanitized_line.strip().split(" ")]
