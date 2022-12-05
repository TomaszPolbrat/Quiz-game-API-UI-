from tkinter import *   # imports Tkinter - all items
from quiz_brain import QuizBrain    # imports QuizBrain class
from data import question_category  # imports question category data
THEME_COLOR = "#375362"     # Theme color variable


class UInterface:   # User Interface class
    def __init__(self, quiz_brain: QuizBrain):  # needed argument object created only from QuizBrain class
        self.quiz = quiz_brain  # ads a QuizBrain class
        self.window = Tk()  # ads Tkinter class and opens a window
        self.window.title = "Quiz game"     # generic game name
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)     # configure the window
        self.canvas = Canvas(width=400, height=350, bg="white", highlightthickness=0)   # ads canvas element (white)
        self.canvas.grid(column=0, row=1, columnspan=3, pady=20)    # place canvas into the grid
        self.canvas_text = self.canvas.create_text(200, 175, text="Placeholder", font=("Arial", 20, "bold"), width=350)
        # place text into the canvas item and configure its characteristics

        self.score_label = Label(text="Score = 0", font=("Arial", 12, "bold"), fg="White", bg=THEME_COLOR)
        # creates a score text label
        self.score_label.grid(column=2, row=0)  # place a score label on the grid

        self.category_label = Label(text=f"Category: {question_category}", font=("Arial", 12, "italic"), fg="White",
                                    bg=THEME_COLOR)     # creates a category label
        self.category_label.grid(column=0, row=0)       # place a category label on the grid

        self.false_image = PhotoImage(file="./images/false.png")      # variable of .png file "false"
        self.true_image = PhotoImage(file="./images/true.png")        # variable of .png file "true"

        self.button_true = Button(image=self.true_image, command=self.answer_correct, highlightthickness=0)
        # creates a "true" button feature
        self.button_true.grid(column=0, row=2)  # place button feature on a grid

        self.button_false = Button(image=self.false_image, command=self.answer_wrong, highlightthickness=0)
        # creates a "false" button feature
        self.button_false.grid(column=2, row=2)   # place button on a grid

        self.next_q()   # change a placeholder text into 1st question

        self.window.mainloop()  # refresh a window

    def next_q(self):   # function that gives new question after users answer
        self.canvas.config(bg="white")       # canvas bg color change into start color
        if self.quiz.still_has_questions():  # boolean checking if there are still question left
            self.score_label.config(text=f"Score: {self.quiz.score}")   # refresh score value
            self.canvas.itemconfig(self.canvas_text, text=self.quiz.next_question())    # refresh question text
        else:
            self.canvas.itemconfig(self.canvas_text, text=f"Congratulations, you finished the Quiz.\n"
                                                          f"Your final score was: {self.quiz.score}/"
                                                          f"{self.quiz.question_number}")
            # after last question refresh text with final score information
            self.button_true.config(command="r")    # turns of the button feature
            self.button_false.config(command="r")    # turns of the button feature

    def answer_correct(self):   # function returning boolean (compare user answer with question real answer)
        self.feedback(self.quiz.check_answer("True"))   # self.quiz.check_answer("True") as is_right argument

    def answer_wrong(self):   # function returning boolean (compare user answer with question real answer)
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_right):   # function changing the colour of canvas giving feedback after user's answer
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1500, self.next_q)    # waits 1500 ms and changes text to new question
