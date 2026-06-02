import random

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
        self.step_limit = 4
        pass

    def validate_move(self, curr_dot, next_dot):
        if next_dot in self.current_pattern:
            return False
        elif curr_dot == next_dot:
            return False
        elif REQUIRED_MIDDLE_DOT.get((curr_dot, next_dot)) is not None:
            if REQUIRED_MIDDLE_DOT.get((curr_dot, next_dot)) in self.current_pattern:
                return True
            return False
        else:
            return True

    def solve(self):

        if self.isPatternSolved():
            return self.current_pattern

        if self.current_pattern == []:
            current_dot = random.randint(1, 9)
            self.current_pattern.append(current_dot)
            print(self.current_pattern)
            return self.current_pattern
        else:
            current_dot = self.current_pattern[-1]


        valid_next_steps = self.get_valid_moves(current_dot)
        self.current_pattern.append(random.choice(valid_next_steps))
        print(self.current_pattern)
        return None

    def get_valid_moves(self,current_dot):
        all_moves = [1,2,3,4,5,6,7,8,9]
        valid_moves = []
        for move in all_moves:
            if self.validate_move(current_dot, move):
                valid_moves.append(move)
        return valid_moves

    def isPatternSolved(self):
        return len(self.current_pattern) >= self.step_limit


solver = PatternSolver()
solver.solve()
solver.solve()
solver.solve()
solver.solve()