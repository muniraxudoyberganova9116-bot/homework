print("task1") 
import sqlite3

conn = sqlite3.connect('roster.db')
cur = conn.cursor()

print("\n1.Creating table Roster and inserting values to it ")
cur.execute('DROP TABLE IF EXISTS Roster')
cur.execute('CREATE TABLE Roster  (Name TEXT, Species TEXT, Age INTEGER)')

Roster = [('Benjamin Sisko','Human',40), ('Jadzia Dax','Trill',300), ('Kira Nerys','Bajoran',29)]

for roster in Roster:
    cur.execute('INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)', roster)

print("\n2.Updating name of Jadzia to Ezri")
cur.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'")

print("\n3.Query ")
for row in cur.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran' "):
    print(row)

print("\n4.Deleting Age>100")
cur.execute("DELETE FROM Roster WHERE Age > 100 ")

print("\n5.Adding a column Rank and inserting values to it")
cur.execute('ALTER TABLE Roster ADD COLUMN Rank TEXT')
cur.execute("UPDATE Roster SET Rank = 'Captain' WHERE Name = 'Benjamin Sisko'")
cur.execute("UPDATE Roster SET Rank = 'Lieutenant' WHERE Name = 'Ezri Dax'")
cur.execute("UPDATE Roster SET Rank = 'Major' WHERE Name = 'Kira Nerys'")

print("\n6.Query in order by age desc")
for row in cur.execute('SELECT * FROM Roster ORDER BY Age DESC'):
    print(row)

conn.commit()
conn.close()

print("\ntask2")


conn = sqlite3.connect('library.db')
cur = conn.cursor()
print("\n1.Creating table BOOKS and inserting values to it")
cur.execute('DROP TABLE IF EXISTS Books')
cur.execute('CREATE TABLE Books(Title TEXT, Author TEXT, Year_Published INTEGER, Genre TEXT)')

Books = [('To Kill a Mockingbird','Harper Lee',1960,'Fiction'),('1984','George Orwell',1949,'Dystopian'), ('The Great Gatsby','F. Scott Fitzgerald',1925,'Classic') ]
for book in Books:
    cur.execute('INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?,?,?,?)', book)

print("\n2.Updating year ")
cur.execute("UPDATE Books SET Year_Published = 1950 WHERE Title = '1984'")

print("\n3.Query")
for row in cur.execute("SELECT Title , Author FROM Books WHERE Genre = 'Dystopian' "):
    print(row)

print("\n4.Delete year < 1950")
cur.execute("DELETE FROM Books WHERE Year_Published <1950")

print("\n5.Added Column and values to it")
cur.execute("ALTER TABLE Books ADD COLUMN Rating REAL")
cur.execute("UPDATE Books SET Rating = 4.8 WHERE Title = 'To Kill a Mockingbird'")
cur.execute("UPDATE Books SET Rating = 4.7 WHERE Title = '1984'")
cur.execute("UPDATE Books SET Rating = 4.5 WHERE Title = 'The Great Gatsby'")

print("\n6.Advanced query with year asc")
for row in cur.execute("SELECT * FROM Books ORDER BY Year_Published ASC"):
    print(row)
conn.commit()
conn.close()