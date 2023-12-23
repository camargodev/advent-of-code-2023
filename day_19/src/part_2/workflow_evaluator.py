import re
import copy
from collections import deque

ACCEPTED = "A"
REJECTED = "R"

X = "x"
M = "m"
A = "a"
S = "s"

LARGER_THAN = ">"
LOWER_THAN = "<"

START_WORKFLOW = "in"

class Rule:
    def __init__(self, property, operand, value, destination):
        self.property = property
        self.operand = operand
        self.value = value
        self.destination = destination

class Workflow:
    def __init__(self, rules, default_rule):
        self.rules = rules
        self.default_rule = default_rule

    def evaluate_ranges(self, ranges_by_property):
        next_steps = dict()
        accepted_ranges = []
        remaining_ranges = copy.deepcopy(ranges_by_property)


        for rule in self.rules:
            range_min, range_max = ranges_by_property[rule.property]
            new_ranges = copy.deepcopy(remaining_ranges)
            
            if rule.operand == LOWER_THAN:
                new_range = (range_min, rule.value-1)
                remaining_ranges[rule.property] = (rule.value, range_max)
            else:
                new_range = (rule.value+1, range_max)
                remaining_ranges[rule.property] = (range_min, rule.value)
            
            new_ranges[rule.property] = new_range
            if rule.destination not in {ACCEPTED, REJECTED}:
                next_steps[rule.destination] = new_ranges
            elif rule.destination == ACCEPTED:
                accepted_ranges.append(new_ranges)

        if self.default_rule not in {ACCEPTED, REJECTED}:
            next_steps[self.default_rule] = remaining_ranges
        elif self.default_rule == ACCEPTED:
            accepted_ranges.append(remaining_ranges)
        return next_steps, accepted_ranges

class InputExtractor:
    def extract(self, lines):
        workflows = {}

        line_index = 0
        while lines[line_index] != "":
            regex_result = re.search('(.+?){(.+?)}', lines[line_index])
            workflow_code, string_rules = regex_result.group(1), regex_result.group(2).split(",")
            rules, default_rule = self.extract_rules(string_rules)
            workflows[workflow_code] = Workflow(rules, default_rule)
            line_index += 1

        return workflows

    def extract_rules(self, string_rules):
        rules = []
        for string_rule in string_rules[:-1]:
            rule = self.map_to_rule_object(string_rule)
            rules.append(rule)
        return rules, string_rules[-1]
    
    def map_to_rule_object(self, string_rule):
        property, operand, value, destination = self.extract_rule_parts(string_rule)
        return Rule(property, operand, value, destination)

    def extract_rule_parts(self, string_rule):
        rule_regex = re.search('(.+?)(<|>)(.+?):(.+)', string_rule)
        return rule_regex.group(1), rule_regex.group(2), int(rule_regex.group(3)), rule_regex.group(4)

class WorkflowEvaluator:
    def evaluate(self, lines):
        workflow_by_code = InputExtractor().extract(lines)

        all_accepted_ranges = []
        ranges_by_property = {X:(1, 4000), M:(1, 4000), A:(1, 4000), S:(1, 4000)}

        workflows_to_evaluate = deque()
        workflows_to_evaluate.append((START_WORKFLOW, ranges_by_property))

        while workflows_to_evaluate:
            workflow_code, ranges_by_property = workflows_to_evaluate.popleft()
            workflow = workflow_by_code[workflow_code]
            
            next_steps, accepted_ranges = workflow.evaluate_ranges(ranges_by_property)
            all_accepted_ranges.extend(accepted_ranges)
            
            for next_workflow_code, next_ranges in next_steps.items():
                workflows_to_evaluate.append((next_workflow_code, next_ranges))

        possibility_count = 0
        for accepted_ranges in all_accepted_ranges:
            possibilites = 1
            for range_min, range_max in accepted_ranges.values():
                # if range_max < range_min:
                #     continue
                possibilites *= (range_max-range_min+1)
            possibility_count += possibilites
        return possibility_count

