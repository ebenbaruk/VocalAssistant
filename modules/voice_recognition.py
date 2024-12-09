# voice_recognition.py

import speech_recognition as sr

def recognize_speech(language="fr-FR"):
    """
    Capture la voix de l'utilisateur et la convertit en texte.

    :param language: str - Code de langue pour la reconnaissance (par défaut "fr-FR" pour le français).
    :return: str - Texte reconnu ou message d'erreur.
    """
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Parlez maintenant...")
            recognizer.adjust_for_ambient_noise(source)  # Ajuster pour le bruit ambiant
            audio = recognizer.listen(source)  # Écoute de l'utilisateur
            print("Traitement en cours...")
            text = recognizer.recognize_google(audio, language=language)
            return text
    except sr.UnknownValueError:
        return "Je n'ai pas compris. Pouvez-vous répéter ?"
    except sr.RequestError as e:
        return f"Erreur du service de reconnaissance vocale : {e}"
    except Exception as e:
        return f"Une erreur inattendue s'est produite : {e}"

if __name__ == "__main__":
    # Test du module
    print("Test de la reconnaissance vocale :")
    result = recognize_speech()
    print(f"Texte reconnu : {result}")
