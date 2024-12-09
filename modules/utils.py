# utils.py

import json
import os
import time

def load_settings(file_path="configs/settings.json"):
    """
    Charge les paramètres depuis un fichier JSON.

    :param file_path: str - Chemin du fichier de configuration JSON.
    :return: dict - Dictionnaire contenant les paramètres.
    """
    try:
        with open(file_path, "r") as f:
            settings = json.load(f)
        return settings
    except FileNotFoundError:
        print(f"Erreur : Le fichier de configuration {file_path} est introuvable.")
        return {}
    except json.JSONDecodeError:
        print("Erreur : Le fichier de configuration contient des erreurs de syntaxe.")
        return {}

def save_settings(data, file_path="configs/settings.json"):
    """
    Sauvegarde les paramètres dans un fichier JSON.

    :param data: dict - Dictionnaire contenant les paramètres.
    :param file_path: str - Chemin où sauvegarder le fichier de configuration JSON.
    """
    try:
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Paramètres sauvegardés avec succès dans {file_path}.")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde des paramètres : {e}")

def validate_command(command, keywords):
    """
    Valide si une commande contient l'un des mots-clés spécifiés.

    :param command: str - Commande vocale reconnue.
    :param keywords: list - Liste de mots-clés à rechercher dans la commande.
    :return: bool - True si un mot-clé est présent, sinon False.
    """
    return any(keyword in command.lower() for keyword in keywords)

def delay(seconds):
    """
    Met en pause le programme pour une durée donnée.

    :param seconds: int - Durée en secondes.
    """
    try:
        time.sleep(seconds)
    except Exception as e:
        print(f"Erreur lors du délai : {e}")

def check_file_exists(file_path):
    """
    Vérifie si un fichier existe.

    :param file_path: str - Chemin du fichier à vérifier.
    :return: bool - True si le fichier existe, sinon False.
    """
    return os.path.isfile(file_path)

if __name__ == "__main__":
    # Tests simples des fonctions utilitaires
    print("Test de la fonction load_settings :")
    settings = load_settings()
    print(settings)

    print("\nTest de la fonction save_settings :")
    new_settings = {"language": "fr-FR", "volume": 0.8}
    save_settings(new_settings)

    print("\nTest de la fonction validate_command :")
    print(validate_command("Quelle heure est-il ?", ["heure", "date"]))

    print("\nTest de la fonction check_file_exists :")
    print(check_file_exists("configs/settings.json"))
