from src.commons.bet_manager import *

class BetWithJokerManager(AbstractBetManager):
    def calculate_bet_type(self, bet):
        bet_unique_cards = "".join(set(bet))
        card_counts = [bet.count(card) for card in bet_unique_cards]
        num_of_jokers = bet.count(JOKER)
        has_joker = num_of_jokers > 0
        
        if len(bet_unique_cards) == 1:
            return FIVE_OF_A_KIND
        if len(bet_unique_cards) == 2:
            if 4 in card_counts:
                if has_joker:
                    return FIVE_OF_A_KIND
                else:
                    return FOUR_OF_A_KIND
            else:
                if num_of_jokers in [2, 3]:
                    return FIVE_OF_A_KIND
                if has_joker:
                    return FOUR_OF_A_KIND
                else:
                    return FULL_HOUSE
        if len(bet_unique_cards) == 3:
            if 3 in card_counts:
                if has_joker:
                    return FOUR_OF_A_KIND
                else:
                    return THREE_OF_A_KIND
            else:
                if num_of_jokers == 2:
                    return FOUR_OF_A_KIND
                if has_joker:
                    return FULL_HOUSE
                else:
                    return TWO_PAIR
        if len(bet_unique_cards) == 4:
            if has_joker:
                return THREE_OF_A_KIND
            else:
                return ONE_PAIR
        if has_joker:
            return ONE_PAIR
        return HIGH_CARD
    
    def get_cards_in_order(self):
        return ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]