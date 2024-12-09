# test_text_to_speech.py

import unittest
from unittest.mock import patch
from modules.text_to_speech import speak, initialize_engine

class TestTextToSpeech(unittest.TestCase):

    @patch("modules.text_to_speech.pyttsx3.init")
    def test_initialize_engine(self, mock_init):
        """
        Teste si le moteur de synthèse vocale est initialisé correctement.
        """
        engine_mock = mock_init.return_value
        engine = initialize_engine()

        # Vérifie que l'initialisation est appelée
        mock_init.assert_called_once()

        # Vérifie que les propriétés par défaut sont définies
        engine_mock.setProperty.assert_any_call("rate", 150)
        engine_mock.setProperty.assert_any_call("volume", 1.0)

    @patch("modules.text_to_speech.pyttsx3.init")
    def test_speak(self, mock_init):
        """
        Teste si la fonction speak appelle correctement le moteur de synthèse vocale.
        """
        engine_mock = mock_init.return_value
        speak("Bonjour, test de synthèse vocale.")

        # Vérifie que la méthode say est appelée avec le bon texte
        engine_mock.say.assert_called_once_with("Bonjour, test de synthèse vocale.")

        # Vérifie que le moteur exécute les commandes
        engine_mock.runAndWait.assert_called_once()

if __name__ == "__main__":
    unittest.main()
