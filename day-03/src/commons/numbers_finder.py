from src.commons.number import Number

DIGITS = [str(num) for num in range(10)]

class NumbersFinder:
    def find(self, lines):
        numbers = []
        for row_index in range(len(lines)):
            line = lines[row_index]
            last_was_digit = False

            start = 0
            for column_index in range(len(line)):
                value = line[column_index]
                if value not in DIGITS and last_was_digit:
                    end = column_index
                    numbers.append(Number(row_index, start, end, int(line[start:end])))
                    last_was_digit = False
                if value in DIGITS and not last_was_digit:
                    start = column_index
                    last_was_digit = True 
                    
        return numbers