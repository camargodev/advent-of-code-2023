import re

class TrebuchetCalibrator:
    def calibrate(self, lines):
        sum = 0
        for line in lines:
            numbers = re.findall('[0-9]', line)
            value = numbers[0] + numbers[-1]
            sum += int(value)
        return sum