from src.commons.bet_winning_manager import *

class BidForBet:
    def __init__(self, bet, bid, type, power):
        self.bet = bet
        self.bid = bid
        self.type = type
        self.power = power

class BidForBetFactory:
    def __init__(self, bet_manager: AbstractBetManager):
        self.bet_manager = bet_manager
    
    def create(self, bet, bid):
        type = self.bet_manager.calculate_bet_type(bet)
        power = str(type) + self.calculate_bet_power(bet)
        return BidForBet(bet, bid, type, power)
    
    def calculate_bet_power(self, bet):
        power_by_card = self.bet_manager.get_cards_order();
        return "".join(str(power_by_card[card]) for card in bet)

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
    def __init__(self, bet_manager: AbstractBetManager):
        self.bid_for_bet_factory = BidForBetFactory(bet_manager)

    def calculate(self, lines):
        bet_manager = BetManager()
        for line in lines:
            bet, bid = line.split(" ")
            bet_manager.add_bet(self.bid_for_bet_factory.create(bet, int(bid)))
        return bet_manager.calculate_total_winnings()
