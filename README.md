# Sonic Nova

A Python application for real-time voice interaction with AWS Bedrock's Nova model. This application enables natural spoken dialogue with an AI assistant, featuring order tracking and time/date information capabilities.

## Features

- Real-time voice input and output
- Natural language processing using AWS Bedrock
- Order tracking functionality
- Date and time information
- Modular and extensible architecture
- Comprehensive test suite

## Prerequisites

- Python 3.7 or higher
- AWS account with Bedrock access
- PyAudio dependencies (for audio input/output)
- AWS credentials configured

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/sonic-nova.git
cd sonic-nova
```

2. Install the package in development mode:
```bash
pip install -e .
```

3. Install test dependencies (optional):
```bash
pip install -e ".[test]"
```

## Configuration

1. Create a `.env` file in the project root with your AWS credentials:
```
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_DEFAULT_REGION=us-east-1
```

2. Customize settings in `sonic_nova/config/settings.py` if needed.

## Usage

Run the application:
```bash
python nova_sonic.py
```

Optional flags:
- `--debug`: Enable debug mode for detailed logging

## Project Structure

```
sonic_nova/
├── core/
│   ├── audio_streamer.py    # Audio I/O handling
│   └── bedrock_manager.py   # AWS Bedrock integration
├── models/
│   └── events.py           # Event templates
├── config/
│   └── settings.py         # Configuration settings
└── utils/
    └── helpers.py          # Utility functions
```

## Testing

Run the test suite:
```bash
python run_tests.py
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- AWS Bedrock team for the Nova model
- PyAudio developers
- All contributors to this project 