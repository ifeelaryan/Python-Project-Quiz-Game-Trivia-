import tkinter as tk
from tkinter import messagebox, ttk
import random

# Try to import winsound for sound effects (Windows only)
try:
    import winsound
    SOUND_AVAILABLE = True
except ImportError:
    SOUND_AVAILABLE = False

# Question Bank
questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "def"
    },
    {
        "question": "What is the output of: print(type([]))?",
        "options": ["<class 'list'>", "<class 'dict'>", "<class 'tuple'>", "<class 'set'>"],
        "answer": "<class 'list'>"
    },
    {
        "question": "Which module is used to generate random numbers in Python?",
        "options": ["random", "math", "time", "os"],
        "answer": "random"
    },
    {
        "question": "What is the correct syntax to output 'Hello World' in Python?",
        "options": ["echo('Hello World')", "print('Hello World')", "printf('Hello World')", "println('Hello World')"],
        "answer": "print('Hello World')"
    },
    {
        "question": "Which data type is immutable in Python?",
        "options": ["List", "Dictionary", "Tuple", "Set"],
        "answer": "Tuple"
    }
]

random.shuffle(questions)


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz - Gaming Mode 🎮")
        self.root.geometry("600x450")
        self.root.configure(bg="#020617")

        self.index = 0
        self.score = 0
        self.total_questions = len(questions)
        self.selected_option = None

        # Title
        tk.Label(root, text="PYTHON TRIVIA QUEST",
                 font=("Consolas", 20, "bold"),
                 fg="#22c55e", bg="#020617").pack(pady=10)

        # Question Label
        self.question_label = tk.Label(
            root,
            text="",
            font=("Consolas", 14),
            fg="#e5e7eb",
            bg="#020617",
            wraplength=550,
            justify="left"
        )
        self.question_label.pack(pady=10)

        # Options
        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(
                root,
                text="",
                font=("Consolas", 12),
                width=40,
                relief="flat",
                anchor="w",
                bg="#111827",
                fg="#e5e7eb",
                activebackground="#1f2937",
                activeforeground="#22c55e",
                command=lambda idx=i: self.option_clicked(idx)
            )
            btn.pack(pady=4)
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#1f2937"))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg="#111827"))
            self.option_buttons.append(btn)

        # Bottom UI container
        bottom_frame = tk.Frame(root, bg="#020617")
        bottom_frame.pack(side="bottom", fill="x", pady=15)

        # Progress bar styling
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "green.Horizontal.TProgressbar",
            troughcolor="#020617",
            background="#22c55e"
        )

        # Progress bar
        self.progress = ttk.Progressbar(
            bottom_frame,
            style="green.Horizontal.TProgressbar",
            orient="horizontal",
            length=350,
            mode="determinate",
            maximum=self.total_questions
        )
        self.progress.pack(side="left", padx=10)

        self.progress_label = tk.Label(
            bottom_frame,
            text=f"0 / {self.total_questions}",
            font=("Consolas", 11),
            fg="#9ca3af",
            bg="#020617"
        )
        self.progress_label.pack(side="left")

        # Next button
        self.next_button = tk.Button(
            bottom_frame,
            text="NEXT ▶",
            font=("Consolas", 12, "bold"),
            bg="#22c55e",
            fg="#020617",
            relief="flat",
            activebackground="#16a34a",
            command=self.next_question,
            state=tk.DISABLED
        )
        self.next_button.pack(side="right", padx=15)

        self.load_question()

    # 🎧 Sound Effects
    def play_click(self): 
        if SOUND_AVAILABLE: winsound.Beep(700, 50)

    def play_correct(self): 
        if SOUND_AVAILABLE: winsound.Beep(1000, 150)

    def play_wrong(self): 
        if SOUND_AVAILABLE: winsound.Beep(300, 200)

    # ✨ Visual Effects
    def flash_bg(self, color):
        original = "#020617"
        self.root.config(bg=color)
        self.root.after(150, lambda: self.root.config(bg=original))

    def shake(self):
        x, y = self.root.winfo_x(), self.root.winfo_y()
        for offset in [10, -10, 8, -8, 4, -4, 0]:
            self.root.geometry(f"+{x+offset}+{y}")
            self.root.update()

    def animate_question(self):
        # Fade text from black to bright
        def fade(step=0):
            if step <= 20:
                gray = int(step * (229 / 20))
                color = f"#{gray:02x}{gray:02x}{gray:02x}"
                self.question_label.config(fg=color)
                self.root.after(20, fade, step + 1)
        fade()

    # 🔥 Quiz Logic
    def load_question(self):
        q = questions[self.index]
        self.selected_option = None
        self.next_button.config(state=tk.DISABLED)

        self.question_label.config(text=q["question"])
        self.animate_question()

        for i, option in enumerate(q["options"]):
            self.option_buttons[i].config(
                text=f"{chr(65+i)}) {option}",
                bg="#111827", fg="#e5e7eb"
            )

    def option_clicked(self, idx):
        self.play_click()
        self.selected_option = idx

        for i, btn in enumerate(self.option_buttons):
            if i == idx:
                btn.config(bg="#22c55e", fg="#020617")
            else:
                btn.config(bg="#111827", fg="#e5e7eb")

        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        if self.selected_option is None:
            return

        q = questions[self.index]
        chosen = q["options"][self.selected_option]

        # Check Answer
        if chosen == q["answer"]:
            self.score += 1
            self.play_correct()
            self.flash_bg("#052e16")
        else:
            self.play_wrong()
            self.flash_bg("#450a0a")
            self.shake()

        self.index += 1
        self.progress["value"] = self.index
        self.progress_label.config(text=f"{self.index} / {self.total_questions}")

        if self.index < self.total_questions:
            self.load_question()
        else:
            self.end_quiz()

    def end_quiz(self):
        message = f"Score: {self.score}/{self.total_questions}\n\n"
        if self.score == self.total_questions:
            message += "🔥 PERFECT! Python God Mode!"
        elif self.score >= self.total_questions // 2:
            message += "⚔️ Good Work! Keep Practicing!"
        else:
            message += "💀 Try Again to Level Up!"

        messagebox.showinfo("Game Over!", message)
        self.root.destroy()


# Run Game
root = tk.Tk()
QuizApp(root)
root.mainloop()
