SPRING = "#"
EMPTY = "."

class WorkingSpringCounter:

    def count(self, springs):
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
            result_count += self.process_next_step(possible_next_step)
        return result_count
    
    def process_next_step(self, spring_next_step):
        return self.process_spring(spring_next_step)