MISTERY = "?"

class InputExtractor:
    def extract_with_repetition(self, lines, additional_repeats):
        return self.extract(lines, additional_repeats)
    
    def extract(self, lines, additional_repeats=0):
        springs = []
        for line in lines:
            pattern, str_numbers = line.split(" ")
            numbers = [int(str_num) for str_num in str_numbers.split(",")]
            springs.append((self.repeat_pattern(pattern, additional_repeats), self.repeat_numbers(numbers, additional_repeats)))
        return springs
    
    def repeat_pattern(self, pattern, additional_repeats):
        repeated_pattern = pattern
        for _ in range(additional_repeats):
            repeated_pattern += MISTERY + pattern
        return repeated_pattern
    
    def repeat_numbers(self, numbers, additional_repeats):
        repeated_numbers = []
        for _ in range(additional_repeats+1):
            repeated_numbers.extend(numbers)
        return repeated_numbers