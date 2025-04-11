"""Sonic Nova - Real-time Voice Interaction with AWS Bedrock Nova Model.

This is the main entry point for the Sonic Nova application. It initializes the necessary
components for real-time voice interaction with AWS Bedrock's Nova model, including:
- Audio streaming (input from microphone and output to speakers)
- Bedrock stream management (bidirectional communication with Nova model)
- Debug mode configuration
- Error handling and graceful shutdown

The application supports the following features:
- Natural language conversation
- Order tracking queries
- Date and time information
- Real-time voice input and output

Usage:
    python nova_sonic.py [--debug]

Options:
    --debug    Enable debug mode for detailed logging
"""

import os
import asyncio
import warnings
from dotenv import load_dotenv

# Import from our modules
from sonic_nova.config.settings import (
    DEFAULT_MODEL_ID,
    DEFAULT_REGION,
    set_debug
)
from sonic_nova.core.bedrock_manager import BedrockStreamManager
from sonic_nova.core.audio_streamer import AudioStreamer

# Load environment variables from .env file
load_dotenv()

# Suppress warnings
warnings.filterwarnings("ignore")

async def main(debug=False):
    """Initialize and run the Sonic Nova application.
    
    This function sets up the core components of the application:
    1. Configures debug mode
    2. Creates and initializes the Bedrock stream manager
    3. Creates and initializes the audio streamer
    4. Starts the streaming process
    5. Handles cleanup on shutdown
    
    Args:
        debug (bool): Whether to enable debug mode. Defaults to False.
    
    Returns:
        None
    
    Raises:
        Exception: If there's an error during initialization or streaming.
    """
    # Set debug mode
    set_debug(debug)

    # Create stream manager
    stream_manager = BedrockStreamManager(
        model_id=DEFAULT_MODEL_ID,
        region=DEFAULT_REGION
    )

    # Create audio streamer
    audio_streamer = AudioStreamer(stream_manager)

    # Initialize the stream
    await stream_manager.initialize_stream()

    try:
        # This will run until the user presses Enter
        await audio_streamer.start_streaming()
        
    except KeyboardInterrupt:
        print("Interrupted by user")
    finally:
        # Clean up
        await audio_streamer.stop_streaming()

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Sonic Nova - Real-time voice interaction with AWS Bedrock Nova model'
    )
    parser.add_argument(
        '--debug',
        action='store_true',
        help='Enable debug mode for detailed logging'
    )
    args = parser.parse_args()

    # Run the main function
    try:
        asyncio.run(main(debug=args.debug))
    except Exception as e:
        print(f"Application error: {e}")
        if args.debug:
            import traceback
            traceback.print_exc()