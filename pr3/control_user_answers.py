
class ControlUserAnswers:

    def __init__(self, answer_true, user_answer):
        self.answer_true = answer_true
        self.user_answer = user_answer
        
    def correct_answear(self):
        if self.user_answer == 'подсказка':
            return True
        if self.user_answer == 'a':
            return True
        if self.user_answer == 'b':
            return True
        if self.user_answer == 'c':
            return True
        if self.user_answer == 'd':
            return True 
        return False

    def hint_answear(self):
        if self.user_answer == 'подсказка':
            return True
        return False

    def right_answear(self):
        if self.user_answer == self.answer_true:
            return True
        return False
