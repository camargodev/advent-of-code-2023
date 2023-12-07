FIVE_OF_A_KIND = 7
FOUR_OF_A_KIND = 6
FULL_HOUSE = 5
THREE_OF_A_KIND = 4
TWO_PAIR = 3
ONE_PAIR = 2
HIGH_CARD = 1

JOKER = "J"

class AbstractBetManager:
    def calculate_bet_type(self, bet):
        pass
    
    def get_cards_order(self):
        pass