class RecordBreakCounter:
    def count(self, lines):
        time = self.extract_value(lines[0])
        record = self.extract_value(lines[1])
        ways_to_break_the_record = 0
        for time_index in range(time):
            time_loading = time - time_index
            speed = time_loading
            time_remaining = time - time_loading
            my_distance = time_remaining * speed
            if my_distance > record:
                ways_to_break_the_record += 1
        return ways_to_break_the_record
    
    def extract_value(self, line):
        _, value = line.split(":")
        return int(value.replace(" ", ""))
