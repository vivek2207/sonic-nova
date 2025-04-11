"""Tests for the events module."""

import unittest
import json
from sonic_nova.models.events import (
    START_SESSION_EVENT,
    SESSION_END_EVENT,
    CONTENT_START_EVENT,
    CONTENT_END_EVENT,
    AUDIO_EVENT_TEMPLATE,
    TEXT_CONTENT_START_EVENT,
    TEXT_INPUT_EVENT,
    TOOL_CONTENT_START_EVENT,
    PROMPT_END_EVENT
)

class TestEvents(unittest.TestCase):
    """Test cases for events module."""

    def test_start_session_event(self):
        """Test START_SESSION_EVENT format."""
        event = json.loads(START_SESSION_EVENT)
        self.assertIn('event', event)
        self.assertIn('sessionStart', event['event'])
        self.assertIn('inferenceConfiguration', event['event']['sessionStart'])

    def test_session_end_event(self):
        """Test SESSION_END_EVENT format."""
        event = json.loads(SESSION_END_EVENT)
        self.assertIn('event', event)
        self.assertIn('sessionEnd', event['event'])

    def test_content_start_event(self):
        """Test CONTENT_START_EVENT format."""
        event_str = CONTENT_START_EVENT % ('test_prompt', 'test_content')
        event = json.loads(event_str)
        self.assertIn('event', event)
        self.assertIn('contentStart', event['event'])
        self.assertEqual(event['event']['contentStart']['promptName'], 'test_prompt')
        self.assertEqual(event['event']['contentStart']['contentName'], 'test_content')

    def test_audio_event_template(self):
        """Test AUDIO_EVENT_TEMPLATE format."""
        event_str = AUDIO_EVENT_TEMPLATE % ('test_prompt', 'test_content', 'test_audio')
        event = json.loads(event_str)
        self.assertIn('event', event)
        self.assertIn('audioInput', event['event'])
        self.assertEqual(event['event']['audioInput']['promptName'], 'test_prompt')
        self.assertEqual(event['event']['audioInput']['contentName'], 'test_content')
        self.assertEqual(event['event']['audioInput']['content'], 'test_audio')

    def test_text_content_start_event(self):
        """Test TEXT_CONTENT_START_EVENT format."""
        event_str = TEXT_CONTENT_START_EVENT % ('test_prompt', 'test_content', 'USER')
        event = json.loads(event_str)
        self.assertIn('event', event)
        self.assertIn('contentStart', event['event'])
        self.assertEqual(event['event']['contentStart']['role'], 'USER')

    def test_text_input_event(self):
        """Test TEXT_INPUT_EVENT format."""
        event_str = TEXT_INPUT_EVENT % ('test_prompt', 'test_content', 'test_text')
        event = json.loads(event_str)
        self.assertIn('event', event)
        self.assertIn('textInput', event['event'])
        self.assertEqual(event['event']['textInput']['content'], 'test_text')

    def test_tool_content_start_event(self):
        """Test TOOL_CONTENT_START_EVENT format."""
        event_str = TOOL_CONTENT_START_EVENT % ('test_prompt', 'test_content', 'test_tool_id')
        event = json.loads(event_str)
        self.assertIn('event', event)
        self.assertIn('contentStart', event['event'])
        self.assertEqual(event['event']['contentStart']['toolResultInputConfiguration']['toolUseId'], 'test_tool_id')

    def test_prompt_end_event(self):
        """Test PROMPT_END_EVENT format."""
        event_str = PROMPT_END_EVENT % 'test_prompt'
        event = json.loads(event_str)
        self.assertIn('event', event)
        self.assertIn('promptEnd', event['event'])
        self.assertEqual(event['event']['promptEnd']['promptName'], 'test_prompt')

if __name__ == '__main__':
    unittest.main() 