import html     # import html package to change text of questions


class Question:     # Question class - structure a object with question and answer
    def __init__(self, q_text, q_answer):
        self.text = q_text      # question string
        self.answer = q_answer  # boolean as an answer


class QuizBrain:        # QuizBrain class - checking answer method, get new question method, and analizing number of
    # question still to answer
    def __init__(self, q_list):     # init method requires question-answer object's list
        self.question_number = 0    # initial number of question
        self.score = 0      # initial score value
        self.question_list = q_list     # object list set as item of QuizBrain class
        self.current_question = None    # current question item placeholder

    def still_has_questions(self):      # method checking if there are still question to be asked
        return self.question_number < len(self.question_list)   # returns boolean - is number of question asked is
        # smaller than question list length

    def next_question(self):    # method to get new question after user's answer
        self.current_question = self.question_list[self.question_number]    # fetch question object from question list
        self.question_number += 1   # increase question's number
        q_numb = html.unescape(self.current_question.text)  # variable that is changing string's special signs
        return f"Q.{self.question_number}: {q_numb}"    # returns string value that will be shown in UI

    def check_answer(self, user_answer):  # returns boolean value if user's answer was right
        correct_answer = self.current_question.answer   # fetch answer from question object
        if user_answer.lower() == correct_answer.lower():   # check if user's answer was same as real answer
            self.score += 1
            return True
        else:
            return False
