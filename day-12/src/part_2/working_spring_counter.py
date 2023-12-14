MISTERY = "?"
SPRING = "#"
EMPTY = "."

DEBUG = False

class InputExtractor:
    def extract(self, lines):
        springs = []
        for line in lines:
            pattern, str_numbers = line.split(" ")
            numbers = [int(str_num) for str_num in str_numbers.split(",")]
            springs.append((self.repeat_pattern(pattern), self.repeat_numbers(numbers)))
        return springs
    
    def repeat_pattern(self, pattern):
        repeated_pattern = pattern
        for _ in range(4):
            repeated_pattern += MISTERY + pattern
        return repeated_pattern
    
    def repeat_numbers(self, numbers):
        repeated_numbers = []
        for _ in range(5):
            repeated_numbers.extend(numbers)
        return repeated_numbers

class WorkingSpringCounter:
    def __init__(self):
        self.cache = dict()

    def count(self, lines):
        springs = InputExtractor().extract(lines)
        spring_sum = 0
        for spring_input_data in springs:
            spring_sum += self.process_spring(spring_input_data)
        return spring_sum

    def process_spring(self, input_data):
        pattern, numbers = input_data

        if len(numbers) == 0 and SPRING not in pattern:
            return 1
        
        if len(numbers) == 0 or len(pattern) == 0:
            return 0

        if len(pattern) < (sum(numbers) + len(numbers) - 1):
            return 0

        current_num = numbers[0]
        remaining_pattern = pattern[current_num:]

        is_number_valid = EMPTY not in pattern[:current_num]
        is_end_of_pattern = len(remaining_pattern) == 0
        is_number_end_separated = is_end_of_pattern or remaining_pattern[0] != SPRING

        possible_next_steps = []
        if is_number_valid and is_number_end_separated:
            possible_next_steps.append((remaining_pattern[1:], tuple(numbers[1:])))
        if pattern[0] != SPRING:
            possible_next_steps.append((pattern[1:], tuple(numbers)))

        result_count = 0
        for possible_next_step in possible_next_steps:
            if possible_next_step not in self.cache:
                self.cache[possible_next_step] = self.process_spring(possible_next_step)
            result_count += self.cache[possible_next_step]
        return result_count