import json
import random
import sys
import time
from datetime import datetime, timedelta

from kafka import KafkaProducer


STATIONS = [
    "ST-001",
    "ST-002",
    "ST-003",
    "ST-004",
    "ST-005",
    "ST-006",
    "ST-007",
    "ST-008",
    "ST-009",
    "ST-010"
]

def random_station_id() -> str:
    """Return a random station ID from a fixed list of 10 stations."""
    return random.choice(STATIONS)


def random_timestamp() -> str:
    """Generate a random timestamp within the current year."""
    start = datetime(2025, 1, 1)
    end = datetime(2025, 12, 31)
    delta = end - start
    random_seconds = random.randint(0, int(delta.total_seconds()))
    return (start + timedelta(seconds=random_seconds)).isoformat()


def random_condition() -> str:
    """Select a random weather condition."""
    return random.choice([
        "Sunny",
        "Cloudy",
        "Rainy",
        "Windy",
        "Stormy",
        "Snowy"
    ])


def generate_weather_record() -> dict:
    """Generate a single synthetic weather observation."""
    return {
        "station_id": random_station_id(),
        "timestamp": random_timestamp(),
        "temperature_c": round(random.uniform(-10.0, 45.0), 1),
        "humidity_pct": random.randint(10, 100),
        "wind_speed_m_s": round(random.uniform(0.0, 25.0), 2),
        "pressure_hpa": round(random.uniform(980.0, 1050.0), 2),
        "precipitation_mm": round(random.uniform(0.0, 80.0), 2),
        "condition": random_condition()
    }


def main():
    """Create main Function."""
    if len(sys.argv) != 3:  # noqa: PLR2004
        print("Usage: python weather_producer.py <broker> <topic>")
        sys.exit(1)

    broker, topic = sys.argv[1], sys.argv[2]

    # Initialize Kafka producer
    producer = KafkaProducer(
        bootstrap_servers=[broker],
        value_serializer=lambda v: json.dumps(v, default=str).encode("utf-8")
    )

    print(f"[INFO] Starting Weather Producer -> Broker: {broker}, Topic: {topic}")  # noqa: E501
    try:
        while True:
            record = generate_weather_record()
            producer.send(topic, value=record)
            print(f"[SENT] {record}")
            time.sleep(3)  # send one record every 3 seconds
    except KeyboardInterrupt:
        print("\n[INFO] Producer stopped by user.")
    finally:
        producer.flush()
        producer.close()
        print("[INFO] Producer connection closed.")


if __name__ == "__main__":
    main()
