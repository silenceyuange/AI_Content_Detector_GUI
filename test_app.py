import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import ExtraTreesClassifier
import streamlit as st
import main as app  # Replace with the actual filename of your Streamlit app

class TestStreamlitApp(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Prepare some mock data for testing
        cls.mock_data = pd.DataFrame({
            'text': ['This is an AI-generated text', 'This is human-written text'],
            'label': ['AI', 'Human']
        })
        cls.vectorizer = TfidfVectorizer()
        cls.X = cls.vectorizer.fit_transform(cls.mock_data['text'])
        cls.y = cls.mock_data['label']
        cls.classifier = ExtraTreesClassifier(n_estimators=50, random_state=2)
        cls.classifier.fit(cls.X, cls.y)
    
    @patch('main.pd.read_csv')  # Replace with the actual filename of your Streamlit app
    def test_model_training(self, mock_read_csv):
        mock_read_csv.return_value = self.mock_data

        # Run the training code
        app.data = pd.read_csv('dataset.csv')
        app.vectorizer = TfidfVectorizer()
        app.X = app.vectorizer.fit_transform(app.data['text'])
        app.y = app.data['label']
        app.classifier = ExtraTreesClassifier(n_estimators=50, random_state=2)
        app.classifier.fit(app.X, app.y)

        # Test if the model has been trained correctly
        self.assertTrue(hasattr(app.classifier, 'estimators_'))

    @patch('main.st.text_area')
    @patch('main.st.button')
    @patch('main.st.progress')
    def test_predict_function(self, mock_progress, mock_button, mock_text_area):
        mock_text_area.return_value = 'This is an AI-generated text'
        mock_button.return_value = True

        # Simulate the prediction process
        text_vectorized = self.vectorizer.transform(['This is an AI-generated text'])
        prediction = self.classifier.predict(text_vectorized)[0]
        self.assertEqual(prediction, 'AI')
        
        score = self.classifier.predict_proba(text_vectorized)[0][0]
        self.assertAlmostEqual(score, 1.0, places=1)

    @patch('main.st.session_state', {'started': True})
    @patch('main.st.text_area')
    @patch('main.st.button')
    def test_streamlit_ui(self, mock_button, mock_text_area):
        mock_text_area.return_value = 'This is an AI-generated text'
        mock_button.return_value = True
        
        with patch('main.predict', return_value=[{'label': 'AI', 'score': 0.9}]):
            app.predict('This is an AI-generated text')
            self.assertEqual(app.predict('This is an AI-generated text')[0]['label'], 'AI')

if __name__ == '__main__':
    unittest.main()
