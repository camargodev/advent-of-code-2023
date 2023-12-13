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

    def process_spring_dp(self, pattern, numbers, current_num_lenght=0):
        if len(numbers) == 0:
            return 0 if SPRING in pattern else 1

        current_num = numbers[0]
        if len(pattern) < (current_num - current_num_lenght):
            return 0
        
        if len(pattern) == 0:
            if len(numbers) == 1 and current_num_lenght == numbers[0]:
                return 1
            if len(numbers) == 0 and current_num_lenght == 0:
                return 1
            return 0
        
        current_char = pattern[0]
        is_current_num_completed = current_num == current_num_lenght

        if is_current_num_completed and current_char != SPRING:
            return self.process_spring_dp(pattern[1:], numbers[1:], 0)

        if current_char == MISTERY:
            temp = 0
            if current_num_lenght == 0:
                temp = self.process_spring_dp(pattern[1:], numbers, current_num_lenght)
            return self.process_spring_dp(pattern[1:], numbers, current_num_lenght+1) + temp
        if current_char == EMPTY and current_num_lenght == 0:
            return self.process_spring_dp(pattern[1:], numbers, 0)
        if current_char == SPRING:
            return self.process_spring_dp(pattern[1:], numbers, current_num_lenght+1)
        return 0