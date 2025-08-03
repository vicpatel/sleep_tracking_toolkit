import unittest
from utils import *

class TestUtils(unittest.TestCase):
    # Test quality_label function
    def test_quality_label(self):
        # Test valid scores
        self.assertEqual(quality_label(90), 'Excellent')
        self.assertEqual(quality_label(75), 'Good')
        self.assertEqual(quality_label(55), 'Fair')
        self.assertEqual(quality_label(30), 'Poor')

        # Test invalid inputs
        self.assertEqual(quality_label(-10), 'Poor')
        # todo: should we handle out of range scores?
        # self.assertEqual(quality_label(110), 'Poor')  # Out of range
        self.assertEqual(quality_label('invalid'), 'Poor')  # Non-numeric input
        self.assertEqual(quality_label(None), 'Poor')  # None input
        self.assertEqual(quality_label([]), 'Poor')  # Empty list input
        self.assertEqual(quality_label({}), 'Poor')  # Empty dict input
        self.assertEqual(quality_label(''), 'Poor')  # Empty string input
        self.assertEqual(quality_label(' '), 'Poor')  # Space string input
        self.assertEqual(quality_label(float('nan')), 'Poor')  # NaN input
        self.assertEqual(quality_label(float('inf')), 'Poor')  # Infinity input
        self.assertEqual(quality_label(float('-inf')), 'Poor')  # Negative infinity input
        self.assertEqual(quality_label(0), 'Poor')  # Zero input

    # Test normalize_quality function
    def test_normalize_quality(self):
        # Test valid scores
        self.assertAlmostEqual(normalize_quality(50, 100), 50.0)
        self.assertAlmostEqual(normalize_quality(25, 50), 50.0)
        self.assertAlmostEqual(normalize_quality(75, 150), 50.0)

        # Test invalid inputs
        self.assertEqual(normalize_quality('invalid', 100), 0.0)
        self.assertEqual(normalize_quality([], 100), 0.0)
        self.assertEqual(normalize_quality({}, 100), 0.0)
        self.assertEqual(normalize_quality(None, 100), 0.0)
        self.assertEqual(normalize_quality(50, 'invalid'), 0.0)

    # Test compute_sleep_score function
    def test_compute_sleep_score(self):
        # Test normal case
        self.assertAlmostEqual(compute_sleep_score(8, 80), round_to(min(60 + 32, 100)))
        # Test duration > 8
        self.assertAlmostEqual(compute_sleep_score(10, 50), round_to(min(60 + 20, 100)))
        # Test duration < 8
        self.assertAlmostEqual(compute_sleep_score(4, 100), round_to(min(30 + 40, 100)))
        # Test quality_score = 0
        self.assertAlmostEqual(compute_sleep_score(8, 0), round_to(min(60 + 0, 100)))
        # Test both zero
        self.assertAlmostEqual(compute_sleep_score(0, 0), round_to(min(0 + 0, 100)))
        # Test score capped at 100
        self.assertAlmostEqual(compute_sleep_score(8, 200), round_to(100))

    # Test round_to function
    def test_round_to_none(self):
        self.assertEqual(round_to(None, 2), 0.0)

    def test_round_to_invalid_type(self):
        self.assertEqual(round_to('invalid', 2), 0.0)
        self.assertEqual(round_to([], 2), 0.0)
        self.assertEqual(round_to({}, 2), 0.0)

    def test_round_to_integer(self):
        self.assertEqual(round_to(5, 2), 5.0)
        self.assertEqual(round_to(10, 0), 10.0)

    def test_round_to_float(self):
        self.assertEqual(round_to(3.14159, 2), 3.14)
        self.assertEqual(round_to(2.71828, 3), 2.718)
        self.assertEqual(round_to(1.0, 0), 1.0)

    def test_round_to_zero(self):
        self.assertEqual(round_to(0, 2), 0.0)
        self.assertEqual(round_to(0.0, 2), 0.0)
        self.assertEqual(round_to(0.0001, 4), 0.0001)

    def test_round_to_empty_string(self):
        self.assertEqual(round_to('', 2), 0.0)
        self.assertEqual(round_to(' ', 2), 0.0)

    def test_round_to_negative(self):
        self.assertEqual(round_to(-3.14159, 2), -3.14)
        self.assertEqual(round_to(-2.71828, 3), -2.718)
        self.assertEqual(round_to(-1.0, 0), -1.0)

    def test_round_to_large_numbers(self):
        self.assertEqual(round_to(123456789.987654321, 2), 123456789.99)
        self.assertEqual(round_to(0.000000123456789, 10), 0.0000001235)
        self.assertEqual(round_to(-987654321.123456789, 3), -987654321.123)

    def test_round_to_zero_digits(self):
        self.assertEqual(round_to(3.14159, 0), 3.0)
        self.assertEqual(round_to(2.71828, 0), 3.0)
        self.assertEqual(round_to(1.0, 0), 1.0)
        self.assertEqual(round_to(0.99999, 0), 1.0)
        self.assertEqual(round_to(0.00001, 0), 0.0)
        self.assertEqual(round_to(-0.99999, 0), -1.0)
        self.assertEqual(round_to(-0.00001, 0), 0.0)

if __name__ == "__main__":
    unittest.main()