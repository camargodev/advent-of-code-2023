import re

ACCEPTED = "A"
REJECTED = "R"

X = "x"
M = "m"
A = "a"
S = "s"

LARGER_THAN = ">"
LOWER_THAN = "<"

START_WORKFLOW = "in"

class MachinePart:
    def __init__(self, x, m, a, s):
        self.parts = {
            X: x,
            M: m,
            A: a,
            S: s
        }
        self.rating = x+m+a+s

    def get_property(self, property):
        return self.parts[property]

class Rule:
    def __init__(self, condition, destination):
        self.condition = condition
        self.destination = destination

class Workflow:
    def __init__(self, rules, default_rule):
        self.rules = rules
        self.default_rule = default_rule

    def evaluate_part(self, part):
        for rule in self.rules:
            if rule.condition(part):
                return rule.destination
        return self.default_rule

class InputExtractor:
    def extract(self, lines):
        workflows = {}
        machine_parts = []

        line_index = 0
        while lines[line_index] != "":
            regex_result = re.search('(.+?){(.+?)}', lines[line_index])
            workflow_code, string_rules = regex_result.group(1), regex_result.group(2).split(",")
            rules, default_rule = self.extract_rules(string_rules)
            workflows[workflow_code] = Workflow(rules, default_rule)
            line_index += 1

        line_index += 1

        while line_index < len(lines):
            regex_result = re.search('{x=(.+?),m=(.+?),a=(.+?),s=(.+?)}', lines[line_index])
            x, m, a, s = int(regex_result.group(1)), int(regex_result.group(2)), int(regex_result.group(3)), int(regex_result.group(4))
            machine_parts.append(MachinePart(x, m, a, s))
            line_index += 1

        return workflows, machine_parts

    def extract_rules(self, string_rules):
        rules = []
        for string_rule in string_rules[:-1]:
            rule = self.map_to_rule_object(string_rule)
            rules.append(rule)
        return rules, string_rules[-1]
    
    def map_to_rule_object(self, string_rule):
        property, operand, value, destination = self.extract_rule_parts(string_rule)
        if operand == LARGER_THAN:
            condition = lambda part: part.get_property(property) > int(value)
        else:
            condition = lambda part: part.get_property(property) < int(value)
        return Rule(condition, destination)

    def extract_rule_parts(self, string_rule):
        rule_regex = re.search('(.+?)(<|>)(.+?):(.+)', string_rule)
        return rule_regex.group(1), rule_regex.group(2), rule_regex.group(3), rule_regex.group(4)

class WorkflowEvaluator:
    def evaluate(self, lines):
        workflows, machine_parts = InputExtractor().extract(lines)

        total_rating = 0
        for machine_part in machine_parts:
            workflow_code = START_WORKFLOW
            while workflow_code not in {ACCEPTED, REJECTED}:
                workflow = workflows[workflow_code]
                workflow_code = workflow.evaluate_part(machine_part)
            if workflow_code == ACCEPTED:
                total_rating += machine_part.rating
                
        return total_rating

