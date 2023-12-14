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
        # return pattern
        repeated_pattern = pattern
        for _ in range(4):
            repeated_pattern += MISTERY + pattern
        return repeated_pattern
    
    def repeat_numbers(self, numbers):
        # return numbers
        repeated_numbers = []
        for _ in range(5):
            repeated_numbers.extend(numbers)
        return repeated_numbers

class WorkingSpringCounter:
    def count(self, lines):
        springs = InputExtractor().extract(lines)
        spring_sum = 0
        for spring in springs:
            if DEBUG:
                print(spring.pattern, spring.numbers)
            current_sum = self.process_spring(spring)
            print(current_sum)
            spring_sum += current_sum
        return spring_sum
        # print(springs)

    def process_spring(self, spring):
        all_possible_patterns = []
        # self.process_spring_dp(all_possible_spring)
        # return len(all_possible_patterns)
        return self.process_spring_dp(spring.pattern, spring.numbers)

    def process_spring_dp(self, pattern, numbers, last_char=""):
        if len(numbers) == 0 and SPRING not in pattern:
            return 1
        
        if len(numbers) == 0 or len(pattern) == 0:
            return 0

        if len(pattern) < (sum(numbers) + len(numbers) - 1):
            return 0
        
        # if len(pattern) == 0:
        #     if len(numbers) == 1 and current_num_lenght == numbers[0]:
        #         return 1
        #     if len(numbers) == 0 and current_num_lenght == 0:
        #         return 1
        #     return 0

        current_num = numbers[0]
        # is_current_num_completed = current_num == current_num_lenght

        results_with_pattern = 0
        remaining_pattern = pattern[current_num:]

        pattern_slice = pattern[:current_num]
        is_number_valid = EMPTY not in pattern_slice
        is_end_of_pattern = len(remaining_pattern) == 0
        # is_number_start_separated = last_char != SPRING
        is_number_end_separated = is_end_of_pattern or remaining_pattern[0] != SPRING

        if is_number_valid and is_number_end_separated:
            next_pattern = remaining_pattern[1:]
            # last_char = remaining_pattern[0] if not is_end_of_pattern else ""
            results_with_pattern = self.process_spring_dp(next_pattern, numbers[1:], "")
        if SPRING == pattern_slice[0]:
            return results_with_pattern
        return results_with_pattern + self.process_spring_dp(pattern[1:], numbers, "")

        # if current_char == SPRING:
        #     return 0
            # return self.process_spring_dp(pattern[1:], numbers[1:], 0)

        # if current_char == MISTERY:
        #     # temp = 0
        #     # if current_num_lenght == 0:
        #     #     temp = self.process_spring_dp(pattern[1:], numbers, current_num_lenght)
        #     return self.process_spring_dp(pattern[1:], numbers)
        # if current_char == EMPTY:
        #     return self.process_spring_dp(pattern[1:], numbers)
        # if current_char == SPRING:
        #     return 0
        # return 0