from src.commons.base_oasis_protector import BaseOasisProtector

class OasisProtector(BaseOasisProtector):
    def calculate_predicted_value(self, current_prediction, differences):
        return differences[0] - current_prediction