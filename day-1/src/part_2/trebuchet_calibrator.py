import re

NUMBER_NAME_MAP = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
    "zero": "z0e",
}

class TrebuchetCalibrator:
    def calibrate(self, lines):
        sum = 0
        for line in lines:
            sanitized_line = self.sanitize_line(line)
            numbers = re.findall('[0-9]', sanitized_line)
            value = numbers[0] + numbers[-1]
            sum += int(value)
        return sum
    
    def sanitize_line(self, line):
        for number_name, target in NUMBER_NAME_MAP.items():
            line = line.replace(number_name, target)
        return line