"""Event templates for AWS Bedrock Nova Sonic model."""

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