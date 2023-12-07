FIVE_OF_A_KIND = 7
FOUR_OF_A_KIND = 6
FULL_HOUSE = 5
THREE_OF_A_KIND = 4
TWO_PAIR = 3
ONE_PAIR = 2
HIGH_CARD = 1

# FIVE_OF_A_KIND = "FIVE_OF_A_KIND"
# FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
# FULL_HOUSE = "FULL_HOUSE"
# THREE_OF_A_KIND = "THREE_OF_A_KIND"
# TWO_PAIR = "TWO_PAIR"
# ONE_PAIR = "ONE_PAIR"
# HIGH_CARD = "HIGH_CARD"

JOKER = "J"

POWER_BY_CARD = {
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

class BidForBet:
    def __init__(self, bet, bid):
        self.bet = bet
        self.bid = bid
        self.type = None
        self.power = None

    @staticmethod
    def create(bet, bid):
        bid_for_bet = BidForBet(bet, bid)
        bid_for_bet.type = bid_for_bet.calculate_type()
        bid_for_bet.power = str(bid_for_bet.type) + bid_for_bet.calculate_cards_power()
        return bid_for_bet

    def calculate_type(self):
        bet_unique_cards = "".join(set(self.bet))
        card_counts = [self.bet.count(card) for card in bet_unique_cards]
        num_of_jokers = self.bet.count(JOKER)
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
    
    def calculate_cards_power(self):
        return "".join(str(POWER_BY_CARD[card]) for card in self.bet)


class BetManager:
    def __init__(self):
        self.bets = []

    def add_bet(self, bet):
        self.bets.append(bet)

    def calculate_total_winnings(self):
        self.bets.sort(key=lambda card: card.power)
        total_winnings_for_bets = 0
        for index, bet in enumerate(self.bets):
            total_winnings_for_bets += bet.bid * (index+1)
        return total_winnings_for_bets
        

class WinningCalculator:

    def calculate(self, lines):
        bet_manager = BetManager()
        for line in lines:
            bet, bid = line.split(" ")
            bet_manager.add_bet(BidForBet.create(bet, int(bid)))
        return bet_manager.calculate_total_winnings()
