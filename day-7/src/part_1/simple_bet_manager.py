from src.commons.bet_manager import *

class SimpleBetManager(AbstractBetManager):
    def calculate_bet_type(self, bet):
        bet_unique_values = "".join(set(bet))
        if len(bet_unique_values) == 1:
            return FIVE_OF_A_KIND
        if len(bet_unique_values) == 2:
            card_1_count = bet.count(bet_unique_values[0])
            card_2_count = bet.count(bet_unique_values[1])
            if 4 in [card_1_count, card_2_count]:
                return FOUR_OF_A_KIND
            return FULL_HOUSE
        if len(bet_unique_values) == 3:
            card_1_count = bet.count(bet_unique_values[0])
            card_2_count = bet.count(bet_unique_values[1])
            card_3_count = bet.count(bet_unique_values[2])
            if 3 in [card_1_count, card_2_count, card_3_count]:
                return THREE_OF_A_KIND
            return TWO_PAIR
        if len(bet_unique_values) == 4:
            return ONE_PAIR
        return HIGH_CARD
    
    def get_cards_order(self):
        return {
            "2": "01",
            "3": "02",
            "4": "03",
            "5": "04",
            "6": "05",
            "7": "06",
            "8": "07",
            "9": "08",
            "T": "09",
            "J": "10",
            "Q": "11",
            "K": "12",
            "A": "13"
        }