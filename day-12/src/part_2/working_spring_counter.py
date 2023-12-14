MISTERY = "?"
SPRING = "#"
EMPTY = "."

DEBUG = False

class Spring:
    def __init__(self, pattern, numbers):
        self.pattern = pattern
        self.numbers = numbers

    def is_current_number_completed(self, num_idx, num_chars_added):
        return self.numbers[num_idx] == num_chars_added

class InputExtractor:
    def extract(self, lines):
        springs = []
        for line in lines:
            pattern, str_numbers = line.split(" ")
            numbers = [int(str_num) for str_num in str_numbers.split(",")]
            springs.append(Spring(self.repeat_pattern(pattern), self.repeat_numbers(numbers)))
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
        for spring in springs:
            current_sum = self.process_spring(spring)
            spring_sum += current_sum
        return spring_sum

    def process_spring(self, spring):
        return self.process_spring_dp(spring.pattern, spring.numbers)

    def process_spring_dp(self, pattern, numbers):
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

        possible_results = 0
        if is_number_valid and is_number_end_separated:
            cache_key = (remaining_pattern[1:], tuple(numbers[1:]))
            if cache_key not in self.cache:
                self.cache[cache_key] = self.process_spring_dp(remaining_pattern[1:], numbers[1:])
            possible_results += self.cache[cache_key]
        if pattern[0] != SPRING:
            cache_key = (pattern[1:], tuple(numbers))
            if cache_key not in self.cache:
                self.cache[cache_key] = self.process_spring_dp(pattern[1:], numbers)
            possible_results += self.cache[cache_key]
        return possible_results