# command_handler.py

import pywhatkit
import datetime
import os

def handle_command(command):
    """
    Gère les commandes vocales données par l'utilisateur et exécute les actions correspondantes.

    :param command: str - Commande vocale reconnue.
    :return: str - Réponse à retourner à l'utilisateur.
    """
    command = command.lower()

    if "heure" in command:
        # Donne l'heure actuelle
        current_time = datetime.datetime.now().strftime("%H:%M")
        return f"Il est actuellement {current_time}."

    elif "recherche" in command:
        # Effectue une recherche Google
        search_query = command.replace("recherche", "").strip()
        if search_query:
            pywhatkit.search(search_query)
            return f"J'ai effectué une recherche Google pour : {search_query}."
        else:
            return "Désolé, je n'ai pas compris quoi rechercher."

    elif "lance" in command:
        # Lance une application installée sur l'ordinateur
        app_name = command.replace("lance", "").strip()
        if app_name:
            try:
                os.system(f"start {app_name}")
                return f"J'ai lancé l'application : {app_name}."
            except Exception as e:
                return f"Je n'ai pas pu lancer l'application {app_name}. Erreur : {e}"
        else:
            return "Désolé, je n'ai pas compris quelle application lancer."

    elif "arrête" in command or "stop" in command or "quitte" in command:
        # Commande pour arrêter l'assistant
        return "stop"

    else:
        # Commande non reconnue
        return "Désolé, je n'ai pas compris cette commande. Pouvez-vous répéter ?"
