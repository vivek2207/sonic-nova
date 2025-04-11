"""Tests for the settings module."""

import unittest
from sonic_nova.config.settings import (
    INPUT_SAMPLE_RATE,
    OUTPUT_SAMPLE_RATE,
    CHANNELS,
    FORMAT,
    CHUNK_SIZE,
    DEFAULT_REGION,
    DEFAULT_MODEL_ID,
    set_debug,
    is_debug
)

class TestSettings(unittest.TestCase):
    """Test cases for settings module."""

    def setUp(self):
        """Set up test environment."""
        set_debug(False)

    def tearDown(self):
        """Clean up test environment."""
        set_debug(False)

    def test_audio_settings(self):
        """Test audio configuration settings."""
        self.assertEqual(INPUT_SAMPLE_RATE, 16000)
        self.assertEqual(OUTPUT_SAMPLE_RATE, 24000)
        self.assertEqual(CHANNELS, 1)
        self.assertEqual(CHUNK_SIZE, 1024)
        self.assertIsNotNone(FORMAT)

    def test_aws_settings(self):
        """Test AWS configuration settings."""
        self.assertEqual(DEFAULT_REGION, 'us-east-1')
        self.assertEqual(DEFAULT_MODEL_ID, 'amazon.nova-sonic-v1:0')

    def test_debug_settings(self):
        """Test debug mode settings."""
        # Test initial state
        self.assertFalse(is_debug())
        
        # Test setting debug mode
        set_debug(True)
        self.assertTrue(is_debug())
        
        # Test turning off debug mode
        set_debug(False)
        self.assertFalse(is_debug())

if __name__ == '__main__':
    unittest.main() 