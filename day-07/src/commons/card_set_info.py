JOKER = "J"

class CardInfo:
    def __init__(self, bet):
        self.card_set = "".join(set(bet))
        self.card_counts = [bet.count(card) for card in self.card_set]
        self.num_of_jokers = bet.count(JOKER)
    
    def any_card_repeats(self, count):
        return count in self.card_counts
    
    def is_num_of_unique_cards(self, num):
        return num == len(self.card_set)
    
    def has_joker(self):
        return self.num_of_jokers > 0
    
    def joker_count_is(self, counts):
        return self.num_of_jokers in counts