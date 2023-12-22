class BaseOasisProtector():
    def predict_values_to_save_oasis(self, lines):
        predicted_value_sum = 0
        for line in lines:
            values = [int(value) for value in line.replace("\n", "").split(" ")]
            all_differences = [values]
            while not self.is_all_zeroes(values):
                values = self.calculate_differences(values)
                all_differences.append(values)
            predicted_value = 0
            for differences in reversed(all_differences):
                predicted_value = self.calculate_predicted_value(predicted_value, differences)
            predicted_value_sum += predicted_value
        return predicted_value_sum

    def calculate_differences(self, values):
        differences = []
        for index in range(len(values)-1):
            differences.append(values[index+1] - values[index])
        return differences
    
    def is_all_zeroes(self, values):
        return set(values) == {0}
    
    def calculate_predicted_value(self, current_prediction, new_value):
        pass