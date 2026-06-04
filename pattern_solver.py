import time
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
        self.current_pattern = []
        self.step_limit = 9
        self.number_of_sequences = 0
        pass

    def validate_move(self, curr_dot, next_dot, pattern):
        middle_dot = REQUIRED_MIDDLE_DOT.get((curr_dot, next_dot))
        if next_dot in pattern:
            return False
        elif curr_dot == next_dot:
            return False
        elif middle_dot  is not None:
            if middle_dot in pattern:
                return True
            return False
        else:
            return True

    def solve_dfs(self, pattern):

        if len(pattern) >= 4:
            self.number_of_sequences += 1
            print(pattern)
        if self.isPatternSolved(pattern):
            return pattern

        current_dot = pattern[-1]
        valid_moves = self.get_valid_moves(current_dot, pattern)

        for move in valid_moves:
            new_pattern = pattern + [move]
            self.solve_dfs(new_pattern)

    def is_valid_sequence(self, pattern):
        return None

    def is_max_length(self, pattern):
        return None

    def handle_pattern(self, pattern):
        return None

    def solve_bfs(self, pattern):
        return None


    def get_valid_moves(self,current_dot,pattern):
        all_moves = [1,2,3,4,5,6,7,8,9]
        valid_moves = []
        for move in all_moves:
            if self.validate_move(current_dot, move, pattern):
                valid_moves.append(move)
        return valid_moves

    def isPatternSolved(self, pattern):
        return len(pattern) >= self.step_limit


solver = PatternSolver()
start_time = time.perf_counter()
solver.solve_dfs([1])
solver.solve_dfs([2])
solver.solve_dfs([3])
solver.solve_dfs([4])
solver.solve_dfs([5])
solver.solve_dfs([6])
solver.solve_dfs([7])
solver.solve_dfs([8])
solver.solve_dfs([9])
end_time = time.perf_counter()
print(solver.number_of_sequences)
print(f"Ellapsed {round(end_time - start_time,2)} seconds")