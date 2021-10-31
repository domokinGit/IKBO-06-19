# -*- coding: utf-8 -*-
import unittest
from control_user_answers import ControlUserAnswers


class TestUserAnswear(unittest.TestCase):

    def test_control_user_answer_correct(self):
        user_answ_correct1 = ControlUserAnswers(' ', ' ')
        user_answ_correct1.user_answer = 'a'
        self.assertTrue(user_answ_correct1.correct_answear())
        user_answ_correct1.user_answer = 'b'
        self.assertTrue(user_answ_correct1.correct_answear())
        user_answ_correct1.user_answer = 'c'
        self.assertTrue(user_answ_correct1.correct_answear())
        user_answ_correct1.user_answer = 'd'
        self.assertTrue(user_answ_correct1.correct_answear())
        user_answ_correct1.user_answer = 'подсказка'
        self.assertTrue(user_answ_correct1.correct_answear())
        user_answ_correct1.user_answer = 'abdc'
        self.assertFalse(user_answ_correct1.correct_answear())
        user_answ_correct1.user_answer = '123'
        self.assertFalse(user_answ_correct1.correct_answear())
        user_answ_correct1.user_answer = 123
        self.assertFalse(user_answ_correct1.correct_answear())

    def test_control_user_answer_right(self):
        user_answ_correct2 = ControlUserAnswers(' ', ' ')
        user_answ_correct2.user_answer = 'a'
        user_answ_correct2.answer_true = 'a'
        self.assertTrue(user_answ_correct2.right_answear())
        user_answ_correct2.user_answer = 'a'
        user_answ_correct2.answer_true = 'b'
        self.assertFalse(user_answ_correct2.right_answear())
        user_answ_correct2.user_answer = 'a'
        user_answ_correct2.answer_true = 'aaa'
        self.assertFalse(user_answ_correct2.right_answear())

    def test_control_user_answer_hint(self):
        user_answ_correct3 = ControlUserAnswers(' ', ' ')
        user_answ_correct3.user_answer = 'подсказка'
        self.assertTrue(user_answ_correct3.hint_answear())
        user_answ_correct3.user_answer = 'под'
        self.assertFalse(user_answ_correct3.hint_answear())
        user_answ_correct3.user_answer = 'a'
        self.assertFalse(user_answ_correct3.hint_answear())
        user_answ_correct3.user_answer = 123
        self.assertFalse(user_answ_correct3.hint_answear())


if __name__ == "__main__":
  unittest.main()