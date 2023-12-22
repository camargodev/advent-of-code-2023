from src.commons.bet_manager import *
    
class BetWithJokerManager(AbstractBetManager):
    def get_conditions_for_type(self):    
        return {
            FIVE_OF_A_KIND: [
                lambda card_info: card_info.is_num_of_unique_cards(1),
                lambda card_info: card_info.is_num_of_unique_cards(2) and card_info.any_card_repeats(4) and card_info.has_joker(),
                lambda card_info: card_info.is_num_of_unique_cards(2) and not card_info.any_card_repeats(4) and card_info.joker_count_is([2,3])],
            FOUR_OF_A_KIND: [
                lambda card_info: card_info.is_num_of_unique_cards(2) and card_info.any_card_repeats(4) and not card_info.has_joker(),
                lambda card_info: card_info.is_num_of_unique_cards(3) and card_info.any_card_repeats(3) and card_info.has_joker(),
                lambda card_info: card_info.is_num_of_unique_cards(3) and not card_info.any_card_repeats(3) and card_info.joker_count_is([2])],
            FULL_HOUSE: [
                lambda card_info: card_info.is_num_of_unique_cards(2) and not card_info.any_card_repeats(4) and not card_info.has_joker(),
                lambda card_info: card_info.is_num_of_unique_cards(3) and not card_info.any_card_repeats(3) and card_info.joker_count_is([1])],
            THREE_OF_A_KIND: [
                lambda card_info: card_info.is_num_of_unique_cards(3) and card_info.any_card_repeats(3) and not card_info.has_joker(),
                lambda card_info: card_info.is_num_of_unique_cards(4) and card_info.has_joker()],
            TWO_PAIR: [
                lambda card_info: card_info.is_num_of_unique_cards(3) and not card_info.any_card_repeats(3) and not card_info.has_joker()],
            ONE_PAIR: [
                lambda card_info: card_info.is_num_of_unique_cards(4) and not card_info.has_joker(),
                lambda card_info: card_info.is_num_of_unique_cards(5) and card_info.has_joker()]
        } 
    
    def get_cards_in_order(self):
        return ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]