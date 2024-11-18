from distutils.command.config import config
from operator import truediv

from quiz_brain import QuizBrain
THEME_COLOR = "#6A9C89"
from tkinter import *
class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,pady=20,padx=20)
        self.score_label=Label(text="score:0",fg="white",bg=THEME_COLOR,font=("Ariel",18,"italic"))
        self.score_label.grid(column=0,row=0,columnspan=2)

        self.canvas=Canvas(bg="white", width=400, height=240)
        self.question_text=self.canvas.create_text(200,120,text="hi",font=("Ariel",20,"italic"),fill=THEME_COLOR,width=370)
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)

        rightimg = PhotoImage(file="images/true.png")
        self.right_button = Button(image=rightimg, highlightthickness=0,command=self.check_true)
        self.right_button.grid(column=0, row=2)

        wrongimg = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrongimg, highlightthickness=0,command=self.check_false)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_ques()

        self.window.mainloop()
    def get_next_ques(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score : {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the quiz")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
    def check_true(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def check_false(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_ques)