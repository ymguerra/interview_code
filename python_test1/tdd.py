import unittest


class Calculator:
    def __init__(self):
        self.value = 0


class TestMyCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_initial_value(self):
        self.assertEqual(0, self.calc.value)
