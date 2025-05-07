import json
import requests
import threading
from dndnetwork import DungeonMasterServer, PlayerClient
from dice_gold_tools import roll_d20, random_gold
import sys
sys.path.append("c:/Users/labadmin/Desktop/spring2025-labs/Project/")
from dm_ai_tool import generate_rag_narrative




class DungeonMasterAI:
    def __init__(self):
        self.game_log = 'The dungeon awaits your adventurers!'  # initial game log
        self.server = DungeonMasterServer(self.game_log, self.dm_turn_hook)

    def start_server(self):
        self.server.start_server()  # This method blocks until the server is stopped
        
    def dm_turn_hook(self):
        """
        Generates a Dungeon Master narrative using the AI tool, 
        incorporating the game log and a relevant query.
        """
        # Define the query dynamically based on the game log (customize as needed).
        query = "dungeon events, enemy actions, magical atmosphere"

        # Generate narrative using the RAG AI function.
        narrative = generate_rag_narrative(self.game_log, query)
        
        # Ensure the response isn't empty before adding to the game log.
        if narrative.strip():
            self.game_log += f"\nDM: {narrative}"
        
        return narrative


    def stop_server(self):
        try:
            self.server.stop_server()  # Ensure DungeonMasterServer implements this method if needed.
        except AttributeError:
            pass

class Player:
    def __init__(self, name):
        self.name = name
        self.client = PlayerClient(self.name)

    def connect(self):
        self.client.connect()

    def unjoin(self):
        self.client.unjoin()

    def take_turn(self, message):
        self.client.send_message(message)

# --- (Optional) Combat / Other Tools can be here. ---

import threading
import Fighting  # Import combat system

if __name__ == "__main__":
    try:
        # Attempt to start the Dungeon Master server
        dm = DungeonMasterAI()
        dm_thread = threading.Thread(target=dm.start_server, daemon=True)
        dm_thread.start()
        server_active = True
    except Exception:
        print("Dungeon Master server could not start. Running in combat-only mode.")
        server_active = False  # Mark the server as inactive

    player_name = input("Enter your player name: ")
    player = Player(player_name)
    player.connect()

    print(f"Welcome, {player_name}! ")

    while True:
        command = input("> ")

        if command.strip().lower() == "/quit":
            player.unjoin()
            if server_active:
                dm.stop_server()
            print("You have left the dungeon. Farewell, adventurer!")
            break

        elif command.strip().lower() == "/combat":
            print("\nA combat encounter begins!")
            Fighting.combat()  # Call combat function from Fighting.py
            if server_active:
                dm.game_log += f"\n{player_name} engaged in combat!"

        elif server_active:
            player.take_turn(command)
            dm.game_log += f"\n{player_name}: {command}"
        else:
            print("Dungeon Master server is inactive. Only combat is available.")
