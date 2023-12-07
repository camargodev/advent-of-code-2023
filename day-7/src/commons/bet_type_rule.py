class AbstractTypeCondition:
    def matches(self, unique_cards, card_counts, joker_count=0):
        pass
    
class BetTypeCondition:
    def __init__(self, type, conditions):
        self.conditions = conditions
        self.type = type


    