# insert info into movie.db
import sqlite3

con = sqlite3.connect("movie.db")
# line 5,6 to use sql lan in python
cu = con.cursor()
d = cu.execute("SELECT rowid, * from movie WHERE rowid BETWEEN 3 AND 5 ")
# fetchone to get the first row
# fetchmany to get how many rows i want
# fetch all to get all of rows
for i in d:
    print(i)
con.commit()

con.close
