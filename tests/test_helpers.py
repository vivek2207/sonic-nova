"""Tests for the helpers module."""

import unittest
import asyncio
import time
from unittest.mock import patch
from sonic_nova.utils.helpers import debug_print, time_it, time_it_async
from sonic_nova.config.settings import set_debug

class TestHelpers(unittest.TestCase):
    """Test cases for helpers module."""

    def setUp(self):
        """Set up test environment."""
        set_debug(False)

    @patch('builtins.print')
    def test_debug_print_when_debug_disabled(self, mock_print):
        """Test debug_print when debug is disabled."""
        debug_print("Test message")
        mock_print.assert_not_called()

    @patch('builtins.print')
    def test_debug_print_when_debug_enabled(self, mock_print):
        """Test debug_print when debug is enabled."""
        set_debug(True)
        debug_print("Test message")
        mock_print.assert_called_once_with("[DEBUG] Test message")

    def test_time_it(self):
        """Test time_it decorator."""
        @time_it("test_function")
        def test_function():
            time.sleep(0.1)
            return "test"

        result = test_function()
        self.assertEqual(result, "test")

    @patch('sonic_nova.utils.helpers.debug_print')
    def test_time_it_with_debug(self, mock_debug_print):
        """Test time_it decorator with debug enabled."""
        set_debug(True)
        
        @time_it("test_function")
        def test_function():
            time.sleep(0.1)
            return "test"

        test_function()
        mock_debug_print.assert_called()

    async def async_test_function(self):
        """Async test function."""
        await asyncio.sleep(0.1)
        return "test"

    @patch('sonic_nova.utils.helpers.debug_print')
    def test_time_it_async(self, mock_debug_print):
        """Test time_it_async decorator."""
        set_debug(True)
        
        @time_it_async("async_test_function")
        async def decorated_function():
            return await self.async_test_function()

        result = asyncio.run(decorated_function())
        self.assertEqual(result, "test")
        mock_debug_print.assert_called()

if __name__ == '__main__':
    unittest.main() 