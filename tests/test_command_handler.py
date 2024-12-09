# test_command_handler.py

import unittest
from modules.command_handler import handle_command

class TestCommandHandler(unittest.TestCase):

    def test_handle_time_command(self):
        """
        Vérifie que la commande pour donner l'heure retourne un texte contenant ":"
        (qui est le format attendu pour l'heure).
        """
        response = handle_command("quelle heure est-il")
        self.assertIn(":", response)

    def test_handle_google_search_command(self):
        """
        Vérifie que la commande de recherche Google retourne une réponse correcte.
        """
        response = handle_command("recherche Python programming")
        self.assertIn("J'ai effectué une recherche Google", response)

    def test_handle_launch_app_command(self):
        """
        Vérifie que la commande pour lancer une application retourne une réponse correcte.
        """
        response = handle_command("lance calculatrice")
        self.assertIn("J'ai lancé l'application", response)

    def test_handle_unknown_command(self):
        """
        Vérifie que les commandes inconnues retournent une réponse appropriée.
        """
        response = handle_command("commande inexistante")
        self.assertEqual(response, "Désolé, je n'ai pas compris cette commande. Pouvez-vous répéter ?")

    def test_handle_stop_command(self):
        """
        Vérifie que la commande pour arrêter retourne le signal "stop".
        """
        response = handle_command("arrête")
        self.assertEqual(response, "stop")


if __name__ == "__main__":
    unittest.main()
