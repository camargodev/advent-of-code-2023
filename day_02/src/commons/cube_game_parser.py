class CubeGameParser:

    def parse(self, line):
        results_by_color = {"red": [], "green": [], "blue": []}
        game_id, results = self.read_raw_data_info(line)

        for result in results:
            value, color = result
            results_by_color[color].append(int(value))

        return game_id, results_by_color
    
    def read_raw_data_info(self, line):
        sanitized_line = line.replace(";", ",")
        
        game_id, results = sanitized_line.split(":")
        game_id = game_id.strip().replace("Game", "")
        
        results = results.strip().split(",")
        results = [result.strip().split(" ") for result in results]
        
        return int(game_id), results
