# Sonic Nova

A Python application for real-time audio interaction with AWS Bedrock's Nova Sonic model.

## Features

- Real-time audio streaming with AWS Bedrock
- Bidirectional communication with Nova Sonic model
- Modular architecture for easy extension

## Requirements

- Python 3.8+
- AWS credentials with Bedrock access
- PyAudio
- AWS SDK Bedrock Runtime
- Python-dotenv

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/sonic-nova.git
cd sonic-nova
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your AWS credentials:
```
AWS_ACCESS_KEY_ID=your_access_key_here
AWS_SECRET_ACCESS_KEY=your_secret_key_here
AWS_DEFAULT_REGION=us-east-1
```

## Usage

Run the application with debug mode:
```bash
python nova_sonic.py --debug
```

Speak into your microphone to interact with Nova Sonic. Press Enter to stop.

## Project Structure

```
sonic_nova/
├── config/
│   ├── audio_config.py    # Audio configuration settings
│   └── __init__.py
├── utils/
│   ├── helpers.py         # Utility functions
│   └── __init__.py
└── __init__.py
```

## License

MIT 