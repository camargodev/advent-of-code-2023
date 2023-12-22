from src.commons.hash_mapper import HashMapper

DELETION_TOKEN = "-"
INSERTION_TOKEN = "="

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

    def insert_lens(self, label, focal_length):
        if label in self.len_by_label:
            self.len_by_label[label].focal_length = int(focal_length)
        else:
            self.len_by_label[label] = Lens(label, int(focal_length), self.order)
            self.order += 1

    def delete_lens(self, label):
        if label in self.len_by_label:
            del self.len_by_label[label]

    def calculate_box_value(self):
        lens = list(self.len_by_label.values())
        lens.sort(key=lambda camera_len: camera_len.order)
        box_value = 0
        for len_idx, camera_len in enumerate(lens):
            len_value = self.box_key * (len_idx+1) * camera_len.focal_length
            box_value += len_value
        return box_value

class HashMapCalculator:

    def calculate(self, line):
        boxes = {i:BoxContent(i+1) for i in range(256)}
        for command in line.split(","):
            self.process_command(boxes, command)
        return sum([box.calculate_box_value() for box in boxes.values()])
    
    def process_command(self, boxes, command):
        token, label, focal_length = self.translate_command(command)
        hash_value = HashMapper.map(label)
        if token == DELETION_TOKEN:
            boxes[hash_value].delete_lens(label)
        else:
            boxes[hash_value].insert_lens(label, focal_length)

    def translate_command(self, command):
        if DELETION_TOKEN in command:
            label, _ = command.split(DELETION_TOKEN)
            return DELETION_TOKEN, label, None
        label, focal_length = command.split(INSERTION_TOKEN)
        return INSERTION_TOKEN, label, focal_length