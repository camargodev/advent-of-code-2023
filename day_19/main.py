from src.part_1.workflow_evaluator import WorkflowEvaluator as FirstWorkflowEvaluator
from src.part_2.workflow_evaluator import WorkflowEvaluator as SecondWorkflowEvaluator

if __name__ == "__main__":
    lines = [line.replace("\n","") for line in open("day_19/res/input.txt", "r")]
    print(FirstWorkflowEvaluator().evaluate(lines))
    print(SecondWorkflowEvaluator().evaluate(lines))
