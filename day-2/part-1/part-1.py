MAX_PIECES_BY_COLOR = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def read_raw_data_info(line):
    sanitized_line = line.replace(";", "").replace(",", "")
    
    game_id, results = sanitized_line.split(":")
    game_id = game_id.replace("Game ", "")
    results = results.strip().split(" ")
    
    return int(game_id), results

def parse_game_info(line):
    results_by_color = {"red": [], "green": [], "blue": []}
    game_id, results = read_raw_data_info(line)

    for i in range(int(len(results)/2)):
        result = int(results[2*i])
        color = results[2*i + 1]
        results_by_color[color].append(result)

    return game_id, results_by_color

def is_game_valid(results_by_color):
    for color, results in results_by_color.items():
        if MAX_PIECES_BY_COLOR[color] < max(results):
            return False
    return True


def day_2(input):
    sum_ids = 0
    for line in input:
        game_id, results_by_color = parse_game_info(line)
        if is_game_valid(results_by_color):
            sum_ids += game_id
    print(sum_ids)


if __name__ == "__main__":
    input = open("day-2/input.txt", "r")
    day_2(input)