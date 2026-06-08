import tkinter as tk
from PatternSolver import PatternSolver
import time
import customtkinter

solver = PatternSolver()

WINDOW_SIZE = 600
INNER_DOT_RADIUS = 10
OUTER_DOT_RADIUS = 50
ACTIVE_COLOR = "#00adff"

DOT_POSITIONS = {
    1: (100, 100), 2: (300, 100), 3: (500, 100),
    4: (100, 300), 5: (300, 300), 6: (500, 300),
    7: (100, 500), 8: (300, 500), 9: (500, 500),
}


class PatternVisualizer:
    def __init__(self, app):
        self.is_visualizing = False
        self.app = app

        self.app.title("Android Pattern - Lock Bruteforce Visualizer")
        self.app.geometry("1200x600")
        self.app.resizable(False, False)

        self.delete_queue = []
        self.pattern_count = 0
        self.start_time = 0
        self.comp_time = 0

        self.algorithm_var = tk.StringVar(value="DFS")
        self.speed_var = tk.IntVar(value=50)

        self.app.grid_columnconfigure(0, weight=0)
        self.app.grid_columnconfigure(1, weight=1)
        self.app.grid_rowconfigure(0, weight=1)

        self.canvas = customtkinter.CTkCanvas(
            self.app,
            width=WINDOW_SIZE,
            height=WINDOW_SIZE,
            bg="lightgrey",
        )
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.draw_dots([])

        self.controls = customtkinter.CTkFrame(
            self.app,
            width=WINDOW_SIZE,
            height=WINDOW_SIZE,
            fg_color="#222222"
        )
        self.controls.grid(row=0, column=1, sticky="nsew")
        self.controls.grid_columnconfigure(0, weight=1)

        self.radio_frame = customtkinter.CTkFrame(self.controls, fg_color="transparent")
        self.input_frame = customtkinter.CTkFrame(self.controls, fg_color="transparent")
        self.button_frame = customtkinter.CTkFrame(self.controls, fg_color="transparent")

        self.title_label = customtkinter.CTkLabel(
            self.controls,
            text="Pattern Visualizer",
            font=("Arial", 24, "bold"),
        )

        self.algorithm_label = customtkinter.CTkLabel(
            self.radio_frame,
            text="Solving method:",
            font=("Arial", 20),
        )

        self.dfs_radio = customtkinter.CTkRadioButton(
            self.radio_frame,
            text="DFS",
            variable=self.algorithm_var,
            value="DFS",
            width=70,
        )

        self.bfs_radio = customtkinter.CTkRadioButton(
            self.radio_frame,
            text="BFS",
            variable=self.algorithm_var,
            value="BFS",
            width=70,
        )

        self.min_label = customtkinter.CTkLabel(
            self.input_frame,
            text="Minimum length:",
            font=("Arial", 14),
        )

        self.max_label = customtkinter.CTkLabel(
            self.input_frame,
            text="Maximum length:",
            font=("Arial", 14),
        )

        self.start_entry = customtkinter.CTkEntry(
            self.input_frame,
            font=("Arial", 16),
            width=80,
            placeholder_text="4",
            justify="center",
        )

        self.end_entry = customtkinter.CTkEntry(
            self.input_frame,
            font=("Arial", 16),
            placeholder_text="9",
            width=80,
            justify="center",
        )

        self.speed_label = customtkinter.CTkLabel(
            self.controls,
            text="Visualization speed:",
            font=("Arial", 14),
        )

        self.speed_slider = customtkinter.CTkSlider(
            self.controls,
            from_=200,
            to=1,
            variable=self.speed_var,
            width=250,
        )

        self.start_button = customtkinter.CTkButton(
            self.button_frame,
            text="Start",
            font=("Arial", 16),
            width=100,
            command=self.start_visualization,
        )

        self.stop_button = customtkinter.CTkButton(
            self.button_frame,
            text="Stop",
            font=("Arial", 16),
            width=100,
            command=self.stop_visualization,
        )

        self.summary_label = customtkinter.CTkLabel(
            self.controls,
            text="Summary:\nWaiting for start...",
            font=("Arial", 13),
        )

        self.progress_bar = customtkinter.CTkProgressBar(
            self.controls,
        )

        self.title_label.grid(row=0, column=0, pady=(35, 30))

        self.radio_frame.grid(row=1, column=0, pady=(0, 30))
        self.algorithm_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))
        self.dfs_radio.grid(row=1, column=0, padx=20)
        self.bfs_radio.grid(row=1, column=1, padx=20)

        self.input_frame.grid(row=2, column=0, pady=(0, 30))
        self.min_label.grid(row=0, column=0, padx=10, pady=8, sticky="e")
        self.start_entry.grid(row=0, column=1, padx=10, pady=8)
        self.max_label.grid(row=1, column=0, padx=10, pady=8, sticky="e")
        self.end_entry.grid(row=1, column=1, padx=10, pady=8)

        self.speed_label.grid(row=3, column=0, pady=(0, 10))
        self.speed_slider.grid(row=4, column=0, pady=(0, 30))

        self.button_frame.grid(row=5, column=0, pady=(0, 30))
        self.start_button.grid(row=0, column=0, padx=15)
        self.stop_button.grid(row=0, column=1, padx=15)

        self.summary_label.grid(row=6, column=0)
        self.progress_bar.grid(row=7, column=0)
        self.progress_bar.set(0)

    def validate_inputs(self):
        try:
            start = int(self.start_entry.get())
            end = int(self.end_entry.get())

            if start < 1 or end < 1:
                self.summary_label.configure(text="Error: values must be at least 1.")
                return None, None

            if start > 9 or end > 9:
                self.summary_label.configure(text="Error: maximum value is 9.")
                return None, None

            if start > end:
                self.summary_label.configure(text="Error: min cannot be greater than max.")
                return None, None

            return start, end

        except ValueError:
            self.summary_label.configure(text="Error: please enter valid numbers.")
            return 4, 9

    def start_visualization(self):
        if self.is_visualizing:
            return

        start, end = self.validate_inputs()
        self.start_button["state"] = "disabled"

        if start is None or end is None:
            return

        self.is_visualizing = True
        self.start_time = time.time()

        algorithm = self.algorithm_var.get()

        if algorithm == "DFS":
            res_object = solver.brute_dfs(start, end)
            patterns = res_object["patterns"]
            self.comp_time = round(res_object["comp_time"], 4)
        else:
            res_object = solver.brute_bfs(start, end)
            patterns = res_object["patterns"]
            self.comp_time = round(res_object["comp_time"], 4)

        self.pattern_count = len(patterns)

        self.summary_label.configure(
            text=f"Summary:\n"
                 f"Algorithm: {algorithm}\n"
                 f"Possible patterns: {self.pattern_count}\n"
                 f"Comp. time: {self.comp_time}s\n"
                 f"Running..."
        )

        self.draw_pattern(patterns)

    def stop_visualization(self):
        self.is_visualizing = False
        self.summary_label.configure(text="Summary:\nVisualization stopped.")

    def draw_dots(self, pattern):
        for dot_number, (x, y) in DOT_POSITIONS.items():
            outline_color = ACTIVE_COLOR if dot_number in pattern else "white"
            small_dot_color = ACTIVE_COLOR if dot_number in pattern else "white"

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

            self.summary_label.configure(
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
        self.progress_bar.set(1 - (len(patterns) / self.pattern_count))

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
        self.app.after(delay, lambda: self.draw_pattern(patterns))


app = customtkinter.CTk()
PatternVisualizer(app)
app.mainloop()