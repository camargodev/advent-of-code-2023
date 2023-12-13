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
        self.process_spring_dp(all_possible_patterns, spring)
        return len(all_possible_patterns)

    def process_spring_dp(self, patterns, spring, result="", current_pattern_idx=0, current_num_idx=0, characters_added=0):
        if current_num_idx == len(spring.numbers) and SPRING in spring.pattern[current_pattern_idx:]:
            return
        
        if current_num_idx > len(spring.numbers) or current_pattern_idx > len(spring.pattern):
            return
        
        if current_num_idx < len(spring.numbers):
            current_number = spring.numbers[current_num_idx]
            missing_chars_for_number = current_number - characters_added
            chars_remaining_in_pattern = len(spring.pattern) - current_pattern_idx
            if chars_remaining_in_pattern < missing_chars_for_number:
                return
        
        if current_pattern_idx == (len(spring.pattern)):
            if result[-1] == SPRING:
                if current_num_idx == (len(spring.numbers)-1) and characters_added == spring.numbers[current_num_idx]:
                    patterns.append(result)
                    return
            if result[-1] == EMPTY:
                if current_num_idx == (len(spring.numbers)) and characters_added == 0:
                    patterns.append(result)
                    return
            return
        if spring.pattern[current_pattern_idx] == MISTERY:
            if current_num_idx == len(spring.numbers):
                self.process_spring_dp(patterns, spring, result+EMPTY, current_pattern_idx+1, current_num_idx, 0)
                return
            if spring.is_current_number_completed(current_num_idx, characters_added):
                self.process_spring_dp(patterns, spring, result+EMPTY, current_pattern_idx+1, current_num_idx+1, 0)
                return
            if characters_added == 0:
                self.process_spring_dp(patterns, spring, result+EMPTY, current_pattern_idx+1, current_num_idx, characters_added)
            self.process_spring_dp(patterns, spring, result+SPRING, current_pattern_idx+1, current_num_idx, characters_added+1)
        if spring.pattern[current_pattern_idx] == EMPTY:
            if current_num_idx == len(spring.numbers):
                self.process_spring_dp(patterns, spring, result+EMPTY, current_pattern_idx+1, current_num_idx, 0)
                return
            if spring.is_current_number_completed(current_num_idx, characters_added):
                self.process_spring_dp(patterns, spring, result+EMPTY, current_pattern_idx+1, current_num_idx+1, 0)
                return
            elif characters_added == 0:
                self.process_spring_dp(patterns, spring, result+EMPTY, current_pattern_idx+1, current_num_idx, 0)
                return
            return
        if spring.pattern[current_pattern_idx] == SPRING:
            if current_num_idx == len(spring.numbers):
                return
            if spring.is_current_number_completed(current_num_idx, characters_added):
                return
            self.process_spring_dp(patterns, spring, result+SPRING, current_pattern_idx+1, current_num_idx, characters_added+1)