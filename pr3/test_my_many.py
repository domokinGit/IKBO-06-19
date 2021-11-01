# -*- coding: utf-8 -*-
import unittest
from my_money import MyMoney


class TestMyMany(unittest.TestCase):

    def test_money_level_equal(self):
        money1 = MyMoney()
        self.assertEquals(money1.money_level(1, 5, True), 10000)
        self.assertEquals(money1.money_level(2, 5, True), 50000)
        self.assertEquals(money1.money_level(3, 5, True), 1000000)
        money1.fix_money = 100
        self.assertEquals(money1.money_level(1, 5, False), 100)
        self.assertEquals(money1.money_level(2, 1, True), 100)
        money1.fix_money = 200
        self.assertEquals(money1.money_level(3, 5, False), 200)
        self.assertEquals(money1.money_level(2, 2, True), 200)

    def test_money_level_instance(self):
        money2 = MyMoney()
        self.assertIsInstance(money2.money_level(3, 5, True), int)
        self.assertIsInstance(money2.money_level(1, 1, True), int)

    def test_money_level_type_error(self):
        money3 = MyMoney()
        self.assertRaises(TypeError, money3.money_level, '1', 2, True)
        self.assertRaises(TypeError, money3.money_level, 3, '23', True)
        self.assertRaises(TypeError, money3.money_level, 2, 1, 'True')

    def test_money_level_value_error(self):
        money4 = MyMoney()
        self.assertRaises(ValueError, money4.money_level, 4, 1, True)
        self.assertRaises(ValueError, money4.money_level, 1, 6, True)
        self.assertRaises(ValueError, money4.money_level, 4, 6, True)

    def test_money_now_equal(self):
        money5 = MyMoney()
        self.assertEquals(money5.money_now(1, 1, True), 10000)
        self.assertEquals(money5.money_now(2, 3, True), 90000)
        self.assertEquals(money5.money_now(3, 4, True), 100000)
        self.assertEquals(money5.money_now(1, 5, False), 0)
        self.assertEquals(money5.money_now(2, 5, False), 0)
        self.assertEquals(money5.money_now(3, 5, False), 0)

    def test_money_now_type_error(self):
        money6 = MyMoney()
        self.assertRaises(TypeError, money6.money_now, 2, '34', True)
        self.assertRaises(TypeError, money6.money_now, 3, 3, 'False')
        self.assertRaises(TypeError, money6.money_now, 1, '17', True)

    def test_money_now_value_error(self):
        money7 = MyMoney()
        self.assertRaises(ValueError, money7.money_now, 4, 1, True)
        self.assertRaises(ValueError, money7.money_now, 1, 6, True)
        self.assertRaises(ValueError, money7.money_now, 4, 6, False)


if __name__ == "__main__":
        unittest.main()