"""
Unit tests for the calculator 
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 6 == calculator.add(4, 2)

    def test_subtraction(self):
        assert 0 == calculator.subtract(4, 4)
