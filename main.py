# main.py

from modules.voice_recognition import recognize_speech
from modules.text_to_speech import speak
from modules.command_handler import handle_command
from modules.utils import load_settings
import sys

def main():
    """
    Point d'entrée principal de l'assistant vocal.
    """
    # Charger les paramètres
    settings = load_settings("configs/settings.json")
    language = settings.get("language", "fr-FR")
    stop_keywords = settings["commands"]["stop_keywords"]

    # Message de bienvenue
    speak("Bonjour, je suis votre assistant vocal. Dites une commande pour commencer.")
    
    while True:
        # Capturer la commande vocale
        command = recognize_speech(language=language)

        if not command:
            speak("Je n'ai pas entendu votre commande. Veuillez réessayer.")
            continue

        print(f"Commande reconnue : {command}")
        
        # Vérifier si la commande est une commande d'arrêt
        if any(keyword in command.lower() for keyword in stop_keywords):
            speak("Au revoir !")
            break

        # Traiter la commande
        response = handle_command(command)

        # Si la réponse est "stop", quitter la boucle
        if response == "stop":
            speak("Au revoir !")
            break

        # Donner la réponse
        speak(response)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAssistant arrêté par l'utilisateur.")
        speak("Assistant arrêté. À bientôt !")
        sys.exit(0)
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        speak("Une erreur inattendue s'est produite. L'assistant va s'arrêter.")
        sys.exit(1)
