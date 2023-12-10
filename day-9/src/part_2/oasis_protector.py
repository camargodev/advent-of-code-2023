class OasisProtector():
    def predict_values_to_save_oasis(self, lines):
        predicted_value_sum = 0
        for line in lines:
            values = [int(value) for value in line.replace("\n", "").split(" ")]
            # print(values)
            all_differences = [values]
            while not self.is_all_zeroes(values):
                values = self.calculate_differences(values)
                all_differences.append(values)
                # print(values)
            predicted_value = 0
            for differences in reversed(all_differences):
                first = differences[0]
                predicted_value = first - predicted_value
                # print(differences, first, predicted_value)
            predicted_value_sum += predicted_value
            # print(predicted_value)
        return predicted_value_sum

    def calculate_differences(self, values):
        differences = []
        for index in range(len(values)-1):
            differences.append(values[index+1] - values[index])
        return differences
    
    def is_all_zeroes(self, values):
        return set(values) == {0}