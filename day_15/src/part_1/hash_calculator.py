from src.commons.hash_mapper import HashMapper

class HashCalculator:
    def calculate(self, line):
        words = line.split(",")
        return sum([HashMapper.map(word) for word in words])
