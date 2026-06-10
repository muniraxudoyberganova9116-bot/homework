import sqlite3 

conn = sqlite3.connect('library.db')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Books')
cur.execute('CREATE TABLE Books(Title TEXT, Author TEXT, Year_Published INTEGER, Genre TEXT)')

Books = [('To Kill a Mockingbird','Harper Lee',1960,'Fiction'),('1984','George Orwell',1949,'Dystopian'), ('The Great Gatsby','F. Scott Fitzgerald',1925,'Classic') ]
for book in Books:
    cur.execute('INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?,?,?,?)', book)

cur.execute("UPDATE Books SET Year_Published = 1950 WHERE Title = '1984'")

for row in cur.execute("SELECT Title , Author FROM Books WHERE Genre = 'Dystopian' "):
    print(row)

cur.execute("DELETE FROM Books WHERE Year_Published <1950")

cur.execute("ALTER TABLE Books ADD COLUMN Rating REAL")
cur.execute("UPDATE Books SET Rating = 4.8 WHERE Title = 'To Kill a Mockingbird'")
cur.execute("UPDATE Books SET Rating = 4.7 WHERE Title = '1984'")
cur.execute("UPDATE Books SET Rating = 4.5 WHERE Title = 'The Great Gatsby'")

for row in cur.execute("SELECT * FROM Books ORDER BY Year_Published ASC"):
    print(row)
conn.commit()
conn.close()