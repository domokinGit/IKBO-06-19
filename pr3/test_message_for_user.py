# -*- coding: utf-8 -*-
import unittest
from message_for_user import Message


class TestMessage(unittest.TestCase):

    def setUp(self):
        self.test_message = Message()

    def test_message_about_money_type(self):
        self.assertRaises(TypeError, self.test_message.message_about_money, 132.0)
        self.assertRaises(TypeError, self.test_message.message_about_money, True)
        self.assertRaises(TypeError, self.test_message.message_about_money, '123')

    def test_message_about_money_instance(self):
        self.assertIsInstance(self.test_message.message_about_money(100000), str)
        self.assertIsInstance(self.test_message.message_about_money(1000000), str)

    def test_message_about_rigth_type(self):
        self.assertRaises(TypeError, self.test_message.message_about_rigth, 400)
        self.assertRaises(TypeError, self.test_message.message_about_rigth, 'False')
        self.assertRaises(TypeError, self.test_message.message_about_rigth, 123.0)

    def test_message_about_rigth_instance(self):
        self.assertIsInstance(self.test_message.message_about_rigth(True), str)
        self.assertIsInstance(self.test_message.message_about_rigth(False), str)

    def test_message_about_correct_type(self):
        self.assertRaises(TypeError, self.test_message.message_about_correct, 234)
        self.assertRaises(TypeError, self.test_message.message_about_correct, 1000)
        self.assertRaises(TypeError, self.test_message.message_about_correct, 'True')

    def test_message_about_correct_instance(self):
        self.assertIsInstance(self.test_message.message_about_correct(True), str)
        self.assertIsInstance(self.test_message.message_about_correct(False), str)


if __name__ == "__main__":
    unittest.main()