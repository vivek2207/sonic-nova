"""Event templates for the Sonic Nova application.

This module contains all the event templates used for communication with the
AWS Bedrock Nova model. The events follow a specific JSON format required by
the Nova model's API.

The module includes templates for:
- Session management (start/end)
- Content management (start/end)
- Audio input/output
- Text input/output
- Tool usage

Each template is a string that can be formatted with specific values using
the Python string formatting operator %.

Note:
    All events must be valid JSON when formatted with appropriate values.
    The events are designed to work with the Nova model's bidirectional
    streaming API.
"""

# Session events
START_SESSION_EVENT = '''{
    "event": {
        "sessionStart": {
        "inferenceConfiguration": {
            "maxTokens": 1024,
            "topP": 0.9,
            "temperature": 0.7
            }
        }
    }
}'''

SESSION_END_EVENT = '''{
    "event": {
        "sessionEnd": {}
    }
}'''

# Content events
CONTENT_START_EVENT = '''{
    "event": {
        "contentStart": {
        "promptName": "%s",
        "contentName": "%s",
        "type": "AUDIO",
        "interactive": true,
        "role": "USER",
        "audioInputConfiguration": {
            "mediaType": "audio/lpcm",
            "sampleRateHertz": 16000,
            "sampleSizeBits": 16,
            "channelCount": 1,
            "audioType": "SPEECH",
            "encoding": "base64"
            }
        }
    }
}'''

CONTENT_END_EVENT = '''{
    "event": {
        "contentEnd": {
        "promptName": "%s",
        "contentName": "%s"
        }
    }
}'''

# Audio events
AUDIO_EVENT_TEMPLATE = '''{
    "event": {
        "audioInput": {
        "promptName": "%s",
        "contentName": "%s",
        "content": "%s"
        }
    }
}'''

# Text events
TEXT_CONTENT_START_EVENT = '''{
    "event": {
        "contentStart": {
        "promptName": "%s",
        "contentName": "%s",
        "type": "TEXT",
        "role": "%s",
        "interactive": true,
            "textInputConfiguration": {
                "mediaType": "text/plain"
            }
        }
    }
}'''

TEXT_INPUT_EVENT = '''{
    "event": {
        "textInput": {
        "promptName": "%s",
        "contentName": "%s",
        "content": "%s"
        }
    }
}'''

# Tool events
TOOL_CONTENT_START_EVENT = '''{
    "event": {
        "contentStart": {
            "promptName": "%s",
            "contentName": "%s",
            "interactive": false,
            "type": "TOOL",
            "role": "TOOL",
            "toolResultInputConfiguration": {
                "toolUseId": "%s",
                "type": "TEXT",
                "textInputConfiguration": {
                    "mediaType": "text/plain"
                }
            }
        }
    }
}'''

# Prompt events
PROMPT_END_EVENT = '''{
    "event": {
        "promptEnd": {
        "promptName": "%s"
        }
    }
}''' 