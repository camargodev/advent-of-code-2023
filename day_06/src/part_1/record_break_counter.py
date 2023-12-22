import re

NUMBER_DIVIDER = " "

class RecordBreakCounter:
    def count(self, lines):
        times = self.extract_values(lines[0])
        records = self.extract_values(lines[1])
        total_product = 1
        for index in range(len(times)):
            time = times[index]
            record = records[index]
            ways_to_break_the_record = 0
            for time_index in range(time):
                time_loading = time - time_index
                speed = time_loading
                time_remaining = time - time_loading
                my_distance = time_remaining * speed
                if my_distance > record:
                    ways_to_break_the_record += 1
            total_product *= ways_to_break_the_record
        return total_product
    
    def extract_values(self, line):
        _, values = line.split(":")
        return [int(value) for value in re.sub(r'\s{2,}', NUMBER_DIVIDER, values).strip().split(NUMBER_DIVIDER)]
