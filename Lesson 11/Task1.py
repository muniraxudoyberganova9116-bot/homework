import sqlite3

conn = sqlite3.connect('roster.db')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Roster')
cur.execute('CREATE TABLE Roster  (Name TEXT, Species TEXT, Age INTEGER)')

Roster = [('Benjamin Sisko','Human',40), ('Jadzia Dax','Trill',300), ('Kira Nerys','Bajoran',29)]

for roster in Roster:
    cur.execute('INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)', roster)

cur.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'")

print("Query Data")
for row in cur.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran' "):
    print(row)

print("Deleting where age > 100")
cur.execute("DELETE FROM Roster WHERE Age > 100 ")

print("Added the column RANK")
cur.execute('ALTER TABLE Roster ADD COLUMN Rank TEXT')
cur.execute("UPDATE Roster SET Rank = 'Captain' WHERE Name = 'Benjamin Sisko'")
cur.execute("UPDATE Roster SET Rank = 'Lieutenant' WHERE Name = 'Ezri Dax'")
cur.execute("UPDATE Roster SET Rank = 'Major' WHERE Name = 'Kira Nerys'")

print("advanced query age = desc")
for row in cur.execute('SELECT * FROM Roster ORDER BY Age DESC'):
    print(row)

conn.commit()
conn.close()