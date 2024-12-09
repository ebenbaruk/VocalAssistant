# test_voice_recognition.py

import unittest
from unittest.mock import patch, MagicMock
from modules.voice_recognition import recognize_speech
import speech_recognition as sr


class TestVoiceRecognition(unittest.TestCase):

    @patch("modules.voice_recognition.sr.Recognizer")
    @patch("modules.voice_recognition.sr.Microphone")
    def test_recognize_speech_success(self, mock_microphone, mock_recognizer):
        """
        Teste si recognize_speech retourne correctement le texte reconnu.
        """
        # Mock de l'objet Recognizer
        recognizer_mock = mock_recognizer.return_value
        recognizer_mock.listen.return_value = "audio_data"
        recognizer_mock.recognize_google.return_value = "test réussi"

        # Appel de la fonction
        result = recognize_speech()
        self.assertEqual(result, "test réussi")

    @patch("modules.voice_recognition.sr.Recognizer")
    @patch("modules.voice_recognition.sr.Microphone")
    def test_recognize_speech_unknown_value_error(self, mock_microphone, mock_recognizer):
        """
        Teste si recognize_speech gère correctement l'erreur UnknownValueError.
        """
        # Mock de l'objet Recognizer
        recognizer_mock = mock_recognizer.return_value
        recognizer_mock.listen.return_value = "audio_data"
        recognizer_mock.recognize_google.side_effect = sr.UnknownValueError

        # Appel de la fonction
        result = recognize_speech()
        self.assertEqual(result, "Je n'ai pas compris. Pouvez-vous répéter ?")

    @patch("modules.voice_recognition.sr.Recognizer")
    @patch("modules.voice_recognition.sr.Microphone")
    def test_recognize_speech_request_error(self, mock_microphone, mock_recognizer):
        """
        Teste si recognize_speech gère correctement l'erreur RequestError.
        """
        # Mock de l'objet Recognizer
        recognizer_mock = mock_recognizer.return_value
        recognizer_mock.listen.return_value = "audio_data"
        recognizer_mock.recognize_google.side_effect = sr.RequestError("Erreur réseau")

        # Appel de la fonction
        result = recognize_speech()
        self.assertIn("Erreur du service de reconnaissance vocale", result)

    @patch("modules.voice_recognition.sr.Recognizer")
    @patch("modules.voice_recognition.sr.Microphone")
    def test_recognize_speech_generic_error(self, mock_microphone, mock_recognizer):
        """
        Teste si recognize_speech gère correctement une erreur générique inattendue.
        """
        # Mock de l'objet Recognizer
        recognizer_mock = mock_recognizer.return_value
        recognizer_mock.listen.side_effect = Exception("Erreur générique")

        # Appel de la fonction
        result = recognize_speech()
        self.assertIn("Une erreur inattendue s'est produite", result)


if __name__ == "__main__":
    unittest.main()
