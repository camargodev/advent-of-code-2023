import math

MAX_PIECES_BY_COLOR = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def read_raw_data_info(line):
    sanitized_line = line.replace(";", "").replace(",", "")
    
    _, results = sanitized_line.split(":")
    return results.strip().split(" ")
    
def parse_game_info(line):
    results_by_color = {"red": [], "green": [], "blue": []}
    results = read_raw_data_info(line)

    for i in range(int(len(results)/2)):
        result = int(results[2*i])
        color = results[2*i + 1]
        results_by_color[color].append(result)

    return results_by_color

def calculate_min_product(results_by_color):
    return math.prod([max(results) for results in results_by_color.values()])


def day_2(input):
    sum_products = 0
    for line in input:
        results_by_color = parse_game_info(line)
        sum_products += calculate_min_product(results_by_color)
    print(sum_products)


if __name__ == "__main__":
    input = open("day-2/input.txt", "r")
    day_2(input)