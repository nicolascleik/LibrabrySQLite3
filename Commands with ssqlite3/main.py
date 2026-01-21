import sqlite3

dataBase = sqlite3.connect("tutorial.db")
cur = dataBase.cursor()
#cur.execute("CREATE TABLE movie(title, year, score)")


#res = cur.execute("SELECT name FROM sqlite_master")
#print(res.fetchone())

#cur.execute("""
#    INSERT INTO movie VALUES
#        ('Star wars', 2005, 9.1),
#        ('Star trak', 2001, 9)
#""")
#
#dataBase.commit()

res = cur.execute("SELECT title FROM movie")
#print(res.fetchall()) # -> [('Star wars',), ('Star trak',)]

data = [
    ("Ratatouille", 2007, 8.1),
    ("Maze Runner", 2014, 6.8),
    ("Love and monsters", 2020, 6.9)
]

#cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
#dataBase.commit()

#print(res.fetchall()) #-> [('Star wars',), ('Star trak',), ('Ratatouille',), ('Maze Runner',), ('Love and monsters',)]

#for row in cur.execute("SELECT year, title FROM movie ORDER BY year DESC"):
#    print(row)

#for row in cur.execute("SELECT year, title FROM movie WHERE year > 2007"):
#    print(row)

#cur.execute("UPDATE movie SET title = 'Test' WHERE title = 'Maze Runner'")
#dataBase.commit()

cur.execute("DELETE FROM movie WHERE title = 'Test'")

for row in cur.execute("SELECT title from movie"):
    print(row)