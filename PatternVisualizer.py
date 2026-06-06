import tkinter as tk
from tkinter import ttk
from PatternSolver import PatternSolver

solver = PatternSolver()

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
        self.is_visualizing = False
        self.root = root
        self.root.title("Pattern Visualizer")
        self.root.geometry("1200x600")
        self.root.resizable(False, False)

        self.delete_queue = []

        # Canvas
        self.canvas = tk.Canvas(
            self.root,
            width=WINDOW_SIZE,
            height=WINDOW_SIZE,
            bg="lightgrey",
        )
        self.canvas.pack(side="left")

        # Control panel
        self.controls = tk.Frame(
            self.root,
            width=WINDOW_SIZE,
            height=WINDOW_SIZE,
            bg="#222222"
        )
        self.controls.pack(side="left")
        self.controls.pack_propagate(False)

        self.draw_dots([])

        # Title
        self.title_label = tk.Label(
            self.controls,
            text="Pattern Visualizer",
            font=("Arial", 24, "bold"),
            fg="white",
            bg="#222222",
        )
        self.title_label.pack(pady=30)

        # Info
        self.info_label = tk.Label(
            self.controls,
            text="Pattern length: 4",
            font=("Arial", 16),
            fg="white",
            bg="#222222",
        )
        self.info_label.pack(pady=10)

        # Input
        self.length_entry = tk.Entry(
            self.controls,
            font=("Arial", 16),
            width=10,
            justify="center",
        )
        self.length_entry.insert(0, "4")
        self.length_entry.pack(pady=10)

        # Start button
        self.start_button = tk.Button(
            self.controls,
            text="Start",
            font=("Arial", 16),
            command=self.start_visualization,
        )
        self.start_button.pack(pady=10)

        # Stop button
        self.stop_button = tk.Button(
            self.controls,
            text="Stop",
            font=("Arial", 16),
            command=self.stop_visualization,
        )
        self.stop_button.pack(pady=10)


    def start_visualization(self):
        length = int(self.length_entry.get())
        print(length)
        if self.is_visualizing:
            return
        self.is_visualizing = True
        self.draw_pattern(solver.brute_bfs(length))

    def stop_visualization(self):
        self.is_visualizing = False
        return None

    def draw_dots(self, pattern):
        for dot_number, (x, y) in DOT_POSITIONS.items():

            outline_color = "white"
            small_dot_color = "white"

            if dot_number in pattern:
                outline_color = ACTIVE_COLOR
                small_dot_color = ACTIVE_COLOR

            # Inner dots
            self.delete_queue.append((self.canvas.create_oval(
                x - OUTER_DOT_RADIUS,
                y - OUTER_DOT_RADIUS,
                x + OUTER_DOT_RADIUS,
                y + OUTER_DOT_RADIUS,
                fill="grey",
                outline=outline_color,
                width=2,
            )))

            self.delete_queue.append(self.canvas.create_oval(
                x - INNER_DOT_RADIUS,
                y - INNER_DOT_RADIUS,
                x + INNER_DOT_RADIUS,
                y + INNER_DOT_RADIUS,
                fill=small_dot_color,
                outline=small_dot_color,
                width=2,
            ))



    def draw_pattern(self, patterns):

        if not self.is_visualizing:
            return

        if len(patterns) == 0:
            self.is_visualizing = False
            return

        for to_delete in self.delete_queue:
            self.canvas.delete(to_delete)

        self.canvas.delete("pattern_line")

        pattern = patterns.pop(0)

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
                tags="pattern_line"
            )
        self.draw_dots(pattern)
        self.root.after(10,lambda: self.draw_pattern(patterns))



root = tk.Tk()
app = PatternVisualizer(root)
root.mainloop()

