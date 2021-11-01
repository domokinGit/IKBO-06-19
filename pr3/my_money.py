

class MyMoney:
    def __init__(self):
        self.level = 1
        self.number = 1
        self.money = 0
        self.now_money = 0
        self.fix_money = 0
        self.true_answer = False
        
    def add_money(self):
        self.money = self.money + self.now_money
        return self.money

    def money_level(self):
        if not(type(new_level) == int):
            raise TypeError
        if not(type(new_number) == int):
            raise TypeError
        if not(type(new_true_answer) == bool):
            raise TypeError
        if new_level > 3 or new_level < 1 or new_number > 5 or new_number < 1:
            raise ValueError
        self.level = new_level
        self.number = new_number
        self.true_answer = new_true_answer
        if self.number == 5 and self.true_answer == True:
            if self.level == 1:
                self.fix_money = 10000
            if self.level == 2:
                self.fix_money = 50000
            if self.level == 3:
                self.fix_money = 1000000
        return self.fix_money

    def money_now(self, new_level, new_number, new_true_answer):
       if not(type(new_level) == int):
            raise TypeError
        if not(type(new_number) == int):
            raise TypeError
        if not(type(new_true_answer) == bool):
            raise TypeError
        if new_level > 3 or new_level < 1 or new_number > 5 or new_number < 1:
            raise ValueError
        self.level = new_level
        self.number = new_number
        self.true_answer = new_true_answer
        if self.true_answer == True:
            if self.level == 1:
                self.now_money = 10000
            if self.level == 2:
                self.now_money = 90000
            if self.level == 3:
                self.now_money = 100000
        else:
            self.now_money = 0
        return self.now_money
