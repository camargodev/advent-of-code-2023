from src.commons.mapping_entities import *

EMPTY = ""
LINE_BREAK = "\n"

class MappingInfoFactory:

    def make(self, lines):
        mapping_info = dict()
        for raw_line in lines[1:]:
            line = raw_line.replace(LINE_BREAK, EMPTY)
            if line == EMPTY:
                last_was_empty = True
                continue
            if last_was_empty:
                last_was_empty = False
                source_type, target_type = self.get_source_and_target(line)
                mapping_info[source_type] = MappingInfo(source_type, target_type)
                continue
            target, source, size = [int(str_num) for str_num in line.strip().split(" ")]
            offset = target - source
            start = source
            end = source + size - 1
            mapping_info[source_type].add_offset_range(OffsetRange(start, end, offset))
        return mapping_info

    def make_with_backtracking(self, lines):
        backtracked_mapping_info = dict()
        for raw_line in lines[1:]:
            line = raw_line.replace(LINE_BREAK, EMPTY)
            if line == EMPTY:
                last_was_empty = True
                continue
            if last_was_empty:
                last_was_empty = False
                source_type, target_type = self.get_source_and_target(line)
                backtracked_mapping_info[target_type] = MappingInfo(source_type, target_type)
                continue
            target, source, size = [int(str_num) for str_num in line.strip().split(" ")]
            offset = target - source
            start = source
            end = source + size - 1
            backtracked_mapping_info[target_type].add_offset_range(OffsetRange(start+ offset, end+ offset, -offset))
        return backtracked_mapping_info
    
    def get_source_and_target(self, line):
        sanitized_line = line.replace(" map:", "")
        source, _, target = sanitized_line.split("-")
        return source, target