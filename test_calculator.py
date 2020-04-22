

"""
Unit tests for the calculator
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 6 == calculator.add(4, 2)

    def test_subtraction(self):
        assert 0 == calculator.subtract(4, 4)

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10101010101010101010)
