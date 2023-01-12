#establish connection to db
import sqlite3
conn = sqlite3.connect('databases/movies_top_250.db')
cursor = conn.cursor()

#userinput
genre_list = []
line = input()
while line != "":
    genre_list.append(line)
    line = input()

#query
query = 'SELECT DISTINCT movies.localized_title FROM movies INNER JOIN movie_genres ON movies.id = movie_genres.movie_id INNER JOIN genres ON movie_genres.genre_id = genres.id'
placeholders = ' WHERE genres.name = ?'
values = (genre_list[0],)
for i in range(1, len(genre_list)):
    query += f' INNER JOIN movie_genres as mg{i} on movies.id = mg{i}.movie_id INNER JOIN genres as g{i} ON mg{i}.genre_id = g{i}.id'
    placeholders += f' AND g{i}.name = ?'
    values += (genre_list[i],)
query += placeholders
cursor.execute(query, values)

#dumb code to sanitize strings
fetched = cursor.fetchone()
while fetched is not None:
    fetched = str(fetched)
    fetched = fetched.replace('\"', '').replace('(', '').replace(',)', '') if '\"' in fetched else fetched.replace('\'', '').replace('(', '').replace(',)', '')
    print(fetched)
    fetched = cursor.fetchone()

#close connection to db
cursor.close()
conn.close()