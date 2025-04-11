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
    """Main function to run the application."""
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
    
    parser = argparse.ArgumentParser(description='Nova Sonic Python Streaming')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    args = parser.parse_args()

    # Run the main function
    try:
        asyncio.run(main(debug=args.debug))
    except Exception as e:
        print(f"Application error: {e}")
        if args.debug:
            import traceback
            traceback.print_exc()