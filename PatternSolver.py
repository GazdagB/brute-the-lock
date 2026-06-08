import time

MAX_SEQUENCE_DIGITS = 9
MIN_SEQUENCE_DIGITS = 4
ALL_DOTS = [1,2,3,4,5,6,7,8,9]

REQUIRED_MIDDLE_DOT = {
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
        self.max_length = MAX_SEQUENCE_DIGITS
        self.min_length = MIN_SEQUENCE_DIGITS
        self.start_time = time.time()
        self.end_time = time.time()
        pass

    def is_valid_move(self, curr_dot, next_dot, pattern):

        if next_dot in pattern:
            return False

        middle_dot = REQUIRED_MIDDLE_DOT.get((curr_dot, next_dot))

        if middle_dot is None:
            return True

        return middle_dot in pattern

    def brute_dfs(self, from_length = MAX_SEQUENCE_DIGITS, up_to_length = MAX_SEQUENCE_DIGITS, do_print = False):
        self.start_time = time.time()
        results = []
        self.max_length = up_to_length
        self.min_length = from_length

        def dfs(pattern):
            if self.is_valid_sequence(pattern):
                if do_print:
                    print(pattern)
                results.append(pattern)
            if self.is_max_length(pattern):
                return pattern

            current_dot = pattern[-1]
            valid_moves = self.get_valid_moves(current_dot, pattern)

            for move in valid_moves:
                new_pattern = pattern + [move]
                dfs(new_pattern)

        for start_dot in range(1, 10):
            dfs([start_dot])

        self.end_time = time.time()
        return {
            "patterns": results,
            "comp_time": self.end_time - self.start_time,
                }


    def is_valid_sequence(self, pattern):
        return len(pattern) >= self.min_length

    def is_max_length(self, pattern):
        return len(pattern) >= self.max_length

    def brute_bfs(self,from_length = MIN_SEQUENCE_DIGITS, up_to_length = MAX_SEQUENCE_DIGITS, do_print = False):
        self.max_length = up_to_length
        self.min_length = from_length

        queue = [[1],[2],[3],[4],[5],[6],[7],[8],[9]]
        result = []

        while len(queue) > 0:

            pattern = queue.pop(0)

            if len(pattern) >= self.min_length:
                result.append(pattern)
                if do_print:
                    print(pattern)
            if self.is_max_length(pattern):
                continue

            current_dot = pattern[-1]

            valid_moves = self.get_valid_moves(current_dot, pattern)
            for move in valid_moves:
                new_pattern = pattern + [move]
                queue.append(new_pattern)
        self.end_time = time.time()
        return {
            "patterns": result,
            "comp_time": self.end_time - self.start_time,
        }

    def get_valid_moves(self,current_dot,pattern):
        valid_moves = []
        for move in ALL_DOTS:
            if self.is_valid_move(current_dot, move, pattern):
                valid_moves.append(move)
        return valid_moves