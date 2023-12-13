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
            possible_patterns = self.process_spring(spring)
            spring_sum += len(possible_patterns)
            if DEBUG:
                print(len(possible_patterns), possible_patterns)
        return spring_sum
        # print(springs)

    def process_spring(self, spring):
        numbers_by_index = {idx:num for idx,num in enumerate(spring.numbers)}
        all_possible_patterns = []
        self.process_spring_dp(all_possible_patterns, numbers_by_index, spring, "")
        return all_possible_patterns
        # print("\n\n",all_possible_patterns, len(all_possible_patterns))

    def process_spring_dp(self, patterns, numbers_by_index, spring, result, current_pattern_idx=0, current_num_idx=0, characters_added=0):
        if DEBUG:
            print(result)
        if current_num_idx == len(spring.numbers) and SPRING in spring.pattern[current_pattern_idx:]:
            if DEBUG:
                print("failed because already complete numbers, but a # will exist")
            return
        
        if current_num_idx > len(spring.numbers) or current_pattern_idx > len(spring.pattern):
            if DEBUG:
                print("failed because string finished")
            return
        
        if current_num_idx < len(spring.numbers):
            current_number = spring.numbers[current_num_idx]
            missing_chars_for_number = current_number - characters_added
            chars_remaining_in_pattern = len(spring.pattern) - current_pattern_idx
            if chars_remaining_in_pattern < missing_chars_for_number:
                if DEBUG:
                    print("failed because there will not be enough chars to finish pattern")
                return
        
        if current_pattern_idx == (len(spring.pattern)):
            if DEBUG:
                print("finished pattern")
            if result[-1] == SPRING:
                if current_num_idx == (len(spring.numbers)-1) and characters_added == spring.numbers[current_num_idx]:
                    if DEBUG:
                        print("  ADDED", result, "TO POSSIBLE PATTERNS!")
                    patterns.append(result)
                    return
            if result[-1] == EMPTY:
                if current_num_idx == (len(spring.numbers)) and characters_added == 0:
                    if DEBUG:
                        print("  ADDED", result, "TO POSSIBLE PATTERNS!")
                    patterns.append(result)
                    return
            if DEBUG:
                print("failed because pattern was not matched")
            return
        if spring.pattern[current_pattern_idx] == MISTERY:
            if current_num_idx == len(spring.numbers):
                self.process_spring_dp(patterns, numbers_by_index, spring, result+EMPTY, current_pattern_idx+1, current_num_idx, 0)
                return
            if spring.is_current_number_completed(current_num_idx, characters_added):
                self.process_spring_dp(patterns, numbers_by_index, spring, result+EMPTY, current_pattern_idx+1, current_num_idx+1, 0)
                return
            if characters_added == 0:
                self.process_spring_dp(patterns, numbers_by_index, spring, result+EMPTY, current_pattern_idx+1, current_num_idx, characters_added)
            self.process_spring_dp(patterns, numbers_by_index, spring, result+SPRING, current_pattern_idx+1, current_num_idx, characters_added+1)
        if spring.pattern[current_pattern_idx] == EMPTY:
            if current_num_idx == len(spring.numbers):
                self.process_spring_dp(patterns, numbers_by_index, spring, result+EMPTY, current_pattern_idx+1, current_num_idx, 0)
                return
            if spring.is_current_number_completed(current_num_idx, characters_added):
                self.process_spring_dp(patterns, numbers_by_index, spring, result+EMPTY, current_pattern_idx+1, current_num_idx+1, 0)
                return
            elif characters_added == 0:
                self.process_spring_dp(patterns, numbers_by_index, spring, result+EMPTY, current_pattern_idx+1, current_num_idx, 0)
                return
            if DEBUG:
                print("failed because", result+EMPTY, "would not complete a number with size", spring.numbers[current_num_idx], "and index", current_num_idx)
            return
        if spring.pattern[current_pattern_idx] == SPRING:
            if current_num_idx == len(spring.numbers):
                if DEBUG:
                    print("failed because numbers were already and a # was found")
                return
            if spring.is_current_number_completed(current_num_idx, characters_added):
                if DEBUG:
                    print("failed because", result+SPRING, "would continue a number already completed with size", spring.numbers[current_num_idx], "and index", current_num_idx)
                return
            self.process_spring_dp(patterns, numbers_by_index, spring, result+SPRING, current_pattern_idx+1, current_num_idx, characters_added+1)
        
        

