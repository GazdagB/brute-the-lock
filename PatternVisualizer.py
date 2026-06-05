import tkinter as tk
from tkinter import ttk

WINDOW_SIZE = 600
INNER_DOT_RADIUS = 10
OUTER_DOT_RADIUS = 50
ACTIVE_COLOR = "#00adff"

DOT_POSITIONS = {
    1: (100, 100),
    2: (300, 100),
    3: (500, 100),
    4: (100, 300),
    5: (300, 300),
    6: (500, 300),
    7: (100, 500),
    8: (300, 500),
    9: (500, 500),
}


class PatternVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pattern Visualizer")
        self.root.geometry(f"{WINDOW_SIZE}x{WINDOW_SIZE}")
        self.delete_queue = []

        self.canvas = tk.Canvas(
            self.root,
            width=WINDOW_SIZE,
            height=WINDOW_SIZE,
            bg="lightgrey",
        )
        self.canvas.pack()
        self.draw_dots()
        self.root.resizable(False, False)
        self.draw_pattern([1,2,3,4,5,6,7,8,9])
        self.draw_dots()

    def draw_dots(self):
        for dot_number, (x, y) in DOT_POSITIONS.items():
            # Inner dots
            self.delete_queue.append((self.canvas.create_oval(
                x - OUTER_DOT_RADIUS,
                y - OUTER_DOT_RADIUS,
                x + OUTER_DOT_RADIUS,
                y + OUTER_DOT_RADIUS,
                fill="grey",
                outline=ACTIVE_COLOR,
                width=2,
            )))

            self.delete_queue.append(self.canvas.create_oval(
                x - INNER_DOT_RADIUS,
                y - INNER_DOT_RADIUS,
                x + INNER_DOT_RADIUS,
                y + INNER_DOT_RADIUS,
                fill=ACTIVE_COLOR,
                outline=ACTIVE_COLOR,
                width=2,
            ))



    def draw_pattern(self, pattern):
        for to_delete in self.delete_queue:
            self.canvas.delete(to_delete)

        for index in range(len(pattern) -1):

            current_dot = pattern[index]
            next_dot = pattern[index+1]

            if index >= len(pattern) - 1:
                continue
            self.canvas.create_line(
                DOT_POSITIONS[current_dot][0],
                DOT_POSITIONS[current_dot][1],
                DOT_POSITIONS[next_dot][0],
                DOT_POSITIONS[next_dot][1],
                fill=ACTIVE_COLOR,
                width=10,
            )


root = tk.Tk()
app = PatternVisualizer(root)
root.mainloop()

