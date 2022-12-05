from data import question_data      # gets questions and answer
from quiz_brain import QuizBrain, Question  # gets question structure and application mechanisms (checking answer,
# counting questions and generating next question
from ui import UInterface      # gets User Interface

question_bank = []  # empty list for questions
for question in question_data:      # loop: creates a list of objects that will be used (pairs of question and answer)
    new_question = Question(question["question"], question["correct_answer"])   # creates variable with
    # a question object
    question_bank.append(new_question)  # ads a new object to a list

quiz = QuizBrain(question_bank)     # creating object from QuizBrain class
quiz_UI = UInterface(quiz)     # creating object from UInterface


while quiz.still_has_questions():       # loop: until there are questions in list, gives new questions
    quiz.next_question()
