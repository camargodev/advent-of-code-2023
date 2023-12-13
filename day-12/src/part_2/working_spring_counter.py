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
    def count(self, lines):
        springs = InputExtractor().extract(lines)
        spring_sum = 0
        for spring in springs:
            if DEBUG:
                print(spring.pattern, spring.numbers)
            spring_sum += self.process_spring(spring)
        return spring_sum
        # print(springs)

    def process_spring(self, spring):
        all_possible_patterns = []
        # self.process_spring_dp(all_possible_spring)
        # return len(all_possible_patterns)
        return self.process_spring_dp(spring.pattern, spring.numbers)

    def process_spring_dp(self, pattern, numbers, result="", current_pattern_idx=0, current_num_idx=0, characters_added=0):
        if current_num_idx == len(numbers):
            return 0 if SPRING in pattern[current_pattern_idx:] else 1

        current_number = numbers[current_num_idx]
        missing_chars_for_number = current_number - characters_added
        chars_remaining_in_pattern = len(pattern) - current_pattern_idx
        if chars_remaining_in_pattern < missing_chars_for_number:
            return 0
        
        if current_pattern_idx == (len(pattern)):
            if result[-1] == SPRING:
                if current_num_idx == (len(numbers)-1) and characters_added == numbers[current_num_idx]:
                    return 1
            if result[-1] == EMPTY:
                if current_num_idx == (len(numbers)) and characters_added == 0:
                    return 1
            return 0
        
        is_current_num_completed = numbers[current_num_idx] == characters_added

        if pattern[current_pattern_idx] == MISTERY:
            if is_current_num_completed:
                return self.process_spring_dp(pattern, numbers, result+EMPTY, current_pattern_idx+1, current_num_idx+1, 0)
            temp = 0
            if characters_added == 0:
                temp = self.process_spring_dp(pattern, numbers, result+EMPTY, current_pattern_idx+1, current_num_idx, characters_added)
            return self.process_spring_dp(pattern, numbers, result+SPRING, current_pattern_idx+1, current_num_idx, characters_added+1) + temp
        if pattern[current_pattern_idx] == EMPTY:
            if is_current_num_completed:
                return self.process_spring_dp(pattern, numbers, result+EMPTY, current_pattern_idx+1, current_num_idx+1, 0)
            if characters_added == 0:
                return self.process_spring_dp(pattern, numbers, result+EMPTY, current_pattern_idx+1, current_num_idx, 0)
        if pattern[current_pattern_idx] == SPRING:
            return self.process_spring_dp(pattern, numbers, result+SPRING, current_pattern_idx+1, current_num_idx, characters_added+1)
        return 0