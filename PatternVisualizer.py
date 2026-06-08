import tkinter as tk
from PatternSolver import PatternSolver
import time

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
        self.pattern_count = 0
        self.start_time = 0
        self.comp_time = 0

        self.algorithm_var = tk.StringVar(value="DFS")
        self.speed_var = tk.IntVar(value=50)

        self.canvas = tk.Canvas(
            self.root,
            width=WINDOW_SIZE,
            height=WINDOW_SIZE,
            bg="lightgrey",
        )
        self.canvas.pack(side="left", fill="both")

        self.controls = tk.Frame(
            self.root,
            width=WINDOW_SIZE,
            height=WINDOW_SIZE,
            bg="#222222"
        )
        self.controls.pack(side="left", fill="both", expand=True)
        self.controls.pack_propagate(False)

        self.controls.grid_columnconfigure(0, weight=1)
        self.controls.grid_columnconfigure(1, weight=1)

        for row in range(9):
            self.controls.grid_rowconfigure(row, weight=0)

        self.draw_dots([])

        self.title_label = tk.Label(
            self.controls,
            text="Pattern Visualizer",
            font=("Arial", 24, "bold"),
            fg="white",
            bg="#222222",
        )
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(25, 25), sticky="ew")

        self.algorithm_label = tk.Label(
            self.controls,
            text="Solving method:",
            font=("Arial", 14),
            fg="white",
            bg="#222222",
        )
        self.algorithm_label.grid(row=1, column=0, columnspan=2, pady=(0, 5), sticky="ew")

        self.dfs_radio = tk.Radiobutton(
            self.controls,
            text="DFS",
            variable=self.algorithm_var,
            value="DFS",
            font=("Arial", 13),
            fg="white",
            bg="#222222",
            selectcolor="#222222",
            activebackground="#222222",
            activeforeground="white",
        )
        self.dfs_radio.grid(row=2, column=0, sticky="e", padx=20)

        self.bfs_radio = tk.Radiobutton(
            self.controls,
            text="BFS",
            variable=self.algorithm_var,
            value="BFS",
            font=("Arial", 13),
            fg="white",
            bg="#222222",
            selectcolor="#222222",
            activebackground="#222222",
            activeforeground="white",
        )
        self.bfs_radio.grid(row=2, column=1, sticky="w", padx=20)

        self.min_label = tk.Label(
            self.controls,
            text="Minimum length:",
            font=("Arial", 14),
            fg="white",
            bg="#222222",
        )
        self.min_label.grid(row=3, column=0, pady=(25, 5), sticky="ew")

        self.max_label = tk.Label(
            self.controls,
            text="Maximum length:",
            font=("Arial", 14),
            fg="white",
            bg="#222222",
        )
        self.max_label.grid(row=3, column=1, pady=(25, 5), sticky="ew")

        self.start_entry = tk.Entry(
            self.controls,
            font=("Arial", 16),
            width=8,
            justify="center",
        )
        self.start_entry.insert(0, "4")
        self.start_entry.grid(row=4, column=0, padx=50, sticky="ew")

        self.end_entry = tk.Entry(
            self.controls,
            font=("Arial", 16),
            width=8,
            justify="center",
        )
        self.end_entry.insert(0, "4")
        self.end_entry.grid(row=4, column=1, padx=50, sticky="ew")

        self.speed_label = tk.Label(
            self.controls,
            text="Visualization speed:",
            font=("Arial", 14),
            fg="white",
            bg="#222222",
        )
        self.speed_label.grid(row=5, column=0, columnspan=2, pady=(30, 5), sticky="ew")

        self.speed_slider = tk.Scale(
            self.controls,
            from_=200,
            to=1,
            orient="horizontal",
            variable=self.speed_var,
            bg="#222222",
            fg="white",
            troughcolor="#444444",
            highlightthickness=0,
        )
        self.speed_slider.grid(row=6, column=0, columnspan=2, padx=70, sticky="ew")

        self.start_button = tk.Button(
            self.controls,
            text="Start",
            font=("Arial", 16),
            width=8,
            command=self.start_visualization,
        )
        self.start_button.grid(row=7, column=0, pady=25, sticky="e", padx=20)

        self.stop_button = tk.Button(
            self.controls,
            text="Stop",
            font=("Arial", 16),
            width=8,
            command=self.stop_visualization,
        )
        self.stop_button.grid(row=7, column=1, pady=25, sticky="w", padx=20)

        self.summary_label = tk.Label(
            self.controls,
            text="Summary:\nWaiting for start...",
            font=("Arial", 13),
            fg="white",
            bg="#222222",
            justify="left",
            anchor="w",
        )
        self.summary_label.grid(
            row=8,
            column=0,
            columnspan=2,
            padx=80,
            pady=(5, 0),
            sticky="ew"
        )

    def validate_inputs(self):
        try:
            start = int(self.start_entry.get())
            end = int(self.end_entry.get())

            if start < 1 or end < 1:
                self.summary_label.config(text="Error: values must be at least 1.")
                return None, None

            if start > 9 or end > 9:
                self.summary_label.config(text="Error: maximum value is 9.")
                return None, None

            if start > end:
                self.summary_label.config(text="Error: min cannot be greater than max.")
                return None, None

            return start, end

        except ValueError:
            self.summary_label.config(text="Error: please enter valid numbers.")
            return None, None

    def start_visualization(self):
        if self.is_visualizing:
            return

        start, end = self.validate_inputs()

        if start is None or end is None:
            return

        self.is_visualizing = True
        self.start_time = time.time()

        algorithm = self.algorithm_var.get()

        if algorithm == "DFS":
            res_object = solver.brute_dfs(start, end)
            patterns = res_object["patterns"]
            self.comp_time = round(res_object["comp_time"],4)
        else:
            res_object = solver.brute_bfs(start, end)
            patterns = res_object["patterns"]
            self.comp_time = round(res_object["comp_time"],3)

        self.pattern_count = len(patterns)

        self.summary_label.config(
            text=f"Summary:\n"
                 f"Algorithm: {algorithm}\n"
                 f"Possible patterns: {self.pattern_count}\n"
                 f"Comp. time: {self.comp_time}s\n"
                 f"Running..."
        )

        self.draw_pattern(patterns)

    def stop_visualization(self):
        self.is_visualizing = False
        self.summary_label.config(text="Summary:\nVisualization stopped.")

    def draw_dots(self, pattern):
        for dot_number, (x, y) in DOT_POSITIONS.items():
            outline_color = "white"
            small_dot_color = "white"

            if dot_number in pattern:
                outline_color = ACTIVE_COLOR
                small_dot_color = ACTIVE_COLOR

            self.delete_queue.append(self.canvas.create_oval(
                x - OUTER_DOT_RADIUS,
                y - OUTER_DOT_RADIUS,
                x + OUTER_DOT_RADIUS,
                y + OUTER_DOT_RADIUS,
                fill="grey",
                outline=outline_color,
                width=2,
            ))

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
            painting_time = time.time() - self.start_time

            self.summary_label.config(
                text=f"Summary:\n"
                     f"Algorithm: {self.algorithm_var.get()}\n"
                     f"Possible patterns: {self.pattern_count}\n"
                     f"Comp. time: {self.comp_time}s\n"
                     f"Painting Time: {painting_time:.4f}s\n"
            )
            return

        for to_delete in self.delete_queue:
            self.canvas.delete(to_delete)

        self.delete_queue.clear()
        self.canvas.delete("pattern_line")

        pattern = patterns.pop(0)

        for index in range(len(pattern) - 1):
            current_dot = pattern[index]
            next_dot = pattern[index + 1]

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

        delay = self.speed_var.get()
        self.root.after(delay, lambda: self.draw_pattern(patterns))


root = tk.Tk()
app = PatternVisualizer(root)
root.mainloop()