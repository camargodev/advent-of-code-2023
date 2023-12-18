from src.commons.base_instructions_extractor import BaseInstructionsExtractor

class InstructionsExtractor(BaseInstructionsExtractor):
    def extract(self, lines):
        instructions = []
        for line in lines:
            direction, steps, _ = line.split(" ")
            instructions.append((direction, int(steps)))
        return instructions