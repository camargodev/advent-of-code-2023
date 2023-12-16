ASCII_MAP = {chr(i):i for i in range(256)}

class HashCalculator:
    def calculate(self, line):
        words = line.split(",")
        return sum([self.calculate_word_hash_value(word) for word in words])
    
    def calculate_word_hash_value(self, word):
        value = 0
        for char in word:
            value += ASCII_MAP[char]
            value *= 17
            value = value % 256
        print(word, value)
        return value