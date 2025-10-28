#!/usr/bin/env python3

import time
import json
import random
from datetime import datetime
from kafka import KafkaProducer


KAFKA_TOPIC = "my-topic"
KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"

def generate_telemetry_data():
    """Generates a single, random video game telemetry event."""
    
    players = ['Player_Alpha', 'Player_Bravo', 'Player_Charlie', 'Player_Delta']
    actions = ['jump', 'run', 'shoot', 'crouch', 'idle', 'open_menu', 'pickup_item']
    devices = ['PC', 'PS5', 'Xbox Series X', 'Mobile']
    
    data = {
        "player_id": random.choice(players),
        "timestamp": datetime.now().isoformat(), 
        "device": random.choice(devices),
        "action": random.choice(actions),
        "speed": round(random.uniform(0.0, 15.0), 2),
        "battery_level": round(random.uniform(5.0, 100.0), 1),
        "location": {
            "latitude": round(random.uniform(-90.0, 90.0), 6),
            "longitude": round(random.uniform(-180.0, 180.0), 6)
        }
    }
    return data


def main():
    """Initializes the Kafka producer and sends data."""
    
    print(f"Connecting to Kafka at {KAFKA_BOOTSTRAP_SERVERS}...")
    
    try:

        producer = KafkaProducer(
            bootstrap_servers=[KAFKA_BOOTSTRAP_SERVERS],
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        print("Successfully connected to Kafka. Starting data production...")
        
        while True:
            data = generate_telemetry_data()
            
            producer.send(KAFKA_TOPIC, value=data)
            
            print(f"Sent: {data}")
            
            time.sleep(1)
            
    except Exception as e:
        print(f"Error connecting to Kafka or sending data: {e}")
        print("Please check that Kafka is running and accessible at 'kafka:9093'.")
    
    finally:
        if 'producer' in locals():
            print("Flushing and closing producer...")
            producer.flush()
            producer.close()

if __name__ == "__main__":
    main()