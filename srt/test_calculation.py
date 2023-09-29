import unittest

from calculation import jisuan

class TestCalculation(unittest.TestCase):
    def test_add(self):
        t = ["1","+","1"]
        result = jisuan(t)
        self.assertEqual(result, 2)
    def test_cos(self):
        t = "cos(1)"
        result = jisuan(t)
        self.assertEqual(result, 0.5403023058681398)
    def test_mulanddev(self):
        t = "3*5/3"
        result = jisuan(t)
        self.assertEqual(result,5)