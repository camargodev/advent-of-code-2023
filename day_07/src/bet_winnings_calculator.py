from src.commons.bet_manager import AbstractBetManager
from src.commons.card_set_info import CardInfo
from src.commons.bet_manager import HIGH_CARD

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
        type = self.calculate_bet_type(bet)
        power = str(type) + self.calculate_bet_power(bet)
        return BidForBet(bet, bid, type, power)
    
    def calculate_bet_type(self, bet):
        card_info = CardInfo(bet)
        conditions_for_type = self.bet_manager.get_conditions_for_type()
        for type, conditions in conditions_for_type.items():
            for condition in conditions:
                if condition(card_info):
                    return type
        return HIGH_CARD

    def calculate_bet_power(self, bet):
        cards_in_order = self.bet_manager.get_cards_in_order();
        power_by_card = {card:str(power).zfill(2) for power, card in enumerate(cards_in_order)}
        return "".join(str(power_by_card[card]) for card in bet)


class WinningCalculator:
    def __init__(self, bet_manager: AbstractBetManager):
        self.bid_for_bet_factory = BidForBetFactory(bet_manager)

    def calculate(self, lines):
        bets = []
        for line in lines:
            bet, bid = line.split(" ")
            bets.append(self.bid_for_bet_factory.create(bet, int(bid)))
        return self.calculate_total_winnings(bets)
    
    def calculate_total_winnings(self, bets):
        bets.sort(key=lambda card: card.power)
        total_winnings_for_bets = 0
        for index, bet in enumerate(bets):
            total_winnings_for_bets += bet.bid * (index+1)
        return total_winnings_for_bets
