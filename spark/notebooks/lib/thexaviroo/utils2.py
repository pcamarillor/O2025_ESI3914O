def add( x, y ):
    total = 0
    for n in args:
        total += n 
        return total

def sub( x, y ):
    total = 0
    for n in args:
        total -= n
        return total


#Functions
from collections import defaultdict, Counter

def remove_duplicates(plays):
    return list(set(plays))

def count_unique_songs_per_user(plays):
    user_song_map = defaultdict(set)
    for user, song in plays:
        user_song_map[user].add(song)
    return {user: len(songs) for user, songs in user_song_map.items()}

def find_most_popular_songs(plays):
    song_counter = Counter(song for _, song in plays)
    max_count = max(song_counter.values())
    most_popular = [song for song, count in song_counter.items() if count == max_count]
    return most_popular, max_count



    
