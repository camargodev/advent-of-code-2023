ASCII_MAP = {chr(i):i for i in range(256)}

class HashMapper:
    @staticmethod
    def map(string):
        value = 0
        for char in string:
            value += ASCII_MAP[char]
            value *= 17
            value = value % 256
        return value