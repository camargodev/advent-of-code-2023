FIVE_OF_A_KIND = 7
FOUR_OF_A_KIND = 6
FULL_HOUSE = 5
THREE_OF_A_KIND = 4
TWO_PAIR = 3
ONE_PAIR = 2
HIGH_CARD = 1

POWER_BY_CARD = {
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
        bet_unique_values = "".join(set(self.bet))
        if len(bet_unique_values) == 1:
            return FIVE_OF_A_KIND
        if len(bet_unique_values) == 2:
            card_1_count = self.bet.count(bet_unique_values[0])
            card_2_count = self.bet.count(bet_unique_values[1])
            if 4 in [card_1_count, card_2_count]:
                return FOUR_OF_A_KIND
            return FULL_HOUSE
        if len(bet_unique_values) == 3:
            card_1_count = self.bet.count(bet_unique_values[0])
            card_2_count = self.bet.count(bet_unique_values[1])
            card_3_count = self.bet.count(bet_unique_values[2])
            if 3 in [card_1_count, card_2_count, card_3_count]:
                return THREE_OF_A_KIND
            return TWO_PAIR
        if len(bet_unique_values) == 4:
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
