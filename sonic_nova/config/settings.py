"""Configuration settings for the Sonic Nova application.

This module contains all the configuration settings for the Sonic Nova application,
including:
- Audio configuration (sample rates, channels, format, chunk size)
- AWS configuration (region, model ID)
- Debug mode settings
- System prompts

The settings in this module can be customized to modify the behavior of the application
without changing the core logic.

Note:
    Some settings (like FORMAT) are dependent on external libraries and should be
    modified with caution.
"""

import pyaudio

# Audio Configuration
INPUT_SAMPLE_RATE = 16000  # Hz, standard for speech recognition
OUTPUT_SAMPLE_RATE = 24000  # Hz, standard for Nova model output
CHANNELS = 1  # Mono audio
FORMAT = pyaudio.paInt16  # 16-bit audio
CHUNK_SIZE = 1024  # Number of frames per buffer

# AWS Configuration
DEFAULT_REGION = 'us-east-1'  # Default AWS region
DEFAULT_MODEL_ID = 'amazon.nova-sonic-v1:0'  # Nova model identifier

# Debug Configuration
_debug_mode = False  # Internal debug state

def set_debug(enabled):
    """Set the debug mode for the application.
    
    This function controls whether debug messages and timing information
    are displayed throughout the application.
    
    Args:
        enabled (bool): True to enable debug mode, False to disable
    """
    global _debug_mode
    _debug_mode = enabled

def is_debug():
    """Check if debug mode is enabled.
    
    Returns:
        bool: True if debug mode is enabled, False otherwise
    """
    return _debug_mode

# System Prompt
DEFAULT_SYSTEM_PROMPT = """You are a friend. The user and you will engage in a spoken dialog exchanging the transcripts of a natural real-time conversation.
When reading order numbers, please read each digit individually, separated by pauses. For example, order #1234 should be read as 'order number one-two-three-four' rather than 'order number one thousand two hundred thirty-four'.""" 