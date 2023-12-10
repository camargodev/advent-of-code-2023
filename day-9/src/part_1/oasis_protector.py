from src.commons.base_oasis_protector import BaseOasisProtector

class OasisProtector(BaseOasisProtector):
    def calculate_predicted_value(self, current_prediction, differences):
        return differences[-1] + current_prediction