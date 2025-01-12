import unittest

from src.add import add


class TestBasic(unittest.TestCase):
    def test_basic(self):
        # Arrange
        left = 1
        right = 2
        expected_sum = 3

        # Act
        sum_value = add(left, right)

        # Assert
        self.assertEqual(sum_value, expected_sum)

