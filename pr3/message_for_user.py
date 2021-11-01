class Message:
    def __init__(self):
        self.correct = False
        self.right = False
        self.money = 0
        self.hint = 'a'
        self.answer1 = "a"
        self.answer2 = "b"
        self.answer3 = "c"
        self.answer4 = "d"
        self.true_answer = 'a'

    def message_about_money(self, money):
        if not(type(money) == int):
            raise TypeError
        self.money = money
        return 'Ваш счет: ' + str(self.money)

    def message_about_hint(self, answer1, answer2, answer3, answer4, true_answer):
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.true_answer = true_answer
        if self.true_answer in self.answer1:
            return "Ответ " + self.answer1 + " - неправильный ответ!\n"
        if self.true_answer in self.answer2:
            return "Ответ " + self.answer2 + " - неправильный ответ!\n"
        if self.true_answer in self.answer3:
            return "Ответ " + self.answer3 + " - неправильный ответ!\n"
        if self.true_answer in self.answer4:
            return "Ответ " + self.answer4 + " - неправильный ответ!\n"
        return "Подсказки не будет!\n"

    def message_about_correct(self, correct):
        if not(type(correct) == bool):
            raise TypeError
        self.correct = correct
        if correct:
            return "Правильный ввод"
        else:
            return "Неправильный ввод!\n" 

    def message_about_rigth(self, right):
        if not(type(right) == bool):
            raise TypeError
        self.right = right
        if right:
            return "Правильный ответ!\n"
        else:
            return "Неправильный ответ!\n"
