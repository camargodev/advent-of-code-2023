from src.commons.base_instructions_extractor import BaseInstructionsExtractor

DIRECTION = {0: "R", 1: "D", 2: "L", 3: "U"}

class InstructionsExtractor(BaseInstructionsExtractor):
    def extract(self, lines):
        instructions = []
        for line in lines:
            _, _, hex_instruction = line.split(" ")
            instruction = hex_instruction.replace("(#", "").replace(")", "")
            hex_number, hex_dir = instruction[:-1], instruction[-1] 
            direction = DIRECTION[int(hex_dir)]
            steps = int(hex_number, 16)
            instructions.append((direction, steps))
        return instructions