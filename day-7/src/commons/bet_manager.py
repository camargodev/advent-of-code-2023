FIVE_OF_A_KIND = 7
FOUR_OF_A_KIND = 6
FULL_HOUSE = 5
THREE_OF_A_KIND = 4
TWO_PAIR = 3
ONE_PAIR = 2
HIGH_CARD = 1

class AbstractBetManager:
    def get_conditions_for_type(self):
        pass
    
    def get_cards_in_order(self):
        pass