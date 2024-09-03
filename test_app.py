import pytest
import streamlit as st
from unittest.mock import MagicMock

@pytest.fixture
def mock_session_state(monkeypatch):
    session_state = MagicMock()
    session_state.started = True  # Set any necessary attributes here
    monkeypatch.setattr(st, 'session_state', session_state)

def test_prediction(mock_session_state):
    from main import predict  # Import the function you want to test
    # Your test logic here
    # Example assertion (replace with actual logic)
    assert predict() == expected_result
