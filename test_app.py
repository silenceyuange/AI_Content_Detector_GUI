import unittest
from unittest.mock import patch, MagicMock
import streamlit as st
import main

class TestStreamlitApp(unittest.TestCase):

    @patch('main.st.session_state', new_callable=MagicMock)
    @patch('main.st.text_area')
    @patch('main.st.button')
    def test_predict_function(self, mock_button, mock_text_area, mock_session_state):
        # Mock return values
        mock_button.return_value = True
        mock_text_area.return_value = "This is a test input"

        # Initialize session state
        mock_session_state.started = True

        # Run the app
        main.main()

        # Check if session state was modified
        self.assertTrue(mock_session_state.started)

    @patch('main.st.session_state', new_callable=MagicMock)
    @patch('main.st.text_area')
    @patch('main.st.button')
    def test_streamlit_ui(self, mock_button, mock_text_area, mock_session_state):
        # Mock return values
        mock_button.return_value = True
        mock_text_area.return_value = "This is a test input"

        # Initialize session state
        mock_session_state.started = False

        # Run the app
        main.main()

        # Check if session state was modified
        self.assertTrue(mock_session_state.started)

if __name__ == "__main__":
    unittest.main()
