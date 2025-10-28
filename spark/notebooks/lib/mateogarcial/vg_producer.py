import json
import random
from faker import Faker
from datetime import datetime

class VideogameDataProducer:
    """
    A class to generate simulated videogame data for player events and server state,
    with realistic, parameter-driven de-sync simulation.
    """

    def __init__(self):
        self.fake = Faker()

    def generate_player_event(self, session_id, player_id, event_type="player_move"):
        """Generates a player event with random client positions."""
        event = {
            "session_id": session_id,
            "player_id": player_id,
            "event_id": self.fake.uuid4(),
            "event_type": event_type,
            "client_position_x": round(random.uniform(0, 100), 2),
            "client_position_y": round(random.uniform(0, 100), 2),
            "client_position_z": round(random.uniform(0, 20), 2)
        }
        return json.dumps(event)

    def generate_server_state(self, session_id, player_id, client_pos):
        """
        Generates a server state snapshot that is realistically synced or de-synced
        based on simulated network conditions.
        """
        is_desynced = False
        
        # Determine network quality first
        roll = random.random()
        if roll < 0.15: # 15% chance of poor network
            ping = random.randint(150, 300)
            packet_loss = round(random.uniform(0.05, 0.1), 2)
            if random.random() < 0.8: # 80% chance of de-sync if network is poor
                is_desynced = True
        elif roll < 0.4: # 25% chance of average network
            ping = random.randint(50, 149)
            packet_loss = round(random.uniform(0.01, 0.04), 2)
            if random.random() < 0.25: # 25% chance of de-sync if network is average
                is_desynced = True
        else: # 60% chance of good network
            ping = random.randint(15, 49)
            packet_loss = 0.0
            is_desynced = False # No de-sync on good connection

        # Set server position based on de-sync status
        server_pos_x = client_pos['x']
        server_pos_y = client_pos['y']
        server_pos_z = client_pos['z']

        if is_desynced:
            desync_offset = random.uniform(1.5, 5.0)
            server_pos_x += desync_offset
            server_pos_y += desync_offset
            server_pos_z += desync_offset

        state = {
            "session_id": session_id,
            "player_id": player_id,
            "state_id": self.fake.uuid4(),
            "server_position_x": round(server_pos_x, 2),
            "server_position_y": round(server_pos_y, 2),
            "server_position_z": round(server_pos_z, 2),
            "ping": ping,
            "packet_loss": packet_loss
        }
        return json.dumps(state)