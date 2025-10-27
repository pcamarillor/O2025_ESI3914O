from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta

fake = Faker()

# Artists chosen by me
artists = [
    "Oasis", "Mumford and Sons", "The Lumineers", "Justin Bieber", "Coldplay",
    "Imagine Dragons", "Modern Baseball", "The Front Bottoms", "The Chainsmokers",
    "Taylor Swift", "Twenty One Pilots", "The Killers", "The Beaches",
    "Stereophonics", "Angus and Julia Stone", "Matt Maeson", "James", "KALEO",
    "My Chemical Romance", "Kanye West", "Lorde", "Sueco", "Bleachers",
    "Radiohead", "Dermot Kennedy", "U2", "Mom Jeans", "Maroon 5",
    "Motion City Soundtrack", "Phoenix", "The Smashing Pumpkins",
    "Glass Animals", "Olivia Rodrigo", "Bring Me The Horizon",
    "Miranda!", "Moderatto", "X Ambassadors", "the 1975", "Arctic Monkeys",
    "Billie Eilish", "Florence and the Machine", "Hozier", "Vampire Weekend",
    "The Strokes", "Foo Fighters", "Red Hot Chili Peppers"
]

num_records = 200
raw_data = []

for _ in range(num_records):
    # Random artist and city
    artist = random.choice(artists)
    city = fake.city()
    event_name = f"{artist} Live in {city}"
    event_id = f"EV-{artist[:3].upper()}-{random.randint(1000,9999)}"

    # User and ticket details
    user = fake.user_name() if random.random() > 0.03 else None  # 3% null usernames
    ticket_count = random.randint(1, 5)
    price_per_ticket = random.uniform(800, 2500)
    total = round(ticket_count * price_per_ticket, 2)

    # Random inconsistency in total
    if random.random() < 0.02:  
        total += random.uniform(50, 300)

    # Payment status and queue metrics
    payment_status = random.choices(
        ["completed", "failed", "pending", None],
        weights=[0.75, 0.15, 0.09, 0.03]
    )[0]
    queue_position = random.randint(1, 50000)
    wait_time = round(random.uniform(20, 400), 2)
    timestamp = fake.date_time_between(start_date='-30d', end_date='now')

    raw_data.append({
        "user": user,
        "event_id": event_id,
        "event_name": event_name,
        "ticket_count": ticket_count,
        "price_per_ticket": round(price_per_ticket, 2),
        "total": total,
        "payment_status": payment_status,
        "queue_position": queue_position,
        "wait_time": wait_time,
        "timestamp": timestamp
    })

# Convert to DataFrame
df_raw = pd.DataFrame(raw_data)

# 1% duplicates
duplicates = df_raw.sample(frac=0.01, random_state=42)
df_raw = pd.concat([df_raw, duplicates], ignore_index=True)

# Shuffle the dataset
df_raw = df_raw.sample(frac=1, random_state=99).reset_index(drop=True)

df_raw.to_csv("../../../data/dirty_ticketmaster_data.csv", index=False)

print("Raw dataset generated successfully!")
df_raw.head(10)
