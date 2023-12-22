from src.commons.working_spring_counter import WorkingSpringCounter

class CachedWorkingSpringCounter(WorkingSpringCounter):
    def __init__(self):
        self.cache = dict()
    
    def process_next_step(self, spring_next_step):
        if spring_next_step not in self.cache:
            self.cache[spring_next_step] = self.process_spring(spring_next_step)
        return self.cache[spring_next_step]