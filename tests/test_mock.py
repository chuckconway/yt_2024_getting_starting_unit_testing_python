import unittest
from unittest.mock import Mock

from src.numbers import add_numbers, Numbers


class TestMock(unittest.TestCase):
    def test_mock(self):
        # Arrange
        left=1
        right=2
        expected_sum = 3
        numbers = Mock(left=left, right=right)

        # Act
        summed_values = add_numbers(numbers)

        # Assert
        self.assertEqual(summed_values, expected_sum)





