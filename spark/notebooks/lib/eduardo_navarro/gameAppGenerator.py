import random
from datetime import datetime, timedelta
from faker import Faker
import pandas as pd
import uuid

fake = Faker()
Faker.seed(42)
random.seed(42)

# Configuration
NUM_RECORDS = 600  # Total number of gaming activity records

# Game genres and platforms
GENRES = ['FPS', 'RPG', 'Strategy', 'Sports', 'Adventure', 'Puzzle', 'Racing', 'Fighting', 'Simulation', 'Horror']
PLATFORMS = ['PC', 'PS5', 'Xbox', 'Switch', 'PS4', 'Multi-platform']
COUNTRIES = ['USA', 'Mexico', 'Canada', 'Brazil', 'UK', 'Germany', 'France', 'Japan', 'South Korea', 'Australia']

# Pre-generate some reference data
NUM_UNIQUE_USERS = 100
NUM_UNIQUE_GAMES = 10

print("Generating reference users and games...")
users_pool = []
for _ in range(NUM_UNIQUE_USERS):
    users_pool.append({
        'user_id': str(uuid.uuid4()),
        'username': fake.user_name(),
        'email': fake.email(),
        'country': random.choice(COUNTRIES),
        'registration_date': fake.date_between(start_date='-5y', end_date='today'),
        'age': random.randint(13, 65)
    })

games_pool = []
developers = [fake.company() for _ in range(100)]
for _ in range(NUM_UNIQUE_GAMES):
    games_pool.append({
        'game_id': str(uuid.uuid4()),
        'title': fake.catch_phrase().title(),
        'genre': random.choice(GENRES),
        'developer': random.choice(developers),
        'release_date': fake.date_between(start_date='-10y', end_date='today'),
        'price': round(random.uniform(0, 69.99), 2),
        'platform': random.choice(PLATFORMS)
    })

print("Generating combined gaming activity records...")
records = []

for i in range(NUM_RECORDS):
    if i % 5000 == 0:
        print(f"Progress: {i}/{NUM_RECORDS}")
    
    # Select random user and game
    user = random.choice(users_pool)
    game = random.choice(games_pool)
    
    # Calculate valid date ranges
    start_date = max(pd.to_datetime(user['registration_date']), pd.to_datetime(game['release_date']))
    purchase_date = fake.date_between(start_date=start_date, end_date='today')
    session_date = fake.date_between(start_date=purchase_date, end_date='today')
    
    # Generate rating (not all sessions have ratings)
    has_rating = random.random() > 0.4
    rating_value = random.choices([1, 2, 3, 4, 5], weights=[5, 10, 20, 35, 30])[0] if has_rating else None
    review_text = fake.text(max_nb_chars=200) if has_rating and random.random() > 0.3 else ''
    rating_date = session_date if has_rating else None
    
    # Combine all data into one record
    record = {
        # User data
        'user_id': user['user_id'],
        'username': user['username'],
        'email': user['email'],
        'country': user['country'],
        'registration_date': user['registration_date'],
        'age': user['age'],
        
        # Game data
        'game_id': game['game_id'],
        'title': game['title'],
        'genre': game['genre'],
        'developer': game['developer'],
        'release_date': game['release_date'],
        'price': game['price'],
        'platform': game['platform'],
        
        # User-Game relationship
        'purchase_date': purchase_date,
        'hours_played': random.randint(0, 1000),
        'last_played': session_date,
        
        # Session data
        'session_id': str(uuid.uuid4()),
        'session_date': session_date,
        'duration_minutes': random.randint(5, 480),
        'achievements_unlocked': random.choices([0, 1, 2, 3], weights=[60, 25, 10, 5])[0],
        
        # Rating data (nullable)
        'rating_id': str(uuid.uuid4()) if has_rating else None,
        'rating': rating_value,
        'review_text': review_text,
        'rating_date': rating_date
    }
    
    records.append(record)

# Create DataFrame
gaming_data_df = pd.DataFrame(records)

# Save to single CSV
import os

output_path = r'C:\Users\enava\OneDrive - ITESO\Semestres\semestre 7\Big Data\O2025_ESI3914O\spark\data\game_recomendation\\'
os.makedirs(output_path, exist_ok=True)
gaming_data_df.to_csv(f'{output_path}gaming_data_complete.csv', index=False)

print(f"\n✓ Dataset generated successfully!")
print(f"Total records: {len(gaming_data_df):,}")
print(f"Unique users: {gaming_data_df['user_id'].nunique():,}")
print(f"Unique games: {gaming_data_df['game_id'].nunique():,}")
print(f"Records with ratings: {gaming_data_df['rating'].notna().sum():,}")
print(f"\nFile saved to: {output_path}gaming_data_complete.csv")
print(f"\nDataFrame shape: {gaming_data_df.shape}")
print(f"Columns: {list(gaming_data_df.columns)}")