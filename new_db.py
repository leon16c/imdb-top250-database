import sqlite3

# Connect to or create a new SQLite3 database
conn = sqlite3.connect('movies.db')

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Create the 'movies' table
cursor.execute('''
    CREATE TABLE movies (
        id INTEGER PRIMARY KEY,
        localized_title TEXT,
        runtime INTEGER,
        rating REAL,
        year INTEGER
    )
''')

# Create the 'genres' table
cursor.execute('''
    CREATE TABLE genres (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE
    )
''')

# Create the 'movie_genres' table
cursor.execute('''
    CREATE TABLE movie_genres (
        movie_id INTEGER,
        genre_id INTEGER,
        FOREIGN KEY (movie_id) REFERENCES movies(id),
        FOREIGN KEY (genre_id) REFERENCES genres(id)
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
