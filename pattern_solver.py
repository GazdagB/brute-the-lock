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
        self.current_pattern = [2,4]
        self.step_limit = 4
        self.step_counter = 0
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




solver = PatternSolver()
print(solver.validate_move(1, 7))