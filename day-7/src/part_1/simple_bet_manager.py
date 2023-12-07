from src.commons.bet_manager import *

class SimpleBetManager(AbstractBetManager):
    def get_conditions_for_type(self):
        return {
            FIVE_OF_A_KIND: [lambda card_info: card_info.is_num_of_unique_cards(1)],
            FOUR_OF_A_KIND: [lambda card_info: card_info.is_num_of_unique_cards(2) and card_info.any_card_repeats(4)],
            FULL_HOUSE: [lambda card_info: card_info.is_num_of_unique_cards(2) and not card_info.any_card_repeats(4)],
            THREE_OF_A_KIND: [lambda card_info: card_info.is_num_of_unique_cards(3) and card_info.any_card_repeats(3)],
            TWO_PAIR: [lambda card_info: card_info.is_num_of_unique_cards(3) and not card_info.any_card_repeats(3)],
            ONE_PAIR: [lambda card_info: card_info.is_num_of_unique_cards(4)]
        }

    
    def get_cards_in_order(self):
        return ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]