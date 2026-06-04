import time
# Required Middle dots for some steps to as a Tuple Collection
REQUIRED_MIDDLE_DOT= {
    (1, 3): 2,
    (3, 1): 2,
    (1, 7): 4,
    (7, 1): 4,
    (3, 9): 6,
    (9, 3): 6,
    (7, 9): 8,
    (9, 7): 8,
    (1, 9): 5,
    (9, 1): 5,
    (3, 7): 5,
    (7, 3): 5,
    (2, 8): 5,
    (8, 2): 5,
    (4, 6): 5,
    (6, 4): 5,
}


class PatternSolver:
    def __init__(self):
        self.step_limit = 9
        self.number_of_sequences = 0
        self.bfs_digits = 4
        pass

    def validate_move(self, curr_dot, next_dot, pattern):
        middle_dot = REQUIRED_MIDDLE_DOT.get((curr_dot, next_dot))
        if next_dot in pattern:
            return False
        elif middle_dot  is not None:
            if middle_dot in pattern:
                return True
            return False
        else:
            return True

    def brute_dfs(self, number_of_digits):
        for num in range(number_of_digits):
            self.solve_dfs([num + 1])

    def solve_dfs(self, pattern):

        if self.is_valid_sequence(pattern):
            self.number_of_sequences += 1
            print(pattern)
        if self.is_max_length(pattern):
            return pattern

        current_dot = pattern[-1]
        valid_moves = self.get_valid_moves(current_dot, pattern)

        for move in valid_moves:
            new_pattern = pattern + [move]
            self.solve_dfs(new_pattern)

    def is_valid_sequence(self, pattern):
        return len(pattern) >= 4

    def is_max_length(self, pattern):
        return len(pattern) >= self.step_limit

    def handle_pattern(self, pattern):
        return None

    def brute_bfs(self):
        queue = [[1],[2],[3],[4],[5],[6],[7],[8],[9]]

        while len(queue) > 0:

            pattern = queue.pop(0)

            if len(pattern) >= 4:
                self.number_of_sequences += 1
                print(pattern)
            if len(pattern) >= self.step_limit:
                continue

            current_dot = pattern[-1]

            valid_moves = self.get_valid_moves(current_dot, pattern)
            for move in valid_moves:
                new_pattern = pattern + [move]
                queue.append(new_pattern)




    def get_valid_moves(self,current_dot,pattern):
        all_moves = [1,2,3,4,5,6,7,8,9]
        valid_moves = []
        for move in all_moves:
            if self.validate_move(current_dot, move, pattern):
                valid_moves.append(move)
        return valid_moves



solver = PatternSolver()
start_time = time.perf_counter()
solver.brute_dfs(9)
end_time = time.perf_counter()
print(solver.number_of_sequences)
print(f"Ellapsed {round(end_time - start_time,2)} seconds")