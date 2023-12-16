ASCII_MAP = {chr(i):i for i in range(256)}

class Lens:
    def __init__(self, label, focal_length, order):
        self.label = label
        self.focal_length = focal_length
        self.order = order

class BoxContent:
    def __init__(self, box_key):
        self.box_key = box_key
        self.len_by_label = dict()
        self.order = 0
    
    def add_lens(self, label, focal_length):
        if label in self.len_by_label:
            self.len_by_label[label].focal_length = int(focal_length)
            return
        self.len_by_label[label] = Lens(label, int(focal_length), self.order)
        self.order += 1

    def calculate_box_value(self):
        lens = list(self.len_by_label.values())
        lens.sort(key=lambda camera_len: camera_len.order)
        box_value = 0
        for len_idx, camera_len in enumerate(lens):
            len_value = self.box_key * (len_idx+1) * camera_len.focal_length
            box_value += len_value
        return box_value

class HashCalculator:
    def __init__(self):
        self.boxes = {}

    def calculate(self, line):
        commands = line.split(",")
        for command in commands:
            self.process_label(command)
        total = 0
        for box in self.boxes.values():
            total += box.calculate_box_value()
        return total
    
    def process_label(self, label):
        if "-" in label:
            label = label.replace("-", "")
            hash_value = WordHashCalculator.calculate(label)
            if hash_value not in self.boxes:
                self.boxes[hash_value] = BoxContent(hash_value+1)
            if label in self.boxes[hash_value].len_by_label:
                del self.boxes[hash_value].len_by_label[label]
            return
        label, focal_length = label.split("=")
        hash_value = WordHashCalculator.calculate(label)
        if hash_value not in self.boxes:
            self.boxes[hash_value] = BoxContent(hash_value+1)
        self.boxes[hash_value].add_lens(label, focal_length)

class WordHashCalculator:
    @staticmethod
    def calculate( word):
        value = 0
        for char in word:
            value += ASCII_MAP[char]
            value *= 17
            value = value % 256
        # print(word, value)
        return value