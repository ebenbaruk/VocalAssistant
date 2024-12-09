# text_to_speech.py

import pyttsx3

def initialize_engine():
    """
    Initialise le moteur de synthèse vocale et retourne une instance.
    
    :return: pyttsx3.Engine - Instance du moteur pyttsx3 configurée.
    """
    engine = pyttsx3.init()

    # Configurations par défaut
    engine.setProperty('rate', 150)  # Vitesse de la parole (mots par minute)
    engine.setProperty('volume', 1.0)  # Volume (entre 0.0 et 1.0)

    # Configuration de la voix (choisir masculine ou féminine)
    voices = engine.getProperty('voices')
    for voice in voices:
        if "femme" in voice.name.lower():  # Prioriser une voix féminine si disponible
            engine.setProperty('voice', voice.id)
            break

    return engine


def speak(text):
    """
    Convertit un texte donné en parole.

    :param text: str - Texte à lire à haute voix.
    """
    engine = initialize_engine()
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    # Exemple d'utilisation
    print("Test de la synthèse vocale...")
    speak("Bonjour, je suis votre assistant vocal. Comment puis-je vous aider aujourd'hui ?")
