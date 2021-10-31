# -*- coding: utf-8 -*-
class Question_and_answer:
    def __init__(self):
        self.level = 1
        self.number = 1
        self.question = "2 + 2 ?"
        self.answer1 = "a"
        self.answer2 = "b"
        self.answer3 = "c"
        self.answer4 = "d"
        self.answer_true = 'a'

    def set_ques_and_answ(self, new_level, new_number):
        if not(type(new_level) == int):
            raise TypeError
        if not(type(new_number) == int):
            raise TypeError
        if new_level > 3 or new_level < 1 or new_number > 5 or new_number < 1:
            raise ValueError
        self.level = new_level
        self.number = new_number
        if self.level == 1:
            if self.number == 1:
               self.question = 'Кем был мужчина, послуживший моделью для картины «Американская готика» Гранта Вуда?\n'
               self.answer1 = 'a. Коммивояжером\n'
               self.answer2 = 'b. Местным шерифом\n'
               self.answer3 = 'c. Его зубным врачом\n'
               self.answer4 = 'd. Его мясником\n'
               self.answer_true = 'c'
            elif self.number == 2:
                self.question = 'Какое насекомое вызвало короткое замыкание в ранней версии вычислительной машины?\n'
                self.answer1 = 'a. Мотылек\n'
                self.answer2 = 'b. Таракан\n'
                self.answer3 = 'c. Муха\n'
                self.answer4 = 'd. Японский хрущик\n'
                self.answer_true = 'c'
            elif self.number == 3:
                self.question = 'Из каких плодов можно получить копру?\n'
                self.answer1 = 'a. Ананас\n'
                self.answer2 = 'b. Вишня\n'
                self.answer3 = 'c. Кокос\n'
                self.answer4 = 'd. Абрикос\n'
                self.answer_true = 'a'
            elif self.number == 4:
                self.question = 'Под каким названием известна единица с последующими ста нулями?\n'
                self.answer1 = 'a. Гугол\n'
                self.answer2 = 'b. Мегатрон\n'
                self.answer3 = 'c. Гигабит\n'
                self.answer4 = 'd. Наномоль\n'
                self.answer_true = 'a'
            else:
                self.question = 'Какой химический элемент составляет более половины массы тела человека?\n'
                self.answer1 = 'a. Углерод\n'
                self.answer2 = 'a. Углерод\n'
                self.answer3 = 'c. Кислород\n'
                self.answer4 = 'd. Железо\n'
                self.answer_true = 'c'
        if self.level == 2:
            if self.number == 1:
                self.question = 'Какую часть тела также называют «атлант»?\n'
                self.answer1 = 'a. Головной мозг\n'
                self.answer2 = 'b. Шестая пара ребер\n'
                self.answer3 = 'c. Шейный позвонок\n'
                self.answer4 = 'd. Часть плеча\n'
                self.answer_true = 'c'
            elif self.number == 2:
                self.question = 'Сколько кубиков в кубике Рубика?\n'
                self.answer1 = 'a. 22\n'
                self.answer2 = 'b. 24\n'
                self.answer3 = 'c. 26\n'
                self.answer4 = 'd. 28\n'
                self.answer_true = 'c'
            elif self.number == 3:
                self.question = 'Что изобразил последний,побывавший на Луне человек, на ее поверхности?\n'
                self.answer1 = 'a. Символ мира\n'
                self.answer2 = 'b. Инициалы дочери\n'
                self.answer3 = 'c. Боже, храни Америку\n'
                self.answer4 = 'd. Здесь был Юджин\n'
                self.answer_true = 'b'
            elif self.number == 4:
                self.question = 'Какого цвета крайнее правое кольцо в олимпийской символике?\n'
                self.answer1 = 'a. Красное\n'
                self.answer2 = 'b. Синее\n'
                self.answer3 = 'c. Желтое\n'
                self.answer4 = 'd. Зеленое\n'
                self.answer_true = 'a'
            else:
                self.question = 'Что изображено на заднем плане картины Леонардо да Винчи «Мона Лиза» ?\n'
                self.answer1 = 'a. Драпировка\n'
                self.answer2 = 'b. Пейзаж\n'
                self.answer3 = 'c. Город\n'
                self.answer4 = 'd. Стадо овец\n'
                self.answer_true = 'b'
        if self.level == 3:
            if self.number == 1:
                self.question = 'Что означает гавайское слово «вики»?\n'
                self.answer1 = 'a. Простой\n'
                self.answer2 = 'b. Быстрый\n'
                self.answer3 = 'c. Изученный\n'
                self.answer4 = 'd. Маленький\n'
                self.answer_true = 'b'
            elif self.number == 2:
                self.question = 'Одним из направлений какой религиозной философии является учение дзен?\n'
                self.answer1 = 'a. Даосизм\n'
                self.answer2 = 'b. Индуизм\n'
                self.answer3 = 'c. Иудаизм\n'
                self.answer4 = 'd. Буддизм\n'
                self.answer_true = 'a'
            elif self.number == 3:
                self.question = 'Какую страну не пересекает экватор?\n'
                self.answer1 = 'a. Кения\n'
                self.answer2 = 'b. Панама\n'
                self.answer3 = 'c. Бразилия\n'
                self.answer4 = 'd. Индонезия\n'
                self.answer_true = 'b'
            elif self.number == 4:
                self.question = 'Кто из перечисленных был пажом во времена Екатерины II?\n'
                self.answer1 = 'a. Д. И. Фонвизин\n'
                self.answer2 = 'b. Г. Р. Державин\n'
                self.answer3 = 'c. А. Н. Радищев\n'
                self.answer4 = 'd. Н. М. Карамзин\n'
                self.answer_true = 'c'
            else:
                self.question = 'Что дало название джинсам?\n'
                self.answer1 = 'a. Наименование места\n'
                self.answer2 = 'b. Фамилия человека\n'
                self.answer3 = 'c. Название растения\n'
                self.answer4 = 'd. Название компании\n'
                self.answer_true = 'a'
        return self.question + self.answer1 + self.answer2 + self.answer3 + self.answer4
