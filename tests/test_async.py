import unittest
from unittest.mock import AsyncMock, patch

from src.greeter import Greeter


class TestAsync(unittest.IsolatedAsyncioTestCase):

    @patch("src.greeter.Greeter.get_greeting_prefix", new_callable=AsyncMock)
    async def test_async(self, mock_get_greeting_prefix):
        greeter = Greeter()

        mock_get_greeting_prefix.return_value = "Hi"
        greeter.get_greeting_prefix = mock_get_greeting_prefix

        name_to_greet = "John"

        result = await greeter.greet(name_to_greet)

        self.assertEqual(result, "Hi, John!")