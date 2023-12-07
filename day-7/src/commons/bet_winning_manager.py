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
    
    def get_cards_order(self):
        return {
            "J": "01",
            "2": "02",
            "3": "03",
            "4": "04",
            "5": "05",
            "6": "06",
            "7": "07",
            "8": "08",
            "9": "09",
            "T": "10",
            "Q": "11",
            "K": "12",
            "A": "13"
        }