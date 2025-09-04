from collections import defaultdict, Counter
plays = [

("UserA", "Song1"),
("UserB", "Song1"),
("UserA", "Song2"),
("UserA", "Song1"),
("UserC", "Song3"),
("UserB", "Song2"),
("UserD", "Song1"),
("UserC", "Song1"),
("UserD", "Song3"),

]

# remove duplicate play records
unique_plays = set(plays)
print("Remove duplicate play records")
print(unique_plays)
print()

# track how many unique songs each user has listened to
user_songs = defaultdict(set)
for user, song in unique_plays:
    user_songs[user].add(song)
user_counts = {user: len(songs) for user, songs in user_songs.items()}
print("Unique songs for each user")
print(user_counts)
print()

# Find the most popular songs
song_counts = Counter()
for user, song in unique_plays:
    song_counts[song] += 1

max_count = max(song_counts.values())
most_popular = [song for song, count in song_counts.items() if count == max_count]
print("Most popular songs")
print(most_popular)
print()

# Output results 