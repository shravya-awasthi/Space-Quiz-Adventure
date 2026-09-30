# Main game file, uses tkinter for the GUI

import tkinter as tk
from tkinter import messagebox
from questions import LEVELS
from score import save_score
from utils import get_ascii_ship

# colors I use a lot
DARK_BG = "#090b2a"
HEADER_BG = "#151a4a"
BUTTON_BG = "#242b63"


class SpaceQuizGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🚀 Space Quiz Adventure")
        self.root.geometry("800x650")
        self.root.resizable(False, False)
        self.root.configure(bg=DARK_BG)

        # game variables
        self.player = ""
        self.level = 1
        self.question_number = 0
        self.score = 0
        self.lives = 3
        self.time_left = 15
        self.timer_id = None
        self.current_question = None

        self.show_start_screen()

    def clear_screen(self):
        # remove everything from the window
        for widget in self.root.winfo_children():
            widget.destroy()

    def stop_timer(self):
        # cancel the timer if it is running
        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

    def show_start_screen(self):
        self.clear_screen()

        title = tk.Label(self.root, text="🚀 SPACE QUIZ ADVENTURE 🚀",
                         font=("Arial", 28, "bold"),
                         fg="#7df9ff", bg=DARK_BG)
        title.pack(pady=35)

        # the ascii spaceship
        art = tk.Label(self.root, text=get_ascii_ship(),
                       font=("Courier New", 14),
                       fg="#ffd166", bg=DARK_BG, justify="left")
        art.pack(pady=10)

        subtitle = tk.Label(self.root, text="Test your space knowledge!",
                            font=("Arial", 16), fg="white", bg=DARK_BG)
        subtitle.pack(pady=10)

        name_label = tk.Label(self.root, text="Enter your name:",
                              font=("Arial", 14), fg="white", bg=DARK_BG)
        name_label.pack(pady=5)

        self.name_entry = tk.Entry(self.root, font=("Arial", 16),
                                   justify="center", width=25)
        self.name_entry.pack(pady=10)
        self.name_entry.focus()

        start_button = tk.Button(self.root, text="▶ START GAME",
                                 command=self.start_game,
                                 font=("Arial", 15, "bold"),
                                 bg="#6c5ce7", fg=DARK_BG,
                                 activebackground="#a29bfe",
                                 width=18, height=1)
        start_button.pack(pady=20)

        info = tk.Label(self.root,
                        text="Level 1 → Level 2 → Level 3\n3 lives • 15 seconds per question",
                        font=("Arial", 11), fg="#b8c1ec", bg=DARK_BG)
        info.pack()

    def start_game(self):
        self.player = self.name_entry.get().strip()

        # make sure they typed a name
        if self.player == "":
            messagebox.showwarning("Missing Name", "Please enter your name.")
            return

        # reset everything for a new game
        self.level = 1
        self.question_number = 0
        self.score = 0
        self.lives = 3
        self.show_game_screen()
        self.next_question()

    def show_game_screen(self):
        self.clear_screen()

        # top bar with level, score, lives and timer
        header = tk.Frame(self.root, bg=HEADER_BG)
        header.pack(fill="x")

        self.level_label = tk.Label(header, text="",
                                    font=("Arial", 14, "bold"),
                                    fg="#7df9ff", bg=HEADER_BG)
        self.level_label.pack(side="left", padx=20, pady=12)

        self.score_label = tk.Label(header, text="",
                                    font=("Arial", 14, "bold"),
                                    fg="#ffd166", bg=HEADER_BG)
        self.score_label.pack(side="left", padx=20)

        self.lives_label = tk.Label(header, text="",
                                    font=("Arial", 14, "bold"),
                                    fg="#ff7675", bg=HEADER_BG)
        self.lives_label.pack(side="left", padx=20)

        self.timer_label = tk.Label(header, text="",
                                    font=("Arial", 14, "bold"),
                                    fg="#55efc4", bg=HEADER_BG)
        self.timer_label.pack(side="right", padx=20)

        self.question_label = tk.Label(self.root, text="",
                                       font=("Arial", 20, "bold"),
                                       fg="white", bg=DARK_BG,
                                       wraplength=700, justify="center")
        self.question_label.pack(pady=45)

        self.buttons_frame = tk.Frame(self.root, bg=DARK_BG)
        self.buttons_frame.pack()

        # make the 4 answer buttons in a 2x2 grid
        self.answer_buttons = []
        for i in range(4):
            if i < 2:
                row = 0
            else:
                row = 1

            if i % 2 == 0:
                column = 0
            else:
                column = 1

            # x=i is needed so each button remembers its own number
            button = tk.Button(self.buttons_frame, text="",
                               font=("Arial", 13, "bold"),
                               bg=BUTTON_BG, fg="red",
                               activebackground="#6c5ce7",
                               activeforeground="white",
                               width=30, height=2,
                               command=lambda x=i: self.check_answer(x))
            button.grid(row=row, column=column, padx=10, pady=10)
            self.answer_buttons.append(button)

        self.message_label = tk.Label(self.root, text="",
                                      font=("Arial", 13, "bold"),
                                      fg="#74b9ff", bg=DARK_BG)
        self.message_label.pack(pady=20)

    def next_question(self):
        self.stop_timer()

        level_questions = LEVELS[self.level]

        # check if this level is finished
        if self.question_number >= len(level_questions):
            if self.level < 3:
                self.level += 1
                self.question_number = 0
                messagebox.showinfo("Level Complete!",
                                    f"🎉 Great job!\nYou reached Level {self.level}!")
                level_questions = LEVELS[self.level]
            else:
                # no more levels so the game is over
                self.end_game()
                return

        self.current_question = level_questions[self.question_number]
        self.question_number += 1

        # update the top bar
        self.level_label.config(text=f"⭐ LEVEL {self.level}")
        self.score_label.config(text=f"🏆 SCORE: {self.score}")
        self.lives_label.config(text=f"❤️ LIVES: {self.lives}")

        self.question_label.config(text=self.current_question["question"])

        # put the options on the buttons
        options = self.current_question["options"]
        for i in range(len(options)):
            self.answer_buttons[i].config(text=options[i],
                                          state="normal",
                                          bg=BUTTON_BG)

        self.message_label.config(text="")
        self.time_left = 15
        self.update_timer()

    def update_timer(self):
        self.timer_label.config(text=f"⏱ TIME: {self.time_left}s")

        # out of time
        if self.time_left <= 0:
            self.message_label.config(text="⏰ Time's up! You lost a life.",
                                      fg="#ff7675")
            self.disable_buttons()
            self.lives -= 1
            self.lives_label.config(text=f"❤️ LIVES: {self.lives}")

            if self.lives <= 0:
                self.root.after(1000, self.end_game)
            else:
                self.root.after(1200, self.next_question)
            return

        # count down 1 second
        self.time_left -= 1
        self.timer_id = self.root.after(1000, self.update_timer)

    def check_answer(self, choice):
        self.stop_timer()

        correct = self.current_question["answer"]

        if choice == correct:
            points = self.level * 10
            self.score += points
            self.message_label.config(text=f"✅ Correct! +{points} points",
                                      fg="#55efc4")
        else:
            self.lives -= 1
            right_answer = self.current_question["options"][correct]
            self.message_label.config(text=f"❌ Wrong! Correct answer: {right_answer}",
                                      fg="#ff7675")

        self.score_label.config(text=f"🏆 SCORE: {self.score}")
        self.lives_label.config(text=f"❤️ LIVES: {self.lives}")

        self.disable_buttons()

        if self.lives <= 0:
            self.root.after(1500, self.end_game)
        else:
            self.root.after(1500, self.next_question)

    def disable_buttons(self):
        for button in self.answer_buttons:
            button.config(state="disabled")

    def end_game(self):
        self.stop_timer()

        # save the score to the file
        save_score(self.player, self.score)

        self.clear_screen()

        end_title = tk.Label(self.root, text="🌟 GAME END 🌟",
                             font=("Arial", 30, "bold"),
                             fg="#ffd166", bg=DARK_BG)
        end_title.pack(pady=45)

        well_played = tk.Label(self.root, text=f"Well played, {self.player}!",
                               font=("Arial", 18, "bold"),
                               fg="red", bg=DARK_BG)
        well_played.pack(pady=10)

        final_score = tk.Label(self.root, text=f"Final Score: {self.score}",
                               font=("Arial", 24, "bold"),
                               fg="#55efc4", bg=DARK_BG)
        final_score.pack(pady=15)

        level_reached = tk.Label(self.root, text=f"Reached Level: {self.level}",
                                 font=("Arial", 15),
                                 fg="#b8c1ec", bg=DARK_BG)
        level_reached.pack(pady=5)

        play_again_button = tk.Button(self.root, text="🔄 PLAY AGAIN",
                                      command=self.show_start_screen,
                                      font=("Arial", 14, "bold"),
                                      bg="#6c5ce7", fg="red",
                                      width=18, height=2)
        play_again_button.pack(pady=30)

        exit_button = tk.Button(self.root, text="EXIT",
                                command=self.root.destroy,
                                font=("Arial", 12),
                                bg="#d63031", fg="red", width=12)
        exit_button.pack()

    def run(self):
        self.root.mainloop()
