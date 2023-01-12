import sqlite3
from imdb import Cinemagoer
#creating an IMDb object
imdb_obj = Cinemagoer()

#fetching the top 250 movies
top_250 = imdb_obj.get_top250_movies()

#option to reduce it to top10 or whatever
top_250_with_info = [imdb_obj.get_movie(movie.movieID) for movie in top_250[:250]]

#connect to existing db and create cursor
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

#fill database with data from top movies
for movie in top_250_with_info:
    cursor.execute("INSERT INTO movies (id, localized_title, runtime, rating, year) VALUES (?,?,?,?,?)", (movie['imdbID'], movie['localized title'], movie['runtimes'][0], movie['rating'], movie['year']))
    for genre in movie['genre']:
        cursor.execute("INSERT OR IGNORE INTO genres (name) VALUES (?)", (genre,))
        cursor.execute("SELECT id FROM genres WHERE name = (?)", (genre,))
        genre_id = cursor.fetchone()[0]
        cursor.execute("INSERT INTO movie_genres (movie_id, genre_id) VALUES (?,?)", (movie['imdbID'], genre_id))

#print and
conn.commit()
conn.close()
print("Lets fucking go!")

# wichtige felder:
# localized title
# genres
# runtimes[] / runtimes[0]
# rating
# year
# imdbID