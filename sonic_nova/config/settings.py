"""Configuration settings for the Sonic Nova application."""

import pyaudio

# Audio Configuration
INPUT_SAMPLE_RATE = 16000
OUTPUT_SAMPLE_RATE = 24000
CHANNELS = 1
FORMAT = pyaudio.paInt16
CHUNK_SIZE = 1024

# AWS Configuration
DEFAULT_REGION = 'us-east-1'
DEFAULT_MODEL_ID = 'amazon.nova-sonic-v1:0'

# Debug Configuration
_debug_mode = False

def set_debug(enabled):
    """Set the debug mode."""
    global _debug_mode
    _debug_mode = enabled

def is_debug():
    """Get the current debug mode."""
    return _debug_mode

# System Prompt
DEFAULT_SYSTEM_PROMPT = """You are a friend. The user and you will engage in a spoken dialog exchanging the transcripts of a natural real-time conversation.
When reading order numbers, please read each digit individually, separated by pauses. For example, order #1234 should be read as 'order number one-two-three-four' rather than 'order number one thousand two hundred thirty-four'.""" 