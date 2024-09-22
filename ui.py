from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        #setting up window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=25, padx=25, background=THEME_COLOR)

        self.score_display = Label()
        self.score_display.config(text=f"Score: 0", fg="#FFFFFF", bg=THEME_COLOR ,font=("Ariel", 15, "italic"), pady=10)
        self.score_display.grid(row=0, column=1, sticky="NE")

        self.canvas = Canvas()
        self.canvas.config(height=250, width=300, bg="#FFFFFF")
        self.question_text = self.canvas.create_text(150, 125, text="Some Question Text",width=280,  fill=THEME_COLOR,font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.get_next_question()

        self.true_image = PhotoImage(file='./images/true.png')
        self.true_button = Button(image=self.true_image)
        self.true_button.config(command=self.true_pressed)
        self.true_button.grid(row=3, column=0, sticky="SW")

        self.false_image = PhotoImage(file='./images/false.png')
        self.false_button = Button(image=self.false_image)
        self.false_button.config(command = self.false_pressed, )
        self.false_button.grid(row=3, column=1, sticky="SE")

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.reset_canvas()
        if self.quiz.still_has_questions():
            score = self.quiz.score
            self.score_display.config(text=f"Score: {score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfigure(self.question_text, text=q_text)
        else:
            self.canvas.itemconfigure(self.question_text, text= "You have reached the end of quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        # self.quiz.check_answer("true")

        check_answer = self.quiz.check_answer("true")
        self.give_feedback(check_answer)


    def false_pressed(self):
        check_answer = self.quiz.check_answer("false")
        self.give_feedback(check_answer)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="#00ff00")
        elif not is_right:
            self.canvas.config(background="#ff0000")

        self.window.after(500, self.get_next_question)

    def reset_canvas(self):
        self.canvas.config(background="#ffffff")











