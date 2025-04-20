import tkinter as tk
import random

class MultiplicationGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Multiplication Game")
        self.score = 0
        self.question_number = 0

        self.label = tk.Label(root, text="Welcome to the Multiplication Game!", font=("Arial", 16))
        self.label.pack(pady=20)

        self.question_label = tk.Label(root, font=("Arial", 14))
        self.question_label.pack()

        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack()

        self.feedback = tk.Label(root, font=("Arial", 12))
        self.feedback.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack()

        self.next_question()

    def next_question(self):
        if self.question_number < 10:
            self.a = random.randint(1, 10)
            self.b = random.randint(1, 10)
            self.question_label.config(text=f"Question {self.question_number + 1}: What is {self.a} x {self.b}?")
            self.entry.delete(0, tk.END)
            self.feedback.config(text="")
            self.question_number += 1
        else:
            self.question_label.config(text=f"Game Over! Your score: {self.score}/10")
            self.entry.pack_forget()
            self.submit_button.pack_forget()
            self.feedback.config(text="")

    def check_answer(self):
        try:
            user_answer = int(self.entry.get())
            if user_answer == self.a * self.b:
                self.feedback.config(text="Correct!", fg="green")
                self.score += 1
            else:
                self.feedback.config(text=f"Wrong. Correct answer was {self.a * self.b}.", fg="red")
        except ValueError:
            self.feedback.config(text="Please enter a valid number!", fg="orange")
            return

        self.root.after(1000, self.next_question)

# Run the GUI
root = tk.Tk()
game = MultiplicationGame(root)
root.mainloop()
