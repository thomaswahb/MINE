# insert info into movie.db
import sqlite3

con = sqlite3.connect("movie.db")
# line 5,6 to use sql lan in python
cu = con.cursor()
cu.execute("INSERT into movie(name, genre) VALUES('batman', 'action')")
# another way to insert info into movie
cu.execute("INSERT into movie VALUES('batman', 'action', 2023)")
# to active the file
con.commit()

con.close
