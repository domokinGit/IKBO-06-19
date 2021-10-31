# -*- coding: utf-8 -*-
import unittest
from questions_and_answers import QuestionAndAnswer


class TestQuestion(unittest.TestCase):

  def setUp(self):
    self.ques_and_answ = QuestionAndAnswer()

  def test_view_ques_and_answer_return(self):
      self.assertEquals(self.ques_and_answ.view_ques_and_answ(1, 1), 'Кем был мужчина, послуживший моделью для картины «Американская готика» Гранта Вуда?\n' + 'a. Коммивояжером\n' + 'b. Местным шерифом\n' + 'c. Его зубным врачом\n' + 'd. Его мясником\n')
      self.assertEquals(self.ques_and_answ.view_ques_and_answ(1, 2), 'Какое насекомое вызвало короткое замыкание в ранней версии вычислительной машины?\n'+ 'a. Мотылек\n' + 'b. Таракан\n' + 'c. Муха\n' + 'd. Японский хрущик\n')
      self.assertEquals(self.ques_and_answ.view_ques_and_answ(1, 3), 'Из каких плодов можно получить копру?\n' + 'a. Ананас\n' + 'b. Вишня\n' + 'c. Кокос\n' + 'd. Абрикос\n')
      self.assertEquals(self.ques_and_answ.view_ques_and_answ(1, 4), 'Под каким названием известна единица с последующими ста нулями?\n'+ 'a. Гугол\n' + 'b. Мегатрон\n' + 'c. Гигабит\n' + 'd. Наномоль\n')
      self.assertEquals(self.ques_and_answ.view_ques_and_answ(1, 5), 'Какой химический элемент составляет более половины массы тела человека?\n' + 'a. Углерод\n' + 'a. Углерод\n' + 'c. Кислород\n' + 'd. Железо\n')
      self.assertEquals(self.ques_and_answ.view_ques_and_answ(2, 1), 'Какую часть тела также называют «атлант»?\n' + 'a. Головной мозг\n' + 'b. Шестая пара ребер\n' + 'c. Шейный позвонок\n' + 'd. Часть плеча\n')
      self.assertEquals(self.ques_and_answ.view_ques_and_answ(2, 2), 'Сколько кубиков в кубике Рубика?\n' + 'a. 22\n' + 'b. 24\n' + 'c. 26\n' + 'd. 28\n')
      self.assertEquals(self.ques_and_answ.view_ques_and_answ(2, 3), 'Что изобразил последний,побывавший на Луне человек, на ее поверхности?\n'+ 'a. Символ мира\n' + 'b. Инициалы дочери\n' + 'c. Боже, храни Америку\n'+ 'd. Здесь был Юджин\n')
      self.assertEquals(self.ques_and_answ.view_ques_and_answ(2, 4), 'Какого цвета крайнее правое кольцо в олимпийской символике?\n' + 'a. Красное\n' + 'b. Синее\n' + 'c. Желтое\n' + 'd. Зеленое\n')
      self.assertEquals(self.ques_and_answ.view_ques_and_answ(2, 5), 'Что изображено на заднем плане картины Леонардо да Винчи «Мона Лиза» ?\n' + 'a. Драпировка\n' + 'b. Пейзаж\n' + 'c. Город\n' + 'd. Стадо овец\n')
      self.assertEquals(self.ques_and_answ.view_ques_and_answ(3, 1), 'Что означает гавайское слово «вики»?\n' + 'a. Простой\n' + 'b. Быстрый\n' + 'c. Изученный\n' + 'd. Маленький\n')
      self.assertEquals(self.ques_and_answ.view_ques_and_answ(3, 2), 'Одним из направлений какой религиозной философии является учение дзен?\n' + 'a. Даосизм\n' + 'b. Индуизм\n' + 'c. Иудаизм\n' + 'd. Буддизм\n')
      self.assertEquals(self.ques_and_answ.view_ques_and_answ(3, 3), 'Какую страну не пересекает экватор?\n' + 'a. Кения\n'+ 'b. Панама\n' + 'c. Бразилия\n' + 'd. Индонезия\n')
      self.assertEquals(self.ques_and_answ.view_ques_and_answ(3, 4), 'Кто из перечисленных был пажом во времена Екатерины II?\n'+ 'a. Д. И. Фонвизин\n' + 'b. Г. Р. Державин\n' + 'c. А. Н. Радищев\n'+'d. Н. М. Карамзин\n')
      self.assertEquals(self.ques_and_answ.view_ques_and_answ(3, 5), 'Что дало название джинсам?\n' + 'a. Наименование места\n'+ 'b. Фамилия человека\n' + 'c. Название растения\n'+'d. Название компании\n')

  def test_view_ques_and_answer_return_str(self):
      self.assertIsInstance(self.ques_and_answ.view_ques_and_answ(1, 1), str)
      self.assertIsInstance(self.ques_and_answ.view_ques_and_answ(1, 2), str)
      self.assertIsInstance(self.ques_and_answ.view_ques_and_answ(1, 3), str)
      self.assertIsInstance(self.ques_and_answ.view_ques_and_answ(1, 4), str)
      self.assertIsInstance(self.ques_and_answ.view_ques_and_answ(1, 5), str)
      self.assertIsInstance(self.ques_and_answ.view_ques_and_answ(2, 1), str)
      self.assertIsInstance(self.ques_and_answ.view_ques_and_answ(2, 2), str)
      self.assertIsInstance(self.ques_and_answ.view_ques_and_answ(2, 3), str)
      self.assertIsInstance(self.ques_and_answ.view_ques_and_answ(2, 4), str)
      self.assertIsInstance(self.ques_and_answ.view_ques_and_answ(2, 5), str)
      self.assertIsInstance(self.ques_and_answ.view_ques_and_answ(3, 1), str)
      self.assertIsInstance(self.ques_and_answ.view_ques_and_answ(3, 2), str)
      self.assertIsInstance(self.ques_and_answ.view_ques_and_answ(3, 3), str)
      self.assertIsInstance(self.ques_and_answ.view_ques_and_answ(3, 4), str)
      self.assertIsInstance(self.ques_and_answ.view_ques_and_answ(3, 5), str)

  def test_view_ques_and_answer_get_integer(self):
       self.assertRaises(TypeError, self.ques_and_answ.view_ques_and_answ, 1, '2')
       self.assertRaises(TypeError, self.ques_and_answ.view_ques_and_answ, '1', 2)
       self.assertRaises(TypeError, self.ques_and_answ.view_ques_and_answ, '3', '5')

  def test_view_ques_and_answer_get_integer_in_interval(self):
       self.assertRaises(ValueError, self.ques_and_answ.view_ques_and_answ, 4, 1)
       self.assertRaises(ValueError, self.ques_and_answ.view_ques_and_answ, 1, 6)
       self.assertRaises(ValueError, self.ques_and_answ.view_ques_and_answ, 4, 6)
       self.assertRaises(ValueError, self.ques_and_answ.view_ques_and_answ, 0, 0)
       self.assertRaises(ValueError, self.ques_and_answ.view_ques_and_answ, 0, 5)
       self.assertRaises(ValueError, self.ques_and_answ.view_ques_and_answ, 3, 0)

if __name__ == "__main__":
  unittest.main()